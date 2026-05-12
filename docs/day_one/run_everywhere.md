---
title: "Run This Everywhere: Fleet Operations with Python"
description: "Loop over a server inventory in Python, run checks across your fleet, collect per-server results, and produce a clear pass/fail report — with proper failure handling."
---

# Run This Everywhere

!!! tip "Part of Day One"
    This is part of [Day One: Python for Platform Engineers](overview.md).

The deploy finished. You need to confirm the service is healthy on all 15 app servers before you call it done. Or you need to check disk space on every node in the cluster before the storage migration. Or you need to verify the new config file landed on every host.

In `bash`, the loop is easy. The problem is what happens when one server fails, or times out, or is unreachable — and you need to know which one.

---

## The Bash Loop and Its Gaps

```bash title="Bash: looping over servers"
for server in $(cat servers.txt); do
  ssh "$server" "systemctl is-active myapp"
done
```

This runs the command on each server. What it doesn't do well:

- Collecting which servers passed and which failed
- Handling SSH timeouts without hanging
- Producing a summary you can act on
- Exiting with a useful code for a pipeline

You end up grepping through interleaved stdout, or writing to temp files, or losing track of which output came from which host.

---

## The Python Version

```python title="fleet_check.py" linenums="1"
import subprocess
import sys


def check_server(server, command, ssh_timeout=5, cmd_timeout=10):
    """Run command on server via SSH. Returns (success, output, error)."""
    try:
        result = subprocess.run(
            ["ssh", "-o", f"ConnectTimeout={ssh_timeout}",
             "-o", "StrictHostKeyChecking=no",  # (1)!
             server] + command,
            capture_output=True,
            text=True,
            timeout=cmd_timeout,  # (2)!
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()

    except subprocess.TimeoutExpired:
        return False, "", "SSH timed out"


def check_fleet(servers, command):
    passed = []
    failed = []

    for server in servers:
        ok, output, error = check_server(server, command)
        status = "✓" if ok else "✗"
        print(f"  {status} {server}")
        if not ok:
            failed.append((server, error or output))
        else:
            passed.append(server)

    return passed, failed


if __name__ == "__main__":
    servers = [
        "app-01.prod.internal",
        "app-02.prod.internal",
        "app-03.prod.internal",
    ]

    command = ["systemctl", "is-active", "--quiet", "myapp"]

    print("Checking fleet...\n")
    passed, failed = check_fleet(servers, command)

    print(f"\n{'✓' if not failed else '✗'} {len(passed)}/{len(servers)} servers healthy")

    if failed:
        print("\nFailed servers:")
        for server, reason in failed:
            print(f"  {server}: {reason}")
        sys.exit(1)
```

1. `StrictHostKeyChecking=no` skips the "are you sure you want to connect?" prompt for new hosts. Necessary in automation; understand the security trade-off. For production tooling, use a known_hosts file instead.
2. `timeout=cmd_timeout` is the Python-level timeout on the `subprocess.run()` call — if SSH hangs entirely (not just slow to connect), this catches it.

```bash title="Running it"
python fleet_check.py
# Checking fleet...
#
#   ✓ app-01.prod.internal
#   ✓ app-02.prod.internal
#   ✗ app-03.prod.internal
#
# ✗ 2/3 servers healthy
#
# Failed servers:
#   app-03.prod.internal: SSH timed out
```

---

## Reading the Server List From a File

Hardcoding servers in the script is fine for one-off tasks. For anything you run regularly, keep the list in a file:

```text title="servers.txt"
app-01.prod.internal
app-02.prod.internal
app-03.prod.internal
```

```python title="Read server list from file" linenums="1"
with open("servers.txt") as f:
    servers = [
        line.strip()
        for line in f
        if line.strip() and not line.startswith("#")  # (1)!
    ]
```

1. Skip blank lines and lines starting with `#`. This lets you comment out servers temporarily in the inventory file without editing the script.

---

## Collecting Per-Server Output

Sometimes you need to collect the output from each server, not just pass/fail:

```python title="Collecting disk usage per server" linenums="1"
results = {}

for server in servers:
    ok, output, error = check_server(
        server,
        ["df", "-h", "--output=pcent", "/"]  # (1)!
    )
    if ok:
        # output is like "Use%\n 63%"
        lines = output.splitlines()
        percent = lines[-1].strip().rstrip("%")
        results[server] = int(percent)
    else:
        results[server] = None

print("Disk usage (root filesystem):\n")
for server, pct in sorted(results.items(), key=lambda x: x[1] or 0, reverse=True):
    if pct is None:
        print(f"  {server:35s} ERROR")
    elif pct >= 90:
        print(f"  {server:35s} {pct}%  ← CRITICAL")
    elif pct >= 80:
        print(f"  {server:35s} {pct}%  ← Warning")
    else:
        print(f"  {server:35s} {pct}%")
```

1. `df --output=pcent /` prints just the percentage used on the `root` filesystem. Keeps the output simple to parse.

Bash can produce this output. Python lets you sort it, flag the worst offenders, and format it clearly — without `awk` and `sort` pipelines.

---

## Adding Parallelism for Large Fleets

The sequential version waits for each server before moving to the next. For 15 servers that's fine. For 150, it's slow. Python's `concurrent.futures` runs checks in parallel without requiring you to manage threads yourself:

```python title="Parallel fleet check" linenums="1"
from concurrent.futures import ThreadPoolExecutor, as_completed

def check_server_task(server):
    ok, output, error = check_server(server, command)
    return server, ok, error or output

with ThreadPoolExecutor(max_workers=10) as executor:  # (1)!
    futures = {executor.submit(check_server_task, s): s for s in servers}

    for future in as_completed(futures):
        server, ok, info = future.result()
        print(f"  {'✓' if ok else '✗'} {server}")
```

1. `max_workers=10` runs up to 10 SSH connections simultaneously. Set this based on your network and the load you're comfortable putting on your servers. Don't set it to 500.

The `as_completed()` loop prints results as they arrive rather than waiting for all of them — so you see fast servers immediately instead of staring at a blank screen.

---

## Practice Exercises

??? question "Exercise 1: Add a dry-run flag"
    Modify the script to accept `--dry-run` as a command-line argument. In dry-run mode, print what it would do on each server without actually connecting.

    ??? tip "Answer"
        ```python title="Dry-run flag" linenums="1"
        import sys

        dry_run = "--dry-run" in sys.argv

        for server in servers:
            if dry_run:
                print(f"  [DRY RUN] Would run {command} on {server}")
            else:
                ok, output, error = check_server(server, command)
                # ...
        ```

??? question "Exercise 2: Write results to a file"
    Extend the script to write a timestamped summary to a file after running. Each line should be: `timestamp,server,status`.

    ??? tip "Answer"
        ```python title="Write results to CSV" linenums="1"
        import datetime

        timestamp = datetime.datetime.now().isoformat()
        with open("fleet_check_results.csv", "a") as f:
            for server in passed:
                f.write(f"{timestamp},{server},ok\n")
            for server, _ in failed:
                f.write(f"{timestamp},{server},failed\n")
        ```
        The `"a"` mode appends to the file rather than overwriting it, so successive runs build a history.

---

## Quick Recap

| Concept | What It Does |
|:--------|:-------------|
| `subprocess.run([...], capture_output=True)` | Run a command and capture stdout/stderr |
| `timeout=N` in `subprocess.run` | Kill the process if it hangs longer than N seconds |
| `result.returncode` | 0 = success, non-zero = failure |
| List comprehension with `if` | Filter blank lines from inventory file |
| `ThreadPoolExecutor` | Run checks in parallel |

---

## What's Next

- **[My Bash Script Is Getting Out of Hand](wrapping_bash.md)** — When you need to run a more complex sequence of shell commands per server, not just one

## Further Reading

### Official Documentation
- [`subprocess` module](https://docs.python.org/3/library/subprocess.html) — Full subprocess docs
- [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — Thread and process pool executors
- [OpenSSH client options](https://man.openbsd.org/ssh_config) — `ConnectTimeout`, `StrictHostKeyChecking`, and other SSH options

### Deep Dives
- [`fabric` library](https://www.fabfile.org/) — A higher-level library for SSH automation in Python, worth knowing once fleet operations become a regular part of your work
- [`paramiko`](https://www.paramiko.org/) — Direct SSH from Python without calling the `ssh` binary, useful when you need more control over the connection
