---
title: Error Handling in Python
description: "Python's try/except — replacing Bash's $? and set -e with proper exception handling, finally for cleanup, and raising exceptions vs exit codes."
---

# Error Handling

In Bash, error handling is an afterthought. Scripts fail silently. `$?` tells you something went
wrong but not what. `set -e` makes scripts exit on error but gives you no way to recover. And
`trap` for cleanup is easy to get wrong.

Python treats errors as first-class objects. Every error has a type, a message, and a traceback.
You can catch specific errors, handle them differently, recover from some, and guarantee cleanup
runs regardless of what happened.

## Coming from Bash

```bash title="Bash Error Handling"
# Check exit code after every command
cp /etc/nginx/nginx.conf /backup/ || echo "Backup failed" >&2

# set -e: exit on any error (but misses errors in subshells and &&)
set -e

# trap for cleanup
cleanup() {
    rm -f /tmp/lockfile
}
trap cleanup EXIT

# Check if a command succeeded
if ! curl -f https://api.example.com/health; then
    echo "Health check failed" >&2
    exit 1
fi
```

```python title="Python Error Handling"
import shutil
from pathlib import Path

# Handle specific errors
try:
    shutil.copy2("/etc/nginx/nginx.conf", "/backup/")
except PermissionError as e:
    print(f"Backup failed: {e}", file=sys.stderr)
    raise SystemExit(1)

# finally: guaranteed cleanup (the Python trap)
lockfile = Path("/tmp/lockfile")
try:
    lockfile.touch()
    do_work()
finally:
    lockfile.unlink(missing_ok=True)  # Always runs

# Check with exception
import requests
try:
    response = requests.get("https://api.example.com/health")
    response.raise_for_status()  # Raises on 4xx/5xx
except requests.HTTPError as e:
    print(f"Health check failed: {e}", file=sys.stderr)
    raise SystemExit(1)
```

Key differences:

| Bash | Python |
|:-----|:-------|
| `$?` (numeric exit code) | Exception object with type and message |
| `cmd \|\| handle_error` | `try: ... except ExceptionType: ...` |
| `set -e` | No equivalent needed — exceptions propagate automatically |
| `trap cleanup EXIT` | `finally:` block |
| `exit 1` | `raise SystemExit(1)` or `sys.exit(1)` |
| Can't catch specific error types | `except FileNotFoundError`, `except PermissionError`, etc. |

## The try/except Block

The basic structure:

```python title="try/except Anatomy" linenums="1"
try:
    result = int(user_input)     # (1)!
except ValueError as e:          # (2)!
    print(f"Not a valid number: {e}")
    result = 0
```

1. Code that might raise an exception goes in the `try` block
2. `except` catches specific exception types — `as e` binds the exception object to a name

### Handling Multiple Exception Types

```python title="Multiple except Clauses" linenums="1"
from pathlib import Path

def read_config(path: str) -> str:
    try:
        return Path(path).read_text()
    except FileNotFoundError:           # (1)!
        print(f"Config not found: {path}")
        return ""
    except PermissionError as e:        # (2)!
        print(f"Cannot read config: {e}")
        raise                           # (3)!
```

1. Catch `FileNotFoundError` specifically — handle missing files gracefully
2. Catch `PermissionError` separately — different cause, different response
3. `raise` without arguments re-raises the current exception — lets it propagate up

### Catching Multiple Types Together

```python title="Catching Multiple Types" linenums="1"
try:
    result = risky_operation()
except (ValueError, TypeError) as e:    # (1)!
    print(f"Input error: {e}")
```

1. Tuple of exception types — catches either

## The else and finally Clauses

The full `try` block can include four parts:

```python title="Full try/except/else/finally" linenums="1"
import subprocess

try:
    result = subprocess.run(                        # (1)!
        ["systemctl", "is-active", "nginx"],
        capture_output=True, text=True, check=True
    )
except subprocess.CalledProcessError as e:
    print(f"nginx is not active: {e.stderr}")
else:
    print(f"nginx status: {result.stdout.strip()}")  # (2)!
finally:
    print("Check complete.")                         # (3)!
```

1. `try` — the code that might fail
2. `else` — runs only if no exception was raised (service is active)
3. `finally` — runs unconditionally — perfect for cleanup

### finally for Guaranteed Cleanup

`finally` is the Python equivalent of Bash's `trap ... EXIT`. Use it to release resources
regardless of what happened:

```python title="finally for Cleanup" linenums="1"
from pathlib import Path
import fcntl

lockfile = Path("/var/run/myapp.lock")

try:
    fd = open(lockfile, "w")
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)  # Acquire lock
    do_work()
except BlockingIOError:
    print("Another instance is running.")
    raise SystemExit(1)
finally:
    fd.close()
    lockfile.unlink(missing_ok=True)    # (1)!
```

1. This runs even if `do_work()` raises an exception — lock is always released

## Common Exception Types

Python's built-in exceptions cover the scenarios sysadmin scripts hit constantly:

| Exception | When it's raised |
|:----------|:----------------|
| `FileNotFoundError` | File or directory doesn't exist |
| `PermissionError` | Insufficient permissions to read/write |
| `IsADirectoryError` | Expected a file, got a directory |
| `OSError` | General OS-level error (parent of the above) |
| `ValueError` | Wrong type or value (e.g., `int("abc")`) |
| `KeyError` | Dictionary key doesn't exist |
| `IndexError` | List index out of range |
| `AttributeError` | Object doesn't have the attribute |
| `ImportError` | Module not found |
| `subprocess.CalledProcessError` | Subprocess exited with non-zero code |
| `requests.HTTPError` | HTTP 4xx or 5xx response (if using `requests`) |
| `json.JSONDecodeError` | Invalid JSON |
| `TimeoutError` | Operation timed out |

```python title="Catching OSError and Subclasses" linenums="1"
import os
from pathlib import Path

try:
    Path("/root/secret").read_text()
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("No permission to read")
except OSError as e:            # (1)!
    print(f"OS error: {e}")
```

1. `OSError` catches any remaining OS-level errors — `FileNotFoundError` and `PermissionError`
   are subclasses of `OSError`, so they're caught by their specific handlers first

## Raising Exceptions

### raise: Signaling Errors

When your code detects an invalid state, raise an exception instead of returning a sentinel value:

```python title="Raising Exceptions" linenums="1"
def deploy(environment: str):
    valid_envs = {"dev", "staging", "prod"}
    if environment not in valid_envs:
        raise ValueError(                           # (1)!
            f"Invalid environment: {environment!r}. "
            f"Must be one of {valid_envs}"
        )
    # Continue with deployment...
```

1. Raise `ValueError` for invalid input — caller can catch it or let it propagate

### sys.exit() vs raise SystemExit

For scripts that need to exit with a specific code (like Bash's `exit 1`):

```python title="Exiting Scripts" linenums="1"
import sys

# Standard: sys.exit() with an exit code
sys.exit(0)    # Success
sys.exit(1)    # General error

# Or raise SystemExit directly (same thing)
raise SystemExit(1)

# Exit with a message (prints to stderr, exits with code 1)
sys.exit("Error: config file not found")  # (1)!
```

1. Passing a string to `sys.exit()` prints it to stderr and exits with code 1

## Context Managers: The Pythonic finally

Context managers (`with` statements) are a cleaner way to handle the open/use/close pattern.
They replace `try/finally` for resource management:

```python title="Context Manager vs try/finally" linenums="1"
# Without context manager (verbose)
f = open("/etc/hosts")
try:
    content = f.read()
finally:
    f.close()

# With context manager (preferred)
with open("/etc/hosts") as f:           # (1)!
    content = f.read()
# File is automatically closed here
```

1. `with` calls `__enter__` on open and `__exit__` (which closes the file) when the block exits —
   even if an exception is raised

### Multiple Context Managers

```python title="Multiple Context Managers" linenums="1"
with open("/var/log/input.log") as infile, \
     open("/var/log/errors.log", "w") as outfile:    # (1)!
    for line in infile:
        if "ERROR" in line:
            outfile.write(line)
```

1. Multiple resources in one `with` statement — both are closed when the block exits

## Practical Patterns

### Fail Fast with Clear Messages

```python title="Input Validation with Exceptions" linenums="1"
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: script.py <config-file>")

    config_path = Path(sys.argv[1])

    if not config_path.exists():
        sys.exit(f"Error: config file not found: {config_path}")

    if not config_path.is_file():
        sys.exit(f"Error: {config_path} is not a file")

    # Safe to proceed
    content = config_path.read_text()
```

### Retry Logic

```python title="Retry with Exception Handling" linenums="1"
import time
import requests

def fetch_with_retry(url: str, max_attempts: int = 3) -> dict:
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.ConnectionError, requests.Timeout) as e:
            if attempt == max_attempts:
                raise                   # (1)!
            print(f"Attempt {attempt} failed: {e}. Retrying...")
            time.sleep(2 ** attempt)    # (2)!
```

1. Re-raise on final attempt — let the caller handle the permanent failure
2. Exponential backoff: 2s, 4s, 8s — standard retry pattern

### Catching and Re-raising with Context

```python title="Exception Chaining" linenums="1"
from pathlib import Path

def load_server_list(path: str) -> list:
    try:
        return Path(path).read_text().splitlines()
    except FileNotFoundError as e:
        raise RuntimeError(f"Cannot load server list from {path}") from e  # (1)!
```

1. `from e` chains exceptions — the traceback shows both the original `FileNotFoundError` and the
   `RuntimeError`, making debugging much easier

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`try/except`** | Wrap risky code; catch specific exception types |
| **`except Type as e`** | Bind the exception object to `e` for its message and details |
| **`else`** | Runs only if no exception was raised in `try` |
| **`finally`** | Runs unconditionally — use for cleanup (the Python `trap EXIT`) |
| **`raise`** | Signal an error; re-raise with `raise` (no args) to propagate |
| **`sys.exit()`** | Exit with a code — Bash's `exit N` |
| **Context managers** | `with` — cleaner than `try/finally` for resource management |
| **Exception hierarchy** | `FileNotFoundError` ⊂ `OSError` — catch specific first, general last |

## Practice Problems

??? question "Practice Problem 1: Safe File Read"

    Write a function `read_config(path)` that reads a file and returns its contents. If the
    file doesn't exist, return an empty string. If there's a permission error, print a message
    to stderr and re-raise.

    ??? tip "Answer"

        ```python title="Safe File Read" linenums="1"
        import sys
        from pathlib import Path

        def read_config(path: str) -> str:
            try:
                return Path(path).read_text()
            except FileNotFoundError:
                return ""                           # (1)!
            except PermissionError as e:
                print(f"Cannot read {path}: {e}", file=sys.stderr)
                raise                               # (2)!
        ```

        1. Missing file is recoverable — return empty string
        2. Permission denied is not — log it and let it propagate

??? question "Practice Problem 2: try/finally Cleanup"

    What does `finally` guarantee? Trace through this code and explain what gets printed
    when `do_work()` raises a `RuntimeError`.

    ```python
    def do_work():
        raise RuntimeError("Something went wrong")

    try:
        print("Starting")
        do_work()
        print("Finished")
    except ValueError:
        print("Value error caught")
    finally:
        print("Cleaning up")
    ```

    ??? tip "Answer"

        ```text
        Starting
        Cleaning up
        RuntimeError: Something went wrong
        ```

        - `"Starting"` prints — code reaches `do_work()`
        - `"Finished"` does NOT print — exception skips the rest of `try`
        - `except ValueError` does NOT run — wrong exception type
        - `"Cleaning up"` ALWAYS prints — `finally` runs regardless
        - Then the unhandled `RuntimeError` propagates and the script exits

??? question "Practice Problem 3: Exit Codes"

    Write a script that takes a filename argument, checks that it exists, and exits with
    code `1` and a useful message if it doesn't. On success, print the number of lines.

    ??? tip "Answer"

        ```python title="Script with Exit Codes" linenums="1"
        import sys
        from pathlib import Path

        if len(sys.argv) != 2:
            sys.exit(f"Usage: {sys.argv[0]} <filename>")

        path = Path(sys.argv[1])

        try:
            lines = path.read_text().splitlines()
            print(f"{len(lines)} lines in {path}")
        except FileNotFoundError:
            sys.exit(f"Error: file not found: {path}")
        except PermissionError:
            sys.exit(f"Error: permission denied: {path}")
        ```

??? question "Practice Problem 4: Which Exception?"

    Match each scenario to the correct exception type to catch:

    1. Parsing `"abc"` as an integer
    2. Opening `/root/private.key` without root
    3. Accessing `my_dict["missing_key"]`
    4. Calling `requests.get()` and getting a 404 response
    5. Reading `/tmp/nonexistent.txt`

    ??? tip "Answer"

        1. `ValueError` — `int("abc")` raises `ValueError: invalid literal`
        2. `PermissionError` — subclass of `OSError`
        3. `KeyError` — use `.get()` or catch `KeyError`
        4. `requests.HTTPError` — after calling `response.raise_for_status()`
        5. `FileNotFoundError` — subclass of `OSError`

## Further Reading

### On This Site

- [Running System Commands](running_commands.md) — `subprocess.CalledProcessError` and handling command failures
- [File and Directory Operations](../efficiency/files_and_directories.md) — `FileNotFoundError`, `PermissionError` in practice

### Official Documentation

- [**Built-in Exceptions**](https://docs.python.org/3/library/exceptions.html) — complete exception hierarchy
- [**Errors and Exceptions Tutorial**](https://docs.python.org/3/tutorial/errors.html) — official tutorial
- [**contextlib — Context Manager Utilities**](https://docs.python.org/3/library/contextlib.html) — writing your own context managers

---

Proper error handling is what separates a script from a tool. Bash scripts fail silently or
hard-exit with no useful context. Python lets you catch the specific thing that went wrong, take
targeted action, and guarantee cleanup. Start with specific exception types, use `finally` for
anything that must run regardless, and exit with `sys.exit()` when the error is terminal.
