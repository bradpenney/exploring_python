---
title: "Python vs Bash: When to Graduate"
description: "You've hit the ceiling of Bash. Here's exactly when Python wins, when Bash still wins, and how to run your first real Python script today."
---

# Python vs Bash: When to Graduate

You have a Bash script. It started as ten lines. It's now 200 lines and nobody touches it without fear. There's a `jq` pipeline that breaks every time the API changes shape. Error handling is a maze of `$?` checks and `|| exit 1` guards that still let things slip through. You added a flag with `getopts` and it took an hour. A colleague asked you to add logging and you said "later."

That's the ceiling. Every ops engineer hits it eventually — the point where Bash stops being a tool and starts being a liability. Python is what's on the other side.

This article isn't about Python being better than Bash. Bash is excellent at what it does. This is about recognizing the moment your work has outgrown the tool, and knowing what to pick up next.

## Is Python Installed?

On any modern Linux system, almost certainly yes:

```bash title="Check Python Version" linenums="1"
python3 --version
```

If you get `Python 3.8` or higher, you're ready. If not, on RHEL/CentOS/Rocky:

```bash title="Install Python on RHEL-family" linenums="1"
sudo dnf install python3
```

On Debian/Ubuntu:

```bash title="Install Python on Debian-family" linenums="1"
sudo apt install python3
```

That's it. No compiling from source. No version managers needed to get started.

## Running a Python Script

Python scripts work exactly like shell scripts:

```python title="check_disk.py" linenums="1"
#!/usr/bin/env python3  # (1)!
import shutil

total, used, free = shutil.disk_usage("/")
pct = (used / total) * 100

if pct > 90:
    print(f"ALERT: / is at {pct:.1f}% — take action")
else:
    print(f"OK: / is at {pct:.1f}%")

if __name__ == "__main__":  # (2)!
    pass
```

1. Use `env python3` rather than a hardcoded path — it finds the right Python regardless of where it's installed
2. This guard means the script only runs when executed directly, not when imported by another script — a habit worth building from day one

```bash title="Running the Script" linenums="1"
chmod +x check_disk.py
./check_disk.py

# Or without the shebang:
python3 check_disk.py
```

No compilation. No build step. Same mental model as Bash.

## When to Stay in Bash

Bash is still the right tool for:

- **One-liners and pipelines** — `ps aux | grep nginx | awk '{print $2}'` — Bash wins, don't fight it
- **Glue scripts that invoke tools** — if you're writing `kubectl apply && echo done`, stay in Bash
- **Shell startup files** — `.bashrc`, `.profile`, `.bash_profile` must be Bash
- **Scripts that need zero dependencies** — Bash is always available; Python sometimes isn't (containers, minimal images)
- **Anything under ~30 lines with no data manipulation** — the overhead of Python isn't worth it

The rule of thumb: **if your script is mostly running commands and wiring their output together, stay in Bash.** That's what Bash is built for.

## When to Reach for Python

Switch when your Bash script starts doing any of these:

- **Parsing JSON or YAML** — `jq` one-liners become unmaintainable; Python's `json` module is clean and handles errors
- **HTTP API calls with real error handling** — `curl | jq` pipelines fail silently on 4xx/5xx; `requests` doesn't
- **Error handling beyond `$?`** — try/except gives you structured, specific error handling instead of return code archaeology
- **Complex data manipulation** — filtering nested structures, deduplicating, sorting by field — Bash is not the right tool
- **CLI tools other people will use** — `getopts` is painful; `argparse` produces proper `--help` output automatically
- **Anything someone else has to maintain** — advanced Bash is write-only; Python reads like what it does
- **Tests** — you can't easily unit-test Bash; Python has `pytest`

## The Same Task, Two Ways

Here are four everyday ops tasks in both languages. The goal isn't to prove Python is always better — it's to show you the shape of the translation.

### Parsing a JSON API Response

=== ":simple-gnubash: Bash"

    ```bash title="Bash: Parse JSON with jq" linenums="1"
    curl -s https://api.example.com/pods \
      | jq -r '.items[] | select(.status.phase == "Running") | .metadata.name'
    ```

    Works until: the API adds pagination, returns a 401, changes the field name, or you need to do anything with the names beyond printing them.

=== ":material-language-python: Python"

    ```python title="Python: Parse JSON" linenums="1"
    import requests

    response = requests.get("https://api.example.com/pods")
    response.raise_for_status()  # (1)!

    pods = response.json()
    running = [p["metadata"]["name"] for p in pods["items"]
               if p["status"]["phase"] == "Running"]  # (2)!

    for name in running:
        print(name)
    ```

    1. Raises an exception on 4xx/5xx — no more silent failures from a bad token or missing permissions
    2. The filter logic is readable Python, not a `jq` expression you have to look up the syntax for

### Disk Usage Check

=== ":simple-gnubash: Bash"

    ```bash title="Bash: Disk Check" linenums="1"
    USAGE=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
    if [ "$USAGE" -gt 90 ]; then
        echo "ALERT: Disk usage is ${USAGE}%"
    fi
    ```

    Breaks on macOS (different `df` output format). Fragile to column ordering changes. The `tr -d '%'` stripping is easy to forget.

=== ":material-language-python: Python"

    ```python title="Python: Disk Check" linenums="1"
    import shutil

    total, used, free = shutil.disk_usage("/")  # (1)!
    pct = (used / total) * 100

    if pct > 90:
        print(f"ALERT: Disk usage is {pct:.1f}%")
    ```

    1. `shutil.disk_usage()` calls the OS directly — no `df | awk | tr` pipeline, works identically on Linux and macOS

### Processing Multiple Log Files

=== ":simple-gnubash: Bash"

    ```bash title="Bash: Find 500 Errors in Nginx Logs" linenums="1"
    for f in /var/log/nginx/*.log; do
        echo "=== $f ==="
        grep " 500 " "$f" | tail -5
    done
    ```

=== ":material-language-python: Python"

    ```python title="Python: Find 500 Errors in Nginx Logs" linenums="1"
    from pathlib import Path

    for log_file in Path("/var/log/nginx").glob("*.log"):  # (1)!
        print(f"=== {log_file} ===")
        lines = log_file.read_text().splitlines()
        errors = [line for line in lines if " 500 " in line]
        for line in errors[-5:]:
            print(line)
    ```

    1. `Path.glob()` handles filenames with spaces correctly — no word-splitting surprises

For this specific task Bash and Python are roughly equivalent. Python wins when you need to do more with the results: aggregate counts across all files, write a summary to a report, filter by time window.

### Error Handling

=== ":simple-gnubash: Bash"

    ```bash title="Bash: Error Handling" linenums="1"
    set -e
    result=$(some_command) || { echo "Command failed: $?"; exit 1; }
    process_result "$result"
    ```

    `set -e` has surprising exceptions. `$?` tells you something failed but not what or why. Cleanup on failure requires traps.

=== ":material-language-python: Python"

    ```python title="Python: Error Handling" linenums="1"
    import subprocess

    try:
        result = subprocess.run(
            ["some_command"],
            capture_output=True, text=True, check=True  # (1)!
        )
        process_result(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed (exit {e.returncode}): {e.stderr}")  # (2)!
        raise SystemExit(1)
    ```

    1. `check=True` raises `CalledProcessError` if the command exits non-zero — no `$?` checking
    2. `e.returncode` and `e.stderr` give you specific, structured information about what failed

## Key Syntax Differences

The things that trip up Bash engineers in their first week of Python:

| Bash | Python | What Changed |
|:-----|:-------|:-------------|
| `$variable` | `variable` | No `$` prefix — just the name |
| `if [ condition ]; then` | `if condition:` | No brackets, no `then`, colon ends the line |
| `fi` / `done` | (indentation) | Indentation defines blocks — no closing keywords |
| `echo "text"` | `print("text")` | `print()` is a function call |
| `$?` | `try/except` | Exceptions, not return codes |
| `$1`, `$2` | `sys.argv[1]` | Or use `argparse` for real CLI tools |
| `$(command)` | `subprocess.run(...)` | Explicit function for running commands |
| `"$VAR"` quoting | (not needed) | Python variables don't word-split |

## The Standard Library: Your Old Tools, Built In

One of Python's biggest advantages: the standard library already contains most of what you'd reach for external tools to do.

| You reach for... | Python has built-in... |
|:----------------|:-----------------------|
| `jq` | `json` module |
| `find` | `pathlib.Path.glob()` / `.rglob()` |
| `cp`, `mv`, `rm -rf` | `shutil` module |
| `tar`, `gzip` | `tarfile`, `gzip`, `zipfile` modules |
| `getopts` / `getopt` | `argparse` module |
| `logger` / syslog | `logging` module |
| `env` / `export` | `os.environ` |
| `date` | `datetime` module |
| `curl` (basic) | `urllib.request` (or `requests` via pip) |

This means fewer external dependencies, more portable scripts, and consistent behavior across platforms.

!!! warning "Standard Library vs pip"

    Everything in the table above ships with Python — no `pip install` needed. The one exception in this article: `requests` is a third-party library. For everything else in Essentials, we use the standard library only.

    When you do need a third-party library: `pip install requests` or, better, use a virtual environment.

## Practice Problems

??? question "Practice Problem 1: Translate a Bash Script"

    Translate this Bash snippet to Python without using `subprocess`. Use Python's standard library to do the same work natively:

    ```bash
    for dir in /var/log/*/; do
        count=$(ls "$dir" | wc -l)
        echo "$dir: $count files"
    done
    ```

    ??? tip "Answer"

        ```python title="Count Files Per Log Directory" linenums="1"
        from pathlib import Path

        for directory in sorted(Path("/var/log").iterdir()):
            if directory.is_dir():
                file_count = len(list(directory.iterdir()))
                print(f"{directory}: {file_count} files")
        ```

        `Path.iterdir()` replaces `ls`. `len(list(...))` replaces `wc -l`. No subprocess, no pipes. The result is also a number you can compare or sort — try doing `sort -n` across the Bash output cleanly.

??? question "Practice Problem 2: When Would You NOT Switch?"

    Your teammate wants to rewrite this in Python. Is that a good idea?

    ```bash
    systemctl restart nginx && echo "Restarted" || echo "Failed"
    ```

    ??? tip "Answer"

        No. This is one command with clean success/failure handling. The Bash is immediately readable to every ops engineer, requires no dependencies, and does exactly one thing.

        You'd switch to Python when this becomes part of something larger — a deployment script that also validates config, calls an API, and writes to a log file. Rewriting a one-liner for its own sake adds complexity without ROI.

??? question "Practice Problem 3: Identify the Breaking Point"

    At what point would you graduate this Bash script to Python?

    ```bash
    #!/bin/bash
    set -e

    RESPONSE=$(curl -s https://api.example.com/servers)
    RUNNING=$(echo "$RESPONSE" | jq -r '.[] | select(.status == "running") | .name')

    for server in $RUNNING; do
        echo "Checking $server..."
        ssh "$server" "uptime"
    done
    ```

    ??? tip "Answer"

        The breaking point is already here — specifically the `for server in $RUNNING` line. Word-splitting on newline-separated `jq` output breaks if any server name contains a space. Unquoted `$RUNNING` is a bug waiting to happen.

        Other signals it needs Python:

        - The `jq` filter will break if the API returns an error body instead of an array
        - There's no retry logic if an SSH connection fails
        - Adding any more logic (logging results, alerting on failure) pushes this past the Bash comfort zone

## Key Takeaways

| Question | Answer |
|:---------|:-------|
| **When to stay in Bash** | One-liners, pipelines, glue scripts, shell startup files, <30-line scripts with no data manipulation |
| **When to switch to Python** | JSON/API work, real error handling, complex data, CLI tools, anything shared or maintained |
| **No `$` prefix** | Python variables are just names — `count`, not `$count` |
| **Indentation over keywords** | No `fi`, `done`, `then` — indentation ends blocks |
| **Standard library** | Python ships with replacements for `jq`, `find`, `shutil`, `argparse`, `logging` |
| **Shebang** | `#!/usr/bin/env python3` — `env` finds the right Python wherever it's installed |

## Further Reading

### On This Site

- [Running System Commands](running_commands.md) — `subprocess.run()` as your replacement for `$(...)` and backticks
- [Working with JSON](working_with_json.md) — the `json` module as your replacement for `jq`
- [Error Handling](error_handling.md) — `try/except` as your replacement for `$?` and `set -e`

### Official Documentation

- [Python Standard Library](https://docs.python.org/3/library/index.html) — everything that ships with Python, no `pip` needed
- [pathlib — Object-oriented filesystem paths](https://docs.python.org/3/library/pathlib.html)
- [subprocess — Subprocess management](https://docs.python.org/3/library/subprocess.html)
- [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html)

### External Resources

- [Real Python: Bash vs Python](https://realpython.com/python-vs-bash/) — deeper comparison with more examples

---

Bash and Python aren't competitors — they're different tools for different jobs. Most platform engineers end up using both daily: Bash for the quick wiring, Python for anything that needs to be reliable, readable, or maintained by someone other than you. The trick is knowing which one you're holding when the complexity starts to climb.
