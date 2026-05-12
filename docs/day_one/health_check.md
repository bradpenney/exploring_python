---
title: "Is It Still Up? Health Checking During Redeploys"
description: "Write a Python health-check poller that distinguishes connection errors from HTTP errors, handles timeouts, and exits cleanly for use in deployment pipelines."
---

# Is It Still Up?

!!! tip "Part of Day One"
    This is part of [Day One: Python for Platform Engineers](overview.md).

You're deploying. Traffic is cut over to the new pods, the old ones are terminating, and you need to know the moment your API is healthy again before you proceed. Your options: sit there hitting refresh, write a `curl` loop in `bash`, or do it properly.

This is where Python earns its place. Not because `curl` can't poll — it can. Because you need to know *why* the check failed, not just that it did.

---

## The Bash Version and Its Problem

```bash title="Bash health poller"
while ! curl -sf http://api.internal/health; do
  sleep 5
done
echo "API is up"
```

This works for interactive use. In a deployment pipeline, it has problems:

- No timeout — it'll run forever if the API never comes back
- No distinction between "connection refused" (server not started yet) and "HTTP 503" (server started, app not ready)
- Exit code is from `curl`, not from your intent — harder to integrate with pipeline logic
- No useful output about how long it waited

---

## The Python Version

```python title="health_check.py" linenums="1"
import requests
import time
import sys


def wait_for_health(url, timeout=120, interval=5):
    """Poll url until it returns HTTP 200 or timeout expires.
    
    Returns True if healthy, False if timed out.
    """
    start = time.time()

    while True:
        elapsed = time.time() - start

        if elapsed >= timeout:
            return False

        try:
            resp = requests.get(url, timeout=3)  # (1)!
            if resp.status_code == 200:
                print(f"✓ {url} is healthy ({elapsed:.0f}s)")
                return True
            else:
                print(f"  HTTP {resp.status_code} ({elapsed:.0f}s / {timeout}s)")

        except requests.exceptions.ConnectionError:
            print(f"  Connection refused ({elapsed:.0f}s / {timeout}s)")  # (2)!

        except requests.exceptions.Timeout:
            print(f"  No response within 3s ({elapsed:.0f}s / {timeout}s)")  # (3)!

        time.sleep(interval)


if __name__ == "__main__":
    url = "http://api.internal/health"

    if not wait_for_health(url, timeout=120, interval=5):
        print(f"✗ {url} did not recover within 120s")
        sys.exit(1)  # (4)!
```

1. `timeout=3` is the per-request timeout — how long to wait for a single HTTP response. Separate from the outer `timeout=120` loop timeout.
2. Connection refused means the server isn't listening yet. Different from an HTTP error — the application hasn't started.
3. Server accepted the connection but didn't respond in time — usually means the app is starting but not ready.
4. `sys.exit(1)` signals failure to whatever called this script — your CI/CD pipeline, a Makefile, a parent script.

---

## Running It

```bash title="Running the health check"
python health_check.py
#   Connection refused (0s / 120s)
#   Connection refused (5s / 120s)
#   HTTP 503 (10s / 120s)
#   HTTP 503 (15s / 120s)
# ✓ http://api.internal/health is healthy (20s)
```

The output tells you exactly what the server was doing during the wait. In a CI log, that's useful information. "It spent 10 seconds failing to connect, then 10 seconds returning 503s before coming healthy" is a different story than "it came up immediately."

---

## Checking a JSON Field, Not Just Status Code

Your `/health` endpoint might return 200 with a body that indicates partial readiness:

```json
{"status": "degraded", "database": false, "cache": true}
```

A status-code-only check would pass this. Here's how to check the body:

```python title="Checking the response body" linenums="1"
resp = requests.get(url, timeout=3)
if resp.status_code == 200:
    data = resp.json()
    if data.get("status") == "healthy":
        return True
    else:
        print(f"  Status: {data.get('status')} ({elapsed:.0f}s)")
```

This is where Python genuinely beats a `curl` loop — parsing JSON inline without calling `jq` or juggling subshells.

---

## Making It Reusable Across a Deploy Script

A health check that lives in a function can be called from a larger deployment script:

```python title="Integrated into a deploy script" linenums="1"
from health_check import wait_for_health
import sys

def deploy():
    print("→ Applying manifests")
    # ... kubectl apply ...

    print("→ Waiting for rollout")
    # ... kubectl rollout status ...

    print("→ Verifying health")
    if not wait_for_health("http://api.internal/health", timeout=120):
        print("✗ Deploy failed — API did not become healthy")
        sys.exit(1)

    print("✓ Deploy complete")

deploy()
```

Bash functions exist but sharing logic across files and integrating cleanly with exit codes gets awkward. Python modules are designed for this.

---

## Practice Exercises

??? question "Exercise 1: Add exponential backoff"
    The current poller waits exactly 5 seconds between each attempt. Modify it so the interval doubles after each failed attempt, up to a maximum of 30 seconds. (This reduces load on a recovering service while still catching a fast recovery.)

    ??? tip "Answer"
        ```python title="Exponential backoff" linenums="1"
        interval = 5
        max_interval = 30

        while True:
            # ... attempt ...
            time.sleep(interval)
            interval = min(interval * 2, max_interval)
        ```

??? question "Exercise 2: Accept the URL as a command-line argument"
    Hardcoding the URL makes the script less reusable. Modify `health_check.py` so the URL is passed as the first argument: `python health_check.py http://api.internal/health`

    ??? tip "Answer"
        ```python title="URL from command line" linenums="1"
        import sys

        if len(sys.argv) < 2:
            print(f"Usage: {sys.argv[0]} <url>")
            sys.exit(1)

        url = sys.argv[1]
        ```
        For a full CLI with flags, the Efficiency section covers `argparse`.

---

## Quick Recap

| Concept | What It Does |
|:--------|:-------------|
| `requests.get(url, timeout=3)` | HTTP GET with per-request timeout |
| `ConnectionError` | Server isn't listening (process not started) |
| `Timeout` | Server accepted connection but didn't respond |
| `resp.status_code` | HTTP status (200, 503, etc.) |
| `resp.json()` | Parse response body as JSON |
| `sys.exit(1)` | Signal failure to calling process |

---

## What's Next

- **[What Just Broke?](parsing_logs.md)** — When the API came back but something still isn't right and you need to read the logs

## Further Reading

### Official Documentation
- [`requests` library](https://requests.readthedocs.io/) — The HTTP library used here
- [`time` module](https://docs.python.org/3/library/time.html) — `time.sleep()`, `time.time()`
- [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit) — Exit codes and pipeline integration
