---
title: "Why Python (Not Just Bash)"
description: "A practical decision framework for platform engineers: when to stay in bash, when to switch to Python, and what the real differences are in practice."
---

# Why Python (Not Just Bash)

!!! tip "Part of Day One"
    This is part of [Day One: Python for Platform Engineers](overview.md).

This isn't a "Python is better" argument. `bash` is excellent. You should keep writing `bash`. The question is: at what point does a problem outgrow what `bash` does comfortably?

That point is earlier than most people think.

---

## What Bash Is Good At

Bash was built for one job: running commands and piping their output together. It's exceptionally good at that job.

```bash title="Bash at its best"
kubectl get pods -o name | grep myapp | xargs kubectl delete
```

One line. Reads clearly. Does exactly what it says. Python would be six lines and harder to follow. Stay in `bash`.

Same for quick file operations, environment setup scripts, one-shot tasks you run manually. `bash` is the right tool.

---

## Where Bash Starts to Cost You

The trouble starts when your script needs to **do something with the data** instead of just passing it along.

### Counting and grouping

```bash title="Bash: counting errors from a log"
grep ERROR app.log | wc -l
```

That tells you how many. It doesn't tell you which component is producing them, whether the count is rising, or what the first one was. To get that in `bash`, you're writing `awk` or accumulating into associative arrays — and most people don't, so they squint at raw `grep` output instead.

### Handling failures per item

```bash title="Bash: looping over servers"
for server in $(cat servers.txt); do
  ssh "$server" "systemctl is-active myapp"
done
```

When one server fails, what happens? The loop continues. How do you collect which ones failed? You're `grep`ping stderr, or writing to temp files, or using subshell tricks. It works but it gets ugly.

### Parsing structured data

```bash title="Bash: parsing JSON"
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

    ```bash title="Deploy check in bash"
    RESULT=$(curl -sf --retry 5 http://api.internal/health)
    if [ $? -ne 0 ]; then
      echo "Health check failed"
      exit 1
    fi
    ```

    What does "failed" mean here? Connection refused? HTTP 500? Timeout? `curl --retry` doesn't distinguish. You get a 0 or a non-zero, and that's it.

=== "Python approach"

    ```python title="Deploy check in Python"
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

## What's Next

The rest of Day One is all specific scenarios where Python is the right call. Start with the one you're facing today:

- **[Is It Still Up?](health_check.md)** — Health checking during a redeploy
- **[What Just Broke?](parsing_logs.md)** — Parsing logs to understand failures
- **[Did the Config Change?](comparing_configs.md)** — Config comparison after a deploy
- **[Run This Everywhere](run_everywhere.md)** — Fleet-wide checks
- **[My Bash Script Is Getting Out of Hand](wrapping_bash.md)** — Migrating an unwieldy `bash` script
