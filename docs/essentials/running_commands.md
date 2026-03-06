---
title: "Running System Commands from Python"
description: "Replace your shell pipelines with subprocess.run(). Capture output, handle errors, set timeouts, and avoid the shell injection trap."
---

# Running Commands from Python: subprocess for Sysadmins

In Bash, calling external programs is the whole point. You pipe `kubectl` into `grep` into `awk`,
chain commands with `&&`, redirect output to files, and check `$?` to see if anything failed.
Your scripts are fundamentally command orchestrators.

Python can do all of this — with the `subprocess` module. But the API looks different from Bash
because Python treats shell commands as **a deliberate choice**, not the default. That design
decision prevents a whole class of security bugs (more on that later).

This article covers everything you need to replace your shell pipelines with Python.

---

## Coming from Bash

In Bash, you run commands like this:

```bash title="Bash: Running Commands" linenums="1"
# Run a command
systemctl status nginx

# Run and capture output
STATUS=$(systemctl is-active nginx)

# Run and check exit code
kubectl apply -f deploy.yaml && echo "OK" || echo "FAILED"

# Pipe output to another command
kubectl get pods | grep Running | wc -l
```

In Python, the same operations look like:

```python title="Python: subprocess.run()" linenums="1"
import subprocess

# Run a command
subprocess.run(["systemctl", "status", "nginx"])

# Run and capture output
result = subprocess.run(["systemctl", "is-active", "nginx"],
                        capture_output=True, text=True)
status = result.stdout.strip()  # (1)!

# Run and check exit code (raises on failure)
subprocess.run(["kubectl", "apply", "-f", "deploy.yaml"], check=True)

# Capture output to process in Python
result = subprocess.run(["kubectl", "get", "pods"],
                        capture_output=True, text=True, check=True)
running = sum(1 for line in result.stdout.splitlines() if "Running" in line)
```

1. `.strip()` removes the trailing newline that commands typically add — same as `echo -n` in Bash

The key differences from Bash:
- Commands are **lists of strings**, not a single string (no word-splitting bugs)
- Output capture is **explicit** (`capture_output=True`) — by default, output goes to the terminal
- Error checking is **explicit** (`check=True`) — by default, failed commands are silently ignored

---

## subprocess.run(): The Modern API

`subprocess.run()` is the function you want for almost everything. It was introduced in Python 3.5
to replace the older `subprocess.call()`, `subprocess.check_call()`, and `subprocess.check_output()`
functions. If you see older code using those, they still work but `subprocess.run()` is cleaner.

### Basic Usage

```python title="subprocess.run() Basics" linenums="1"
import subprocess

# Run a command, output goes to terminal
result = subprocess.run(["ls", "-la", "/var/log"])

# Check what came back
print(result.returncode)  # 0 = success
```

### Capturing Output

```python title="Capturing stdout and stderr" linenums="1"
import subprocess

result = subprocess.run(
    ["df", "-h", "/"],
    capture_output=True,  # (1)!
    text=True,            # (2)!
)

print("stdout:", result.stdout)
print("stderr:", result.stderr)
print("return code:", result.returncode)
```

1. `capture_output=True` is shorthand for `stdout=subprocess.PIPE, stderr=subprocess.PIPE`
2. `text=True` decodes bytes to strings using the system encoding — without it, you get `bytes`

### Checking for Errors

```python title="Handling Command Failures" linenums="1"
import subprocess

# Option 1: check=True raises CalledProcessError on non-zero exit
try:
    result = subprocess.run(
        ["kubectl", "apply", "-f", "deploy.yaml"],
        capture_output=True,
        text=True,
        check=True,  # (1)!
    )
    print("Deployed successfully")
except subprocess.CalledProcessError as e:
    print(f"Deploy failed (exit code {e.returncode})")
    print(f"Error output: {e.stderr}")

# Option 2: check returncode manually
result = subprocess.run(["systemctl", "is-active", "nginx"],
                        capture_output=True, text=True)
if result.returncode == 0:
    print("nginx is running")
else:
    print("nginx is not running")
```

1. `check=True` is the equivalent of Bash's `set -e` — it makes failures loud

---

## Real-World Examples

### Checking Service Status

```python title="Check Service Status" linenums="1"
import subprocess

def is_service_running(service: str) -> bool:
    """Check if a systemd service is active."""
    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True,
    )
    return result.stdout.strip() == "active"

def restart_service(service: str) -> None:
    """Restart a systemd service, raising on failure."""
    subprocess.run(
        ["systemctl", "restart", service],
        check=True,
    )

# Usage
if not is_service_running("nginx"):
    print("nginx is down, restarting...")
    restart_service("nginx")
```

### Running git Commands

```python title="Git Operations" linenums="1"
import subprocess
from pathlib import Path

def get_current_branch(repo_path: Path) -> str:
    """Get the current git branch name."""
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
        cwd=repo_path,  # (1)!
    )
    return result.stdout.strip()

def get_uncommitted_changes(repo_path: Path) -> list[str]:
    """Return list of modified files."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True,
        cwd=repo_path,
    )
    return [line[3:] for line in result.stdout.splitlines() if line]

repo = Path("/home/deploy/myapp")
branch = get_current_branch(repo)
changes = get_uncommitted_changes(repo)
print(f"Branch: {branch}, Uncommitted files: {len(changes)}")
```

1. `cwd=` sets the working directory for the command — equivalent to `cd /path && git ...` in Bash

### Calling kubectl

```python title="kubectl Wrapper" linenums="1"
import subprocess
import json

def kubectl(args: list[str], namespace: str = "default") -> str:
    """Run a kubectl command and return stdout."""
    result = subprocess.run(
        ["kubectl", "-n", namespace] + args,
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout

def get_pods(namespace: str = "default") -> list[dict]:
    """Get all pods as a list of dicts."""
    output = kubectl(["get", "pods", "-o", "json"], namespace=namespace)
    return json.loads(output)["items"]  # (1)!

def get_running_pods(namespace: str = "default") -> list[str]:
    """Return names of running pods."""
    pods = get_pods(namespace)
    return [
        p["metadata"]["name"]
        for p in pods
        if p["status"]["phase"] == "Running"
    ]

running = get_running_pods("production")
print(f"Running pods: {', '.join(running)}")
```

1. `kubectl get pods -o json` outputs structured data; `json.loads()` turns it into a Python dict — no `jq` required

---

## Replacing Bash Pipelines

The Bash pipeline (`cmd1 | cmd2 | cmd3`) is powerful but awkward to replicate in Python.
The good news: most of the time, **you don't need to**. Instead of piping between tools, you
capture the output of the first command and process it in Python.

```bash title="Bash: Pipeline" linenums="1"
# Find large log files
find /var/log -name "*.log" -size +100M | xargs ls -lh | sort -k5 -rh
```

```python title="Python: No Pipeline Needed" linenums="1"
from pathlib import Path

# Find large log files (over 100MB) and sort by size
large_logs = sorted(
    [f for f in Path("/var/log").rglob("*.log")  # (1)!
     if f.stat().st_size > 100 * 1024 * 1024],  # (2)!
    key=lambda f: f.stat().st_size,
    reverse=True,
)

for log in large_logs:
    size_mb = log.stat().st_size / (1024 * 1024)
    print(f"{log}: {size_mb:.0f}MB")
```

1. `rglob("*.log")` is recursive glob — replaces `find -name "*.log"`
2. `st_size` is bytes — `100 * 1024 * 1024` is 100 MB

When you really do need to pipe between two processes:

```python title="Subprocess Pipeline" linenums="1"
import subprocess

# Two-process pipeline: ps | grep python
ps = subprocess.run(["ps", "aux"], capture_output=True, text=True)
python_procs = [line for line in ps.stdout.splitlines() if "python" in line]
print("\n".join(python_procs))

# True pipe between processes (when you can't buffer the output)
ps_proc = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)
grep_proc = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_proc.stdout,
    stdout=subprocess.PIPE,
    text=True,
)
ps_proc.stdout.close()  # (1)!
output, _ = grep_proc.communicate()
print(output)
```

1. Close the parent's copy of the pipe so the child receives EOF when the first process exits — this is the correct way to chain processes

---

## Security: Why `shell=True` Is Dangerous

`subprocess.run()` accepts a `shell=True` argument that lets you pass a command as a single
string, like Bash:

```python title="shell=True — DON'T DO THIS with user input" linenums="1"
import subprocess

# DANGEROUS if filename comes from user input
filename = input("Enter log file name: ")
subprocess.run(f"cat {filename}", shell=True)  # (1)!
```

1. If the user enters `access.log; rm -rf /`, your script will run that too — classic command injection

The safe version:

```python title="Safe: Command as List" linenums="1"
import subprocess

filename = input("Enter log file name: ")
subprocess.run(["cat", filename])  # (2)!
```

2. Passing a list means `filename` is treated as data, not code — no injection possible

**Rules:**
- If the command **never contains user input**, `shell=True` is acceptable (though still not recommended)
- If the command contains **any user-supplied data** — filename, username, search term — never use `shell=True`
- When in doubt, use a list

---

## Handling Timeouts

Long-running commands can hang your script indefinitely. Add a timeout:

```python title="Timeouts" linenums="1"
import subprocess

try:
    result = subprocess.run(
        ["aws", "s3", "sync", "s3://mybucket", "/backup"],
        capture_output=True,
        text=True,
        check=True,
        timeout=300,  # (1)!
    )
except subprocess.TimeoutExpired:
    print("Backup timed out after 5 minutes")
except subprocess.CalledProcessError as e:
    print(f"Backup failed: {e.stderr}")
```

1. Timeout is in seconds — the process is killed after 300 seconds (5 minutes)

---

## Practice Problems

??? question "Practice Problem 1: Service Health Check"

    Write a function `check_services(services: list[str]) -> dict[str, bool]` that
    checks whether each service in the list is active, returning a dict mapping
    service name to True/False.

    ??? tip "Answer"

        ```python title="Service Health Check" linenums="1"
        import subprocess

        def check_services(services: list[str]) -> dict[str, bool]:
            results = {}
            for service in services:
                result = subprocess.run(
                    ["systemctl", "is-active", service],
                    capture_output=True,
                    text=True,
                )
                results[service] = result.stdout.strip() == "active"
            return results

        status = check_services(["nginx", "postgresql", "redis"])
        for service, active in status.items():
            state = "UP" if active else "DOWN"
            print(f"{service}: {state}")
        ```

??? question "Practice Problem 2: Git Log Summary"

    Write a function that returns the last N commit messages from a git repository.
    Use `git log --oneline -N`.

    ??? tip "Answer"

        ```python title="Git Log Summary" linenums="1"
        import subprocess
        from pathlib import Path

        def recent_commits(repo: Path, n: int = 10) -> list[str]:
            result = subprocess.run(
                ["git", "log", f"--oneline", f"-{n}"],
                capture_output=True,
                text=True,
                check=True,
                cwd=repo,
            )
            return result.stdout.strip().splitlines()

        commits = recent_commits(Path("/home/deploy/myapp"), n=5)
        for commit in commits:
            print(commit)
        ```

??? question "Practice Problem 3: Explain the Security Risk"

    What's wrong with this code, and how would you fix it?

    ```python
    import subprocess

    username = input("Username to check: ")
    subprocess.run(f"grep {username} /etc/passwd", shell=True)
    ```

    ??? tip "Answer"

        The `shell=True` combined with unsanitized user input is a command injection
        vulnerability. If the user enters `root; cat /etc/shadow`, the shell will
        execute both `grep root /etc/passwd` AND `cat /etc/shadow`.

        **Fix**: Use a list and pass the username as a separate argument:

        ```python title="Safe grep" linenums="1"
        import subprocess

        username = input("Username to check: ")
        subprocess.run(["grep", username, "/etc/passwd"])
        ```

        Now `username` is passed as data to `grep`, not interpreted by the shell.
        Even if someone enters `root; rm -rf /`, grep just looks for that exact string.

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`subprocess.run()`** | The modern API for running external commands |
| **Command as list** | `["cmd", "arg1", "arg2"]` — prevents shell injection, no word-splitting |
| **`capture_output=True`** | Captures both stdout and stderr; access via `result.stdout` / `result.stderr` |
| **`text=True`** | Decodes output to strings; without it you get `bytes` |
| **`check=True`** | Raises `CalledProcessError` on non-zero exit code |
| **`cwd=`** | Set working directory for the command |
| **`timeout=`** | Kill the process after N seconds |
| **`shell=True`** | Dangerous with user input — avoid unless you understand the risk |
| **No pipeline needed** | Capture output and process in Python instead of piping to `awk`/`grep` |

## Further Reading

### On This Site

- [Error Handling](error_handling.md) — catching `CalledProcessError` and other exceptions
- [File and Directory Operations](../efficiency/files_and_directories.md) — `pathlib` for file operations that complement subprocess

### Official Documentation

- [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html)
- [Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations) — the official guidance on `shell=True`
- [Replacing Shell Pipeline](https://docs.python.org/3/library/subprocess.html#replacing-shell-pipeline) — official Bash → Python migration patterns

### External Resources

- [Real Python: subprocess](https://realpython.com/python-subprocess/) — comprehensive tutorial with examples

`subprocess` is the bridge between Python and the rest of your infrastructure. Once you're
comfortable with it, you'll find yourself writing deployment scripts, health checks, and
automation tools that are genuinely more maintainable than their Bash equivalents — proper
error handling, structured logging, testable functions, and no shell injection risks.
