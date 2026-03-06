---
title: REST API Patterns in Python
description: "Pagination, rate limiting, retry logic, and reusable API client classes — practical patterns for production API automation in Python."
---

# REST API Patterns

A single `requests.get()` call is straightforward. Real API automation is not. APIs paginate
large result sets. They enforce rate limits. They fail transiently and need retries. You end
up calling the same endpoint dozens of times with slightly different parameters.

This article covers the patterns that turn one-off API calls into reliable, reusable
automation.

## Coming from Bash

In Bash, API pagination means a `while` loop, manual `jq` extraction, and no retry logic:

```bash title="Bash: Manual Pagination and Retry"
# Paginate a GitHub API — manual while loop
page=1
while true; do
    response=$(curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
        "https://api.github.com/orgs/myorg/repos?per_page=100&page=$page")

    count=$(echo "$response" | jq '. | length')
    [[ "$count" -eq 0 ]] && break

    echo "$response" | jq -r '.[].name'
    page=$((page + 1))
done

# Retry: manual loop with sleep
for attempt in 1 2 3; do
    response=$(curl -sf https://api.example.com/data) && break
    echo "Attempt $attempt failed, retrying..." >&2
    sleep $((2 ** attempt))
done
```

```python title="Python: Reusable Pagination and Retry"
# Pagination: reusable function
def get_all_pages(url, headers):
    items = []
    page = 1
    while True:
        data = requests.get(url, headers=headers,
                            params={"per_page": 100, "page": page}).json()
        if not data:
            break
        items.extend(data)
        page += 1
    return items

# Retry: backoff built into a helper or class
# (See examples below)
```

The Python patterns — pagination generators, retry with backoff, rate-limited sessions —
are reusable across all your scripts. The Bash equivalent needs to be re-implemented in every
script that calls an API.

## Pagination

APIs rarely return all results in one response. They paginate — returning a page of results
with a pointer to the next page:

### Link Header Pagination (GitHub style)

```python title="Link Header Pagination" linenums="1"
import requests
import re
import os


def get_all_pages(url: str, headers: dict, params: dict | None = None) -> list:
    """Fetch all pages from a Link-header paginated API."""
    results = []
    current_url = url
    current_params = params or {}

    while current_url:
        response = requests.get(current_url, headers=headers,
                                params=current_params, timeout=30)
        response.raise_for_status()
        results.extend(response.json())         # (1)!

        # Parse Link header for next page URL
        link_header = response.headers.get("Link", "")
        next_url = None

        for part in link_header.split(","):     # (2)!
            if 'rel="next"' in part:
                match = re.search(r"<([^>]+)>", part)
                if match:
                    next_url = match.group(1)
                    break

        current_url = next_url
        current_params = {}                     # URL includes params after first page

    return results


# Usage: get all repos in an organization
headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
repos = get_all_pages(
    "https://api.github.com/orgs/kubernetes/repos",
    headers=headers,
    params={"per_page": 100, "type": "public"},
)
print(f"Found {len(repos)} repos")
```

1. `extend()` adds all items from the page to the running list
2. GitHub's `Link` header looks like: `<url>; rel="next", <url>; rel="last"` — parse it

### Offset/Cursor Pagination (JSON response)

Many APIs return pagination info in the response body:

```python title="Cursor-Based Pagination" linenums="1"
import requests
import os


def get_all_items(base_url: str, headers: dict) -> list:
    """Fetch all items from a cursor-paginated API."""
    items = []
    cursor = None

    while True:
        params = {"limit": 100}
        if cursor:
            params["cursor"] = cursor               # (1)!

        response = requests.get(base_url, headers=headers,
                                params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        items.extend(data["items"])

        cursor = data.get("next_cursor")            # (2)!
        if not cursor:
            break

    return items
```

1. Send the cursor as a query parameter on each request after the first
2. `next_cursor` is `None` (or absent) when there are no more pages

### Page Number Pagination

```python title="Page Number Pagination" linenums="1"
import requests


def get_all_pages_numbered(url: str, headers: dict) -> list:
    """Fetch all pages from a page-number paginated API."""
    results = []
    page = 1

    while True:
        response = requests.get(
            url,
            headers=headers,
            params={"page": page, "per_page": 100},
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()

        if not data["items"]:                       # (1)!
            break

        results.extend(data["items"])
        page += 1

        if page > data.get("total_pages", page):    # (2)!
            break

    return results
```

1. Stop when an empty page is returned — simplest termination condition
2. Stop when we've passed the last page, if the API tells us the total

## Retry Logic

APIs fail transiently — network blips, rate limits, temporary server errors. Retry with
exponential backoff:

```python title="Retry with Exponential Backoff" linenums="1"
import time
import requests
import logging

log = logging.getLogger(__name__)

RETRY_STATUSES = {429, 500, 502, 503, 504}    # (1)!


def get_with_retry(
    url: str,
    headers: dict,
    max_retries: int = 3,
    backoff_base: float = 1.0,
    **kwargs,
) -> requests.Response:
    """GET with exponential backoff retry."""

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=30, **kwargs)

            if response.status_code not in RETRY_STATUSES:
                response.raise_for_status()
                return response

            if attempt == max_retries - 1:
                response.raise_for_status()

            wait = backoff_base * (2 ** attempt)   # (2)!
            log.warning(
                "HTTP %d on attempt %d/%d, retrying in %.1fs",
                response.status_code, attempt + 1, max_retries, wait,
            )
            time.sleep(wait)

        except requests.exceptions.ConnectionError as e:
            if attempt == max_retries - 1:
                raise
            wait = backoff_base * (2 ** attempt)
            log.warning("Connection error on attempt %d, retrying in %.1fs: %s",
                        attempt + 1, wait, e)
            time.sleep(wait)

    raise RuntimeError("Retry logic error — should not reach here")
```

1. These status codes are safe to retry: `429` (rate limited), `5xx` (server errors)
2. Exponential backoff: 1s, 2s, 4s, 8s... — reduces load on struggling servers

### Respecting Retry-After

Many APIs return a `Retry-After` header on `429` responses:

```python title="Respect Retry-After Header" linenums="1"
import time
import requests


def get_with_rate_limit(url: str, headers: dict, **kwargs) -> requests.Response:
    """GET that respects Retry-After on 429 responses."""
    while True:
        response = requests.get(url, headers=headers, timeout=30, **kwargs)

        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 60))   # (1)!
            print(f"Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
            continue

        response.raise_for_status()
        return response
```

1. `Retry-After` is in seconds — wait exactly as long as the server asks, not less

## Rate Limiting

Proactive rate limiting — slow your script down to stay within the API's limits:

```python title="Proactive Rate Limiting" linenums="1"
import time
import requests


class RateLimitedSession:
    """Session that enforces a maximum request rate."""

    def __init__(self, requests_per_second: float = 5.0):
        self._session = requests.Session()
        self._min_interval = 1.0 / requests_per_second   # (1)!
        self._last_request = 0.0

    def get(self, url: str, **kwargs) -> requests.Response:
        self._wait_for_rate_limit()
        response = self._session.get(url, **kwargs)
        self._last_request = time.monotonic()
        return response

    def _wait_for_rate_limit(self) -> None:
        elapsed = time.monotonic() - self._last_request
        wait = self._min_interval - elapsed
        if wait > 0:
            time.sleep(wait)


# Usage: max 5 requests/second
session = RateLimitedSession(requests_per_second=5)
for resource_id in resource_ids:
    data = session.get(f"https://api.example.com/items/{resource_id}").json()
```

1. `1 / requests_per_second` gives the minimum interval between requests

## A Reusable API Client

Combine authentication, retry, rate limiting, and pagination into one class:

```python title="Production API Client" linenums="1"
import logging
import os
import time
from typing import Any, Iterator

import requests

log = logging.getLogger(__name__)


class APIClient:
    """Reusable authenticated API client with retry and rate limiting."""

    RETRY_STATUSES = {429, 500, 502, 503, 504}

    def __init__(
        self,
        base_url: str,
        token: str | None = None,
        max_retries: int = 3,
        timeout: int = 30,
        requests_per_second: float = 10.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.max_retries = max_retries
        self.timeout = timeout
        self._min_interval = 1.0 / requests_per_second
        self._last_request = 0.0

        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token or os.environ['API_TOKEN']}",
            "Accept": "application/json",
        })

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        """Make a request with retry and rate limiting."""
        url = f"{self.base_url}{path}"

        for attempt in range(self.max_retries):
            # Rate limiting
            elapsed = time.monotonic() - self._last_request
            if elapsed < self._min_interval:
                time.sleep(self._min_interval - elapsed)

            try:
                response = self._session.request(
                    method, url, timeout=self.timeout, **kwargs
                )
                self._last_request = time.monotonic()

                if response.status_code in self.RETRY_STATUSES:
                    if attempt == self.max_retries - 1:
                        response.raise_for_status()
                    retry_after = int(response.headers.get("Retry-After", 2 ** attempt))
                    log.warning("HTTP %d, retrying in %ds", response.status_code, retry_after)
                    time.sleep(retry_after)
                    continue

                response.raise_for_status()
                return response

            except requests.exceptions.ConnectionError:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)

        raise RuntimeError("Should not reach here")

    def get(self, path: str, **kwargs) -> Any:
        return self._request("GET", path, **kwargs).json()

    def post(self, path: str, payload: dict) -> Any:
        return self._request("POST", path, json=payload).json()

    def paginate(self, path: str, **kwargs) -> Iterator[dict]:
        """Yield all items from a paginated endpoint."""
        params = kwargs.pop("params", {})
        params["per_page"] = 100
        page = 1

        while True:
            params["page"] = page
            data = self.get(path, params=params, **kwargs)

            items = data if isinstance(data, list) else data.get("items", [])
            if not items:
                break

            yield from items
            page += 1


# Usage
client = APIClient("https://api.example.com")

# Simple request
cluster = client.get("/clusters/prod-01")

# Paginated — yields each item one at a time
for deployment in client.paginate("/deployments", params={"environment": "prod"}):
    print(deployment["name"], deployment["status"])
```

## Parallel Requests

When you need to fetch many independent resources, parallel requests are faster:

```python title="Parallel Requests with ThreadPoolExecutor" linenums="1"
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def fetch_resource(session: requests.Session, resource_id: str) -> dict:
    response = session.get(
        f"https://api.example.com/resources/{resource_id}",
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def fetch_all(resource_ids: list[str], max_workers: int = 5) -> list[dict]:
    headers = {"Authorization": f"Bearer {os.environ['API_TOKEN']}"}

    with requests.Session() as session:
        session.headers.update(headers)

        with ThreadPoolExecutor(max_workers=max_workers) as executor:    # (1)!
            futures = {
                executor.submit(fetch_resource, session, rid): rid
                for rid in resource_ids
            }
            results = []
            for future in as_completed(futures):
                try:
                    results.append(future.result())
                except Exception as e:
                    print(f"Failed: {futures[future]}: {e}")

    return results


# Fetch 50 resources with up to 5 concurrent requests
resources = fetch_all(resource_ids, max_workers=5)
```

1. `ThreadPoolExecutor` runs requests concurrently — but respect the API's rate limits

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **Link header** | GitHub-style: `<url>; rel="next"` tells you the next page URL |
| **Cursor pagination** | Response includes `next_cursor`; pass it back as a parameter |
| **Exponential backoff** | Wait 1s, 2s, 4s... between retries — don't hammer the server |
| **`Retry-After` header** | Wait exactly as long as the server says on a 429 response |
| **Proactive rate limiting** | Slow yourself down before hitting limits |
| **`Session`** | Reuse connections and headers across many requests |
| **`yield from`** | Paginate lazily — caller gets items one at a time |
| **`ThreadPoolExecutor`** | Parallel requests for independent resources |

## Practice Problems

??? question "Practice Problem 1: Paginate a List Endpoint"

    Write a function `list_all_pods(namespace: str, token: str) -> list` that
    fetches all pods from a Kubernetes-style API. Assume the API returns
    `{"items": [...], "continue": "token-or-null"}` and accepts `continue` as a
    query parameter for the next page.

    ??? tip "Answer"

        ```python title="Kubernetes-Style Pagination" linenums="1"
        import requests


        def list_all_pods(namespace: str, token: str) -> list:
            headers = {"Authorization": f"Bearer {token}"}
            pods = []
            continue_token = None

            while True:
                params = {"limit": 500}
                if continue_token:
                    params["continue"] = continue_token

                response = requests.get(
                    f"https://k8s.example.com/api/v1/namespaces/{namespace}/pods",
                    headers=headers,
                    params=params,
                    timeout=30,
                )
                response.raise_for_status()
                data = response.json()
                pods.extend(data["items"])

                continue_token = data.get("continue")
                if not continue_token:
                    break

            return pods
        ```

??? question "Practice Problem 2: Retry with Backoff"

    Write a function `post_with_retry(url, payload, headers, max_retries=3)` that
    POSTs the payload and retries on `429` or `503` with exponential backoff.
    On other errors, raise immediately.

    ??? tip "Answer"

        ```python title="POST with Retry" linenums="1"
        import time
        import requests

        RETRY_STATUSES = {429, 503}


        def post_with_retry(
            url: str,
            payload: dict,
            headers: dict,
            max_retries: int = 3,
        ) -> dict:
            for attempt in range(max_retries):
                response = requests.post(url, json=payload, headers=headers, timeout=30)

                if response.status_code in RETRY_STATUSES:
                    if attempt == max_retries - 1:
                        response.raise_for_status()
                    wait = 2 ** attempt
                    print(f"HTTP {response.status_code}, retrying in {wait}s...")
                    time.sleep(wait)
                    continue

                response.raise_for_status()
                return response.json()

            raise RuntimeError("Max retries exceeded")
        ```

??? question "Practice Problem 3: Respect Rate Limits"

    A loop makes 200 API calls. The API allows 10 requests per second.
    How would you add rate limiting without checking the clock on every request?

    ??? tip "Answer"

        ```python title="Simple Rate Limit" linenums="1"
        import time
        import requests

        MIN_INTERVAL = 0.1  # 1/10 requests per second = 100ms between requests

        last_request = 0.0

        for item_id in item_ids:
            # Wait if we're going too fast
            elapsed = time.monotonic() - last_request
            if elapsed < MIN_INTERVAL:
                time.sleep(MIN_INTERVAL - elapsed)

            response = requests.get(f"https://api.example.com/items/{item_id}")
            response.raise_for_status()
            last_request = time.monotonic()
            process(response.json())
        ```

        For more complex cases, wrap it in the `RateLimitedSession` class shown earlier.

??? question "Practice Problem 4: When to Retry"

    For each HTTP status code, decide: retry, raise immediately, or handle specially?

    - `200` — success
    - `400` — bad request
    - `401` — unauthorized
    - `429` — too many requests
    - `404` — not found
    - `500` — internal server error
    - `503` — service unavailable

    ??? tip "Answer"

        | Status | Action |
        |:-------|:-------|
        | `200` | Return the response — success |
        | `400` | Raise immediately — your request is malformed; retrying won't help |
        | `401` | Raise immediately — your credentials are wrong or expired |
        | `429` | Retry after waiting (respect `Retry-After` header) |
        | `404` | Raise immediately — the resource doesn't exist |
        | `500` | Retry a few times — server error may be transient |
        | `503` | Retry with backoff — server temporarily unavailable |

        The rule: retry transient errors (`429`, `5xx`). Raise immediately on client
        errors (`4xx` except `429`) — retrying won't fix a bad request.

## Further Reading

### On This Site

- [HTTP Requests](http_requests.md) — the basics before adding pagination and retry
- [Authentication](authentication.md) — setting up auth before handling pagination
- [Error Handling](../scripting_fundamentals/error_handling.md) — try/except patterns for API errors

### Official Documentation

- [requests — Official Docs](https://docs.python-requests.org/)
- [urllib3 Retry](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.retry.html) — lower-level retry implementation

### External Resources

- [Tenacity](https://tenacity.readthedocs.io/) — decorator-based retry library; cleaner for complex retry policies
- [httpx](https://www.python-httpx.org/) — modern `requests` alternative with async support

---

Pagination, retry, and rate limiting aren't optional polish — they're what separates a
script that works once from one that runs reliably in production. Build them in from the
start rather than adding them after the first 3am page.
