---
title: HTTP Requests with the requests Library
description: "Replace curl | jq with Python's requests library — GET, POST, JSON handling, error checking, headers, timeouts, and sessions for real API automation."
---

# HTTP Requests with the requests Library

You already use `curl` to hit APIs, check health endpoints, and pull data from web services.
It works. But `curl | jq` pipelines break on nested JSON, error handling is manual (`-f` and
`$?`), and anything beyond a simple GET becomes a wall of flags.

Python's `requests` library is the `curl` you wish you had — clean syntax, automatic JSON
parsing, proper error handling, and session management for authenticated API clients.

## Coming from Bash

```bash title="Bash: curl + jq" linenums="1"
# GET request
curl -s https://api.github.com/repos/kubernetes/kubernetes | jq '.stargazers_count'

# POST with JSON body
curl -s -X POST https://api.example.com/deployments \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $API_TOKEN" \
    -d '{"environment": "prod", "tag": "v2.1.0"}' | jq '.id'

# Error checking
response=$(curl -s -o /tmp/response.json -w "%{http_code}" https://api.example.com/status)
if [[ "$response" != "200" ]]; then
    echo "Error: HTTP $response" >&2
    exit 1
fi
```

```python title="Python: requests" linenums="1"
import requests

# GET request
r = requests.get("https://api.github.com/repos/kubernetes/kubernetes")
print(r.json()["stargazers_count"])

# POST with JSON body
r = requests.post(
    "https://api.example.com/deployments",
    json={"environment": "prod", "tag": "v2.1.0"},
    headers={"Authorization": f"Bearer {api_token}"},
)
print(r.json()["id"])

# Error checking — raise on 4xx/5xx
r = requests.get("https://api.example.com/status")
r.raise_for_status()   # Raises requests.HTTPError if status >= 400
```

Key differences:

| Bash (`curl`) | Python (`requests`) |
|:--------------|:--------------------|
| `curl -s URL \| jq '.key'` | `requests.get(url).json()["key"]` |
| `-H "Content-Type: application/json"` | Set automatically with `json=` parameter |
| `-d '{"key": "value"}'` | `json={"key": "value"}` — no manual serialization |
| `-w "%{http_code}"` + check | `r.raise_for_status()` — raises on error |
| `-f` (fail on 4xx) | `r.raise_for_status()` in try/except |
| `-o file` to capture body | `r.text`, `r.json()`, `r.content` directly |

## Installation

`requests` is not in the standard library — install it with pip:

```bash title="Install requests"
pip install requests
```

For scripts in a project, add it to your `requirements.txt` or `pyproject.toml`.

## GET Requests

```python title="Basic GET" linenums="1"
import requests

response = requests.get("https://httpbin.org/get")    # (1)!

print(response.status_code)    # 200
print(response.headers["Content-Type"])               # (2)!
print(response.text)           # Raw response body as string
print(response.json())         # Parsed JSON as dict/list
```

1. `requests.get()` sends the request and waits for the response synchronously
2. `response.headers` is a case-insensitive dict of response headers

### Query Parameters

Pass query parameters as a dict — `requests` handles URL encoding:

```python title="Query Parameters" linenums="1"
import requests

# These are equivalent:
# requests.get("https://api.example.com/logs?level=ERROR&limit=100")
response = requests.get(
    "https://api.example.com/logs",
    params={"level": "ERROR", "limit": 100}    # (1)!
)

print(response.url)   # https://api.example.com/logs?level=ERROR&limit=100
```

1. `params=` handles URL encoding automatically — special characters, spaces, etc. are escaped

## Working with JSON Responses

Most APIs return JSON. `response.json()` parses it into Python dicts and lists:

```python title="JSON Response" linenums="1"
import requests

response = requests.get("https://api.github.com/repos/python/cpython")
response.raise_for_status()

repo = response.json()                         # dict

# Navigate like any Python dict
print(repo["name"])                            # cpython
print(repo["stargazers_count"])                # integer
print(repo["owner"]["login"])                  # nested access
print(repo.get("description", "No description"))  # safe access

# List response
response = requests.get("https://api.github.com/repos/python/cpython/tags")
tags = response.json()                         # list

for tag in tags[:5]:
    print(tag["name"])                         # iterate normally
```

## POST Requests

### JSON Body

Pass `json=` and `requests` sets `Content-Type: application/json` automatically:

```python title="POST with JSON Body" linenums="1"
import requests

payload = {
    "name": "web-deployment",
    "environment": "prod",
    "image": "myapp:v2.1.0",
    "replicas": 3,
}

response = requests.post(
    "https://api.example.com/deployments",
    json=payload,                              # (1)!
)
response.raise_for_status()

created = response.json()
print(f"Deployment ID: {created['id']}")
print(f"Status: {created['status']}")
```

1. `json=payload` serializes the dict to JSON and sets the correct Content-Type header automatically

### Form Data

For form-encoded POST (like `curl -F`):

```python title="Form POST" linenums="1"
import requests

response = requests.post(
    "https://api.example.com/upload",
    data={"key": "value", "other": "thing"}    # (1)!
)
```

1. `data=` sends `application/x-www-form-urlencoded` — what HTML forms submit

## Headers

Set request headers as a dict:

```python title="Custom Headers" linenums="1"
import requests
import os

headers = {
    "Authorization": f"Bearer {os.environ['API_TOKEN']}",   # (1)!
    "X-Request-ID": "deploy-20240115-001",
    "User-Agent": "myapp-deployer/1.0",
}

response = requests.get(
    "https://api.example.com/clusters",
    headers=headers,
)
response.raise_for_status()
```

1. Read the token from an environment variable — never hardcode credentials in source

## Error Handling

### raise_for_status()

```python title="Error Handling" linenums="1"
import requests

try:
    response = requests.get("https://api.example.com/pods")
    response.raise_for_status()                        # (1)!
    pods = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code} {e.response.reason}")
    print(f"Response body: {e.response.text}")
    raise
except requests.exceptions.ConnectionError:            # (2)!
    print("Could not connect to API — is the endpoint reachable?")
    raise
except requests.exceptions.Timeout:
    print("Request timed out")
    raise
```

1. `raise_for_status()` raises `HTTPError` for 4xx and 5xx responses — does nothing for 2xx
2. `ConnectionError` for network failures (DNS, refused connection, etc.)

### Common Exception Types

| Exception | When It Occurs |
|:----------|:---------------|
| `requests.exceptions.HTTPError` | 4xx or 5xx response (after `raise_for_status()`) |
| `requests.exceptions.ConnectionError` | Network failure — DNS, refused, unreachable |
| `requests.exceptions.Timeout` | Request exceeded the timeout |
| `requests.exceptions.TooManyRedirects` | Too many redirects |
| `requests.exceptions.RequestException` | Base class — catches all of the above |

## Timeouts

Always set a timeout — without one, your script can hang indefinitely:

```python title="Timeouts" linenums="1"
import requests

# Raise Timeout if no response within 10 seconds
response = requests.get("https://api.example.com/health", timeout=10)   # (1)!

# Separate connect and read timeouts
response = requests.get(
    "https://api.example.com/health",
    timeout=(3, 30)    # (2)!
)
```

1. `timeout=10` — total seconds to wait for a response
2. `(connect_timeout, read_timeout)` — 3 seconds to connect, 30 seconds to read the response

## Sessions

When making multiple requests to the same API, use a `Session` to reuse the connection and
share headers:

```python title="Session for Multiple Requests" linenums="1"
import requests
import os

with requests.Session() as session:            # (1)!
    session.headers.update({                   # (2)!
        "Authorization": f"Bearer {os.environ['API_TOKEN']}",
        "Accept": "application/json",
    })

    # All requests share headers and connection pool
    clusters = session.get("https://api.example.com/clusters").json()
    for cluster in clusters:
        status = session.get(
            f"https://api.example.com/clusters/{cluster['id']}/status"
        ).json()
        print(f"{cluster['name']}: {status['phase']}")
```

1. `Session` as a context manager — connection is closed when the `with` block exits
2. Headers set on the session apply to all requests — set auth headers once, not per-request

## A Complete API Client

Here's a reusable pattern for API clients:

```python title="API Client Pattern" linenums="1"
import logging
import os
import requests

log = logging.getLogger(__name__)


class DeploymentClient:
    """Client for the deployment API."""

    def __init__(self, base_url: str, token: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def _get(self, path: str, **kwargs) -> dict:
        url = f"{self.base_url}{path}"
        log.debug("GET %s", url)
        response = self.session.get(url, timeout=self.timeout, **kwargs)
        response.raise_for_status()
        return response.json()

    def _post(self, path: str, payload: dict) -> dict:
        url = f"{self.base_url}{path}"
        log.debug("POST %s %s", url, payload)
        response = self.session.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def list_deployments(self, environment: str) -> list:
        return self._get("/deployments", params={"environment": environment})

    def create_deployment(self, environment: str, tag: str) -> dict:
        return self._post("/deployments", {
            "environment": environment,
            "tag": tag,
        })


# Usage
client = DeploymentClient(
    base_url=os.environ["API_URL"],
    token=os.environ["API_TOKEN"],
)

deployments = client.list_deployments("prod")
new_deploy = client.create_deployment("prod", "v2.1.0")
```

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`requests.get(url)`** | Send a GET request; returns a `Response` object |
| **`requests.post(url, json={})`** | POST with JSON body; sets Content-Type automatically |
| **`response.json()`** | Parse response body as JSON → Python dict/list |
| **`response.raise_for_status()`** | Raise `HTTPError` on 4xx/5xx; no-op on 2xx |
| **`timeout=10`** | Always set — prevents hanging on unresponsive servers |
| **`params={}`** | Query string — URL-encoded automatically |
| **`headers={}`** | Request headers dict |
| **`requests.Session()`** | Reuse connection + share headers across requests |
| **`requests.exceptions.RequestException`** | Base exception — catches all request errors |

## Practice Problems

??? question "Practice Problem 1: Check Multiple Endpoints"

    Write a function `check_endpoints(urls: list[str]) -> dict` that GETs each URL
    and returns a dict of `{url: status_code}`. Use a timeout of 5 seconds.
    On any exception, map the URL to `0`.

    ??? tip "Answer"

        ```python title="Check Endpoints" linenums="1"
        import requests

        def check_endpoints(urls: list[str]) -> dict:
            results = {}
            for url in urls:
                try:
                    response = requests.get(url, timeout=5)
                    results[url] = response.status_code
                except requests.exceptions.RequestException:
                    results[url] = 0
            return results

        status = check_endpoints([
            "https://api.github.com",
            "https://unreachable.example.com",
        ])
        # {'https://api.github.com': 200, 'https://unreachable.example.com': 0}
        ```

        `requests.exceptions.RequestException` is the base class — catching it
        handles network errors, timeouts, and HTTP errors in one clause.

??? question "Practice Problem 2: Paginated API Response"

    Many APIs return paginated results with a `next` URL in the response. Write a
    function `get_all_pages(url: str, headers: dict) -> list` that follows pagination
    until there's no `next` link, collecting all results.

    Assume each page returns `{"items": [...], "next": "url-or-null"}`.

    ??? tip "Answer"

        ```python title="Paginated Fetch" linenums="1"
        import requests

        def get_all_pages(url: str, headers: dict) -> list:
            all_items = []
            current_url = url

            while current_url:
                response = requests.get(current_url, headers=headers, timeout=30)
                response.raise_for_status()
                data = response.json()
                all_items.extend(data["items"])     # (1)!
                current_url = data.get("next")      # None stops the loop

            return all_items
        ```

        1. `list.extend()` adds all items from the page to the running list —
           use `extend` (not `append`) when adding multiple items at once.

??? question "Practice Problem 3: POST with Error Detail"

    Write a function `create_resource(url: str, payload: dict, token: str)` that
    POSTs the payload. On HTTP error, print the status code and response body before
    re-raising. On success, return the parsed JSON response.

    ??? tip "Answer"

        ```python title="POST with Error Detail" linenums="1"
        import requests

        def create_resource(url: str, payload: dict, token: str) -> dict:
            response = requests.post(
                url,
                json=payload,
                headers={"Authorization": f"Bearer {token}"},
                timeout=30,
            )
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(f"HTTP {e.response.status_code}: {e.response.text}")
                raise
            return response.json()
        ```

        Logging the response body before re-raising is crucial for debugging — a
        bare `raise_for_status()` only tells you the status code, not why it failed.

??? question "Practice Problem 4: curl vs requests"

    Convert this `curl` command to Python using `requests`:

    ```bash
    curl -s -X DELETE \
        https://api.example.com/pods/web-01 \
        -H "Authorization: Bearer $TOKEN" \
        -H "X-Confirm: yes" \
        -w "\nStatus: %{http_code}\n"
    ```

    ??? tip "Answer"

        ```python title="DELETE Request" linenums="1"
        import os
        import requests

        response = requests.delete(
            "https://api.example.com/pods/web-01",
            headers={
                "Authorization": f"Bearer {os.environ['TOKEN']}",
                "X-Confirm": "yes",
            },
            timeout=30,
        )
        response.raise_for_status()
        print(f"Status: {response.status_code}")
        ```

        `requests.delete()`, `requests.put()`, and `requests.patch()` follow the
        same pattern as `get()` and `post()`.

## Further Reading

### On This Site

- [Working with JSON](../essentials/working_with_json.md) — navigating the API responses `requests` returns
- [Error Handling](../essentials/error_handling.md) — wrapping `raise_for_status()` in try/except
- [Environment Variables and Secrets](environment_and_secrets.md) — storing API tokens safely in env vars
- [Logging](logging.md) — logging request/response details for debugging

### Official Documentation

- [requests — Official Docs](https://docs.python-requests.org/) — full reference with examples

### External Resources

- [httpx](https://www.python-httpx.org/) — modern alternative to `requests` with async support and HTTP/2
- [urllib3](https://urllib3.readthedocs.io/) — the lower-level library `requests` is built on

---

`requests` is the `curl` replacement you actually want to use in Python. Install it once,
learn `get()`, `post()`, `raise_for_status()`, and `json()` — that covers 90% of API work.
Add `Session()` for authenticated clients that make multiple requests.
