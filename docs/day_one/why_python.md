---
title: "Why Python, Not Just Bash: A Practical Decision Framework"
description: "A practical decision framework for platform engineers: when to stay in bash, when to switch to Python, and what the real differences look like in practice."
---

# Why Python (Not Just Bash)

!!! tip "Part of Day One"
    This is part of [Day One: Python for Platform Engineers](overview.md).

It's 2am. The alert fired. Your monitoring script logged 'Health check failed' and exited 1 — but you don't know if it was a connection refused, an HTTP 500, or a 30-second timeout. `bash` gave you one bit of information.

That's the flip-over point. Not an argument against `bash` — a decision framework for when the problem has outgrown what `bash` handles well.

---

## What Bash Is Good At

Bash was built for one job: running commands and piping their output together. It's exceptionally good at that job.

```bash title="Bash at its best" linenums="1"
kubectl get pods -o name | grep myapp | xargs kubectl delete
```

One line. Reads clearly. Does exactly what it says. Python would be six lines and harder to follow. Stay in `bash`.

Same for quick file operations, environment setup scripts, one-shot tasks you run manually. `bash` is the right tool.

---

## Where Bash Starts to Cost You

The trouble starts when your script needs to **do something with the data** instead of just passing it along.

### Counting and grouping

```bash title="Bash: counting errors from a log" linenums="1"
grep ERROR app.log | wc -l
```

That tells you how many. It doesn't tell you which component is producing them, whether the count is rising, or what the first one was. To get that in `bash`, you're writing `awk` or accumulating into associative arrays — and most people don't, so they squint at raw `grep` output instead.

### Handling failures per item

```bash title="Bash: looping over servers" linenums="1"
for server in $(cat servers.txt); do
  ssh "$server" "systemctl is-active myapp"
done
```

When one server fails, what happens? The loop continues. How do you collect which ones failed? You're `grep`ping stderr, or writing to temp files, or using subshell tricks. It works but it gets ugly.

### Parsing structured data

```bash title="Bash: parsing JSON" linenums="1"
curl -s http://api/status | jq '.services[] | select(.healthy == false) | .name'
```

`jq` is powerful but it's its own language. Nested conditions and multi-step transformations become hard to read and nearly impossible to test.

---

## The Flip-Over Point

Reach for Python when your `bash` script hits any of these:

| Signal | Why it matters |
|:-------|:---------------|
| More than 3 levels of nested `if` | Logic is hard to follow and harder to test |
| You've written `awk` more than twice | You're reinventing Python's string parsing |
| You need to collect results across a loop | `bash` has no real data structures |
| Someone else needs to maintain this | Python is easier to read six months later |
| You want to test it | You can't unit-test `bash` meaningfully |
| The output needs to be structured | Python makes JSON output trivial |

---

## The Real Difference in Practice

The difference isn't syntax. It's what happens when something goes wrong.

=== "Bash approach"

    ```bash title="Deploy check in bash" linenums="1"
    RESULT=$(curl -sf --retry 5 http://api.internal/health)
    if [ $? -ne 0 ]; then
      echo "Health check failed"
      exit 1
    fi
    ```

    What does "failed" mean here? Connection refused? HTTP 500? Timeout? `curl --retry` doesn't distinguish. You get a 0 or a non-zero, and that's it.

=== "Python approach"

    ```python title="Deploy check in Python" linenums="1"
    import requests

    try:
        resp = requests.get("http://api.internal/health", timeout=5)
        resp.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("✗ Server not reachable")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"✗ Server returned {e.response.status_code}")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("✗ Server did not respond within 5s")
        sys.exit(1)
    ```

    You know exactly what failed. You can handle each case differently. You can log it, retry selectively, or notify on specific error types.

The `bash` version is faster to write. The Python version is faster to debug at 2am.

---

## The Practical Rule

**Write it in `bash` first.** If you finish and it's under 20 lines with no nested loops or conditions, ship it as `bash`. It's the right tool.

If you find yourself:

- Writing functions to compensate for missing data structures
- Parsing `awk` output with more `awk`
- Commenting every third line because it's not obvious what it does
- Avoiding tests because "it's just a `bash` script"

...rewrite it in Python. You'll spend an hour on the rewrite and save days over the life of the script.

---

## Quick Recap

| Situation | Stay in `bash` | Switch to Python |
|:----------|:--------------|:-----------------|
| Running commands, piping output | ✓ | |
| One-liners and quick operations | ✓ | |
| Counting, grouping, summarizing results | | ✓ |
| Handling failures per item in a loop | | ✓ |
| Parsing structured JSON or YAML | | ✓ |
| Script needs to be testable | | ✓ |
| Someone else needs to maintain it | | ✓ |

---

## Practice Exercises

??? question "Exercise 1: Identify the flip-over point"
    Should this script stay in `bash` or be rewritten in Python? Explain your reasoning.

    ```bash title="deploy_check.sh" linenums="1"
    #!/bin/bash
    SERVICES=("api" "worker" "scheduler")
    FAILED=()

    for svc in "${SERVICES[@]}"; do
        if ! kubectl rollout status deployment/$svc -n production --timeout=30s 2>/dev/null; then
            FAILED+=("$svc")
        fi
    done

    if [ ${#FAILED[@]} -gt 0 ]; then
        echo "Failed: ${FAILED[*]}"
        exit 1
    fi
    echo "All services healthy"
    ```

    ??? tip "Answer"
        This is a good candidate for rewrite. Signs:

        - **Collecting results across a loop** — works in `bash` but gets harder to extend as requirements grow
        - **No per-service failure details** — you know something failed but not why or what the rollout output said
        - **Can't easily add features** — retry logic, per-service timeouts, or Slack notification would require significantly more `bash`

        The `bash` version is functional for its current scope. The Python version would be easier to extend and test.

??? question "Exercise 2: Decide for a one-liner"
    This one-liner counts pods that aren't Running. Rewrite it in Python. Then decide: was the rewrite worth it?

    ```bash title="count not-running pods" linenums="1"
    kubectl get pods -n production -o json \
      | jq '[.items[] | select(.status.phase != "Running")] | length'
    ```

    ??? tip "Answer"
        ```python title="equivalent Python" linenums="1"
        import subprocess
        import json

        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", "production", "-o", "json"],
            capture_output=True, text=True
        )
        pods = json.loads(result.stdout)
        not_running = [p for p in pods["items"] if p["status"]["phase"] != "Running"]
        print(len(not_running))
        ```

        **Was the rewrite worth it?** Probably not for just the count. The `bash` version is shorter and clearer. Python wins when you also need the pod names, restart counts, or per-pod status — `jq` gets unwieldy for multi-field output.

---

## Further Reading

### Official Documentation
- [`subprocess` module](https://docs.python.org/3/library/subprocess.html) — Running shell commands from Python
- [`requests` library](https://requests.readthedocs.io/) — HTTP in Python, used in the health check example

### Perspective
- [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) — When Google uses shell scripts and when they don't; the same decision framework applied at scale

---

## What's Next

The rest of Day One is all specific scenarios where Python is the right call. Start with the one you're facing today:

- **[Is It Still Up?](health_check.md)** — Health checking during a redeploy
- **[What Just Broke?](parsing_logs.md)** — Parsing logs to understand failures
- **[Did the Config Change?](comparing_configs.md)** — Config comparison after a deploy
- **[Run This Everywhere](run_everywhere.md)** — Fleet-wide checks
- **[My Bash Script Is Getting Out of Hand](wrapping_bash.md)** — Migrating an unwieldy `bash` script
