---
date: "2026-07-28 14:00"
title: "Is This Whole Stack Healthy? Checking Services in Parallel"
description: "Check dozens of services at once with ThreadPoolExecutor, why Python's GIL blocks a CPU-bound speedup, and when to reach for multiprocessing instead."
---

# Is This Whole Stack Healthy?

!!! tip "Part of Efficiency"
    This is part of [Efficiency](../index.md#efficiency): professional Python patterns for working platform engineers.

[Is It Still Up?](../day_one/health_check.md) covered polling one service until it comes back healthy. A real deploy rarely touches one service: it's a stack of them, and "is this whole stack healthy" means running that same check against 40 URLs, not one.

Loop over the list and call `wait_for_health()` on each one in turn, and the total wait time is the *sum* of every service's response time. Forty services at roughly a second each is forty seconds, even though most of that time is each request just sitting on the network waiting for a reply, not doing anything that needs your CPU.

---

## The Sequential Version and Its Problem

```python title="Sequential health check across a stack" linenums="1"
import requests

SERVICES = [
    "http://auth.internal/health",
    "http://billing.internal/health",
    "http://orders.internal/health",
    "http://inventory.internal/health",
    "http://notifications.internal/health",
    # ... 35 more
]


def check_one(url):
    try:
        resp = requests.get(url, timeout=3)
        return url, resp.status_code == 200
    except requests.exceptions.RequestException:
        return url, False


results = {}
for url in SERVICES:  # (1)!
    name, healthy = check_one(url)
    results[name] = healthy

unhealthy = [url for url, ok in results.items() if not ok]
if unhealthy:
    print(f"✗ {len(unhealthy)} service(s) down: {unhealthy}")
else:
    print("✓ Whole stack is healthy")
```

1. Each iteration blocks until that request completes before the next one even starts. The CPU is idle almost the entire time, waiting on the network.

That idle time is the tell. This is an **I/O-bound** problem (the bottleneck is waiting on other machines to respond, not computing anything), and I/O-bound problems are exactly what threads are good at.

---

## Checking Them All at Once with Threads

`concurrent.futures.ThreadPoolExecutor` runs multiple calls to `check_one()` on separate threads, so the waiting overlaps instead of stacking up:

```python title="Concurrent health check with ThreadPoolExecutor" linenums="1"
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

SERVICES = [
    "http://auth.internal/health",
    "http://billing.internal/health",
    "http://orders.internal/health",
    # ... 37 more
]


def check_one(url):
    try:
        resp = requests.get(url, timeout=3)
        return url, resp.status_code == 200
    except requests.exceptions.RequestException:
        return url, False


results = {}
with ThreadPoolExecutor(max_workers=20) as pool:  # (1)!
    futures = {pool.submit(check_one, url): url for url in SERVICES}
    for future in as_completed(futures):  # (2)!
        name, healthy = future.result()
        results[name] = healthy

unhealthy = [url for url, ok in results.items() if not ok]
if unhealthy:
    print(f"✗ {len(unhealthy)} service(s) down: {unhealthy}")
else:
    print("✓ Whole stack is healthy")
```

1. `max_workers=20` caps how many requests are in flight at once: unbounded concurrency against 40 internal services is its own way to cause an incident.
2. `as_completed()` yields each result as soon as it finishes, not in submission order: the fastest service reports first instead of waiting behind whichever URL happened to be listed earlier.

Forty services that each take about a second now finish in roughly a second, not forty. The wall-clock time collapses to whichever single request took longest, plus a small amount of thread-management overhead.

### Why This Actually Works: the GIL Steps Aside for I/O

Python's Global Interpreter Lock (GIL), covered in depth in **[Processes and Threads (cs.bradpenney.io)](https://cs.bradpenney.io/efficiency/systems/processes_and_threads/)**, normally means only one thread in a process executes Python bytecode at a time. That sounds like it should rule out any benefit from threading at all. It doesn't, for one specific reason: a thread that's blocked waiting on network I/O releases the GIL while it waits.

`requests.get()` spends nearly all of its time inside that blocked, GIL-released state: the socket is waiting on a reply, not running Python. That's the window every other thread in the pool uses to make progress. Twenty threads can all be legitimately blocked on twenty different sockets at once; the GIL only matters for the brief moments a thread is actually executing Python bytecode, and for an I/O-bound function like this one, that's a small fraction of its total runtime.

---

## What Threads Don't Fix: CPU-Bound Work

Health checks aren't the only thing you'd run against a stack. Say each service also returns its live config, and you want to catch drift by comparing it against a known-good baseline, the same comparison **[Did the Config Change?](../day_one/comparing_configs.md)** covers for a single service, now run across all forty:

```python title="Fetching and diffing configs across the stack" linenums="1"
import requests
from concurrent.futures import ThreadPoolExecutor


def find_differences(expected, actual, path=""):  # (1)!
    """Same function as Day One's comparing_configs.md — reused here unchanged."""
    differences = []
    all_keys = set(expected) | set(actual)
    for key in sorted(all_keys):
        location = f"{path}.{key}" if path else key
        if key not in actual:
            differences.append(f"MISSING:    {location}  (expected: {expected[key]!r})")
        elif key not in expected:
            differences.append(f"UNEXPECTED: {location}  (got: {actual[key]!r})")
        elif isinstance(expected[key], dict) and isinstance(actual[key], dict):
            differences.extend(find_differences(expected[key], actual[key], location))
        elif expected[key] != actual[key]:
            differences.append(f"CHANGED: {location}")
    return differences


def fetch_live_config(url):
    return requests.get(url, timeout=3).json()


def check_drift(url, expected):
    live = fetch_live_config(url)
    return url, find_differences(expected, live)


with ThreadPoolExecutor(max_workers=20) as pool:
    futures = {pool.submit(check_drift, url, EXPECTED_CONFIGS[url]): url for url in SERVICES}  # (2)!
    results = {f.result()[0]: f.result()[1] for f in futures}
```

1. Identical to the Day One version: no changes needed to make it work here. That's the payoff of writing it as a plain function in the first place.
2. `EXPECTED_CONFIGS` is assumed to be a dict mapping each URL to its own known-good baseline, loaded from the same source of truth the deploy pipeline uses.

Fetching each config is I/O-bound, so the threaded fan-out helps there exactly like it did for the health check. But `find_differences()` itself (walking two dicts, comparing keys and recursing into nested ones) is pure Python doing CPU work, not waiting on anything. For small, typical service configs (a few dozen keys), that work is trivial and none of this matters; sequential is fast enough. It starts to matter once the configs are large (a service with hundreds of feature flags, a deeply nested Helm-templated manifest), where the diff itself becomes real, measurable CPU time:

```text title="Representative timing, 4 large configs, 4 workers"
sequential:   ~2.0s
threaded:     ~2.1s   # no improvement — slightly worse, from thread-switching overhead
multiprocess: ~1.7s   # some real speedup, but muted (see below)
```

(Illustrative, not a guarantee: exact numbers depend on the machine, the configs, and how much of the work is genuinely CPU-bound.)

The threaded result is the GIL doing exactly what it's designed to do: only one thread executes Python bytecode at a time, full stop, and `find_differences()` never blocks on anything that would release it. Four threads computing four diffs run one at a time, taking turns, with the overhead of switching between them on top of the same total work, never meaningfully faster than just doing it sequentially, sometimes a little worse.

---

## Multiprocessing: Separate Processes, Separate GILs

`concurrent.futures.ProcessPoolExecutor` has almost the same interface as `ThreadPoolExecutor`, but each worker is a separate OS process with its own Python interpreter, and its own GIL. Four processes really do run four diffs on four different CPU cores at the same time:

```python title="Parallel config diffing with ProcessPoolExecutor" linenums="1"
from concurrent.futures import ProcessPoolExecutor

# find_differences() defined exactly as above


def check_drift(args):  # (1)!
    url, expected, live_config = args
    return url, find_differences(expected, live_config)


if __name__ == "__main__":  # (2)!
    # live_configs already fetched via the threaded step above
    work = [(url, EXPECTED_CONFIGS[url], live_configs[url]) for url in SERVICES]
    with ProcessPoolExecutor(max_workers=4) as pool:
        results = dict(pool.map(check_drift, work))
```

1. `check_drift` takes one argument because `pool.map()` sends one item per call: bundling `url`, `expected`, and `live_config` into a tuple avoids needing multiple parallel lists.
2. The `if __name__ == "__main__":` guard is required on the platforms that start worker processes by re-importing your script (Windows always; macOS and Linux depending on the multiprocessing start method). Without it, each new process re-runs the whole module and spawns its own set of workers.

The catch, visible in the ~1.7s above: it's real speedup over the ~2.0s baseline, but nowhere near the roughly 4x you'd hope for from four cores. Starting a process is far more expensive than starting a thread, and, unlike threads, which share memory for free, every argument and return value has to be serialized (`pickle`d) to cross between processes. Large configs and long lists of difference strings are exactly the kind of data that's expensive to pickle, and that cost eats directly into the parallelism gained. For forty small health-check responses, that overhead alone can cost more than the CPU work saves. Multiprocessing pays off in proportion to how heavy the computation is *relative to* how much data has to cross the process boundary to get there and back — the more of one and the less of the other, the better the payoff.

---

## Choosing Between Threads and Processes

| Situation | Use |
|:----------|:----|
| Waiting on network calls (HTTP requests, DB queries) | `ThreadPoolExecutor`: GIL releases during the wait |
| Heavy pure-Python computation (parsing, diffing, hashing large data in Python code) | `ProcessPoolExecutor`: sidesteps the GIL entirely |
| A mix of both (fetch, then compute) | Thread the fetch, process the compute, as shown above |
| Light computation on small inputs | Neither: process-startup and serialization overhead will cost more than sequential execution saves |

The fastest way to get this wrong is guessing. If a change to `max_workers` doesn't move the needle, the bottleneck probably isn't where you assumed: profile before reaching for a bigger pool.

---

## Practice Exercises

??? question "Exercise 1: Threads or processes?"
    You're writing a script that downloads 100 log files from S3, then greps each one for a specific error pattern. Which part benefits from `ThreadPoolExecutor`, which from `ProcessPoolExecutor`, and why?

    ??? tip "Answer"
        The download step is I/O-bound — each request spends its time waiting on S3 to respond, so `ThreadPoolExecutor` overlaps those waits and should be used there. Grepping the downloaded content is CPU-bound pure-Python work (assuming a manual string search, not a C-accelerated library call), so if that step is slow enough to matter, `ProcessPoolExecutor` is the one that actually parallelizes it. In practice: thread the downloads, then decide on the grep step based on whether it's actually the bottleneck, since for 100 small files it might not be worth the process overhead at all.

??? question "Exercise 2: Reading the timing pattern"
    You benchmark a function with `ThreadPoolExecutor` and it's about 5% *slower* than calling it sequentially, using 8 workers on an 8-core machine. What does that result tell you about the function?

    ??? tip "Answer"
        It's a strong signal the function is CPU-bound pure Python that doesn't release the GIL: if it did any meaningful blocking I/O, or called into a C extension that releases the GIL during its work (some `hashlib` and `numpy` operations do), threading would show a real speedup instead. The 5% slowdown is the cost of context-switching between threads that are all fighting over the same GIL, with none of them making any faster progress for it. That's the exact case `ProcessPoolExecutor` exists for.

---

## Quick Recap

| Concept | What It Does |
|:--------|:--------------|
| `ThreadPoolExecutor` | Runs calls on separate threads; helps when work is I/O-bound (the GIL releases during blocking waits) |
| `ProcessPoolExecutor` | Runs calls on separate OS processes, each with its own GIL; helps for CPU-bound pure-Python work |
| `as_completed()` | Yields results as they finish, not in submission order |
| `pool.map()` | Simplest fan-out when you don't need results in completion order |
| `if __name__ == "__main__":` | Required around code that starts a `ProcessPoolExecutor`, to avoid runaway re-imports |
| Process overhead | Startup cost + pickling arguments/results: only worth it when the per-item computation is heavy |

---

## What's Next

Efficiency builds the professional patterns (this one, `click` for real CLIs, proper logging) that turn working scripts into tools other people on your team can run. Mastery picks concurrency back up with `asyncio`, for the specific case of managing thousands of concurrent I/O waits without a thread per connection.

## Further Reading

### Official Documentation
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html): `ThreadPoolExecutor` and `ProcessPoolExecutor` reference
- [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html): the lower-level module `ProcessPoolExecutor` is built on
- [Python GIL design FAQ](https://docs.python.org/3/glossary.html#term-global-interpreter-lock): the official glossary definition, straight from the source

### Exploring Computer Science
- [Processes and Threads](https://cs.bradpenney.io/efficiency/systems/processes_and_threads/): the GIL, context switching, and the shared-memory trade-off this article's threading behavior comes from

### On This Site
- [Is It Still Up?](../day_one/health_check.md): the single-service poller this article extends to a whole stack
- [Did the Config Change?](../day_one/comparing_configs.md): the `find_differences()` diff logic used in the CPU-bound example
