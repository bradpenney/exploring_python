---
title: Argument Parsing with argparse
description: "Replace Bash's getopts with Python's argparse — positional args, optional flags, default values, subcommands, and automatic --help generation for CLI tools."
---

# Argument Parsing with argparse

Bash's `getopts` is a rite of passage. You write it once, it works, and you copy-paste it into
every script forever. It handles short flags (`-v`, `-f file`) well enough, but the moment you
need `--long-flags`, `--help` text, type coercion, or subcommands, `getopts` becomes a maze
of `case` statements and manual string handling.

Python's `argparse` is the standard library alternative. You describe what arguments your
script accepts, and `argparse` handles parsing, validation, help text, and error messages
automatically.

## Coming from Bash

```bash title="Bash: getopts"
#!/bin/bash
# Script: deploy.sh -e prod -v --dry-run

ENVIRONMENT=""
VERBOSE=false
DRY_RUN=false

# getopts only handles short flags; long flags require manual parsing
while getopts "e:v" opt; do
    case $opt in
        e) ENVIRONMENT="$OPTARG" ;;
        v) VERBOSE=true ;;
        *) echo "Usage: $0 -e <env> [-v]" >&2; exit 1 ;;
    esac
done

# Long flags need a separate loop
for arg in "$@"; do
    case $arg in
        --dry-run) DRY_RUN=true ;;
    esac
done

if [[ -z "$ENVIRONMENT" ]]; then
    echo "Error: -e <environment> is required" >&2
    exit 1
fi

echo "Deploying to $ENVIRONMENT (verbose=$VERBOSE, dry-run=$DRY_RUN)"
```

```python title="Python: argparse"
#!/usr/bin/env python3
# Script: deploy.py --environment prod --verbose --dry-run

import argparse

parser = argparse.ArgumentParser(description="Deploy application to target environment")
parser.add_argument("--environment", "-e", required=True, help="Target environment (prod, staging)")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
parser.add_argument("--dry-run", action="store_true", help="Show what would happen without doing it")

args = parser.parse_args()
print(f"Deploying to {args.environment} (verbose={args.verbose}, dry_run={args.dry_run})")
```

Key differences:

| Bash (`getopts`) | Python (`argparse`) |
|:-----------------|:--------------------|
| Short flags only (`-e`) | Long and short flags (`--environment`, `-e`) |
| Manual error messages | Automatic error messages and exit |
| No `--help` | `--help` generated automatically |
| Type is always string | `type=int`, `type=float`, etc. for auto-conversion |
| Manual required-check | `required=True` on the argument |
| Subcommands need manual parsing | Built-in subparser support |

## Basic Usage

### Positional Arguments

Positional arguments are required and order-dependent — like `cp source dest`:

```python title="Positional Arguments" linenums="1"
import argparse

parser = argparse.ArgumentParser(description="Copy a file")
parser.add_argument("source", help="Source file path")       # (1)!
parser.add_argument("dest", help="Destination file path")

args = parser.parse_args()
print(f"Copying {args.source} to {args.dest}")
```

1. No `--` prefix = positional argument; required by default

Running `python copy.py /tmp/foo.txt /var/log/foo.txt` sets `args.source` and `args.dest`.
Running `python copy.py` produces an error automatically:
```text
error: the following arguments are required: source, dest
```

### Optional Arguments (Flags)

Optional arguments use `--name` (or `-n` for short form):

```python title="Optional Flags" linenums="1"
import argparse

parser = argparse.ArgumentParser(description="Backup a directory")
parser.add_argument("--output", "-o", default="/tmp/backup", help="Output directory")  # (1)!
parser.add_argument("--compress", "-c", action="store_true", help="Compress the backup")  # (2)!
parser.add_argument("--level", type=int, default=9, help="Compression level (1-9)")      # (3)!

args = parser.parse_args()
print(f"Output: {args.output}")
print(f"Compress: {args.compress}")
print(f"Level: {args.level}")
```

1. `default="/tmp/backup"` — value used if flag not provided; `args.output` is always set
2. `action="store_true"` — flag with no value; `True` if present, `False` if absent
3. `type=int` — argparse converts the string "9" to integer `9` automatically

## Argument Types and Defaults

`argparse` converts argument values from strings to Python types:

```python title="Type Conversion" linenums="1"
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8080)             # (1)!
parser.add_argument("--threshold", type=float, default=0.95)
parser.add_argument("--log-file", type=argparse.FileType("w"),   # (2)!
                    default="-", help="Log file (default: stdout)")
parser.add_argument("--workers", type=int, choices=[1, 2, 4, 8]) # (3)!

args = parser.parse_args()
print(f"Port: {args.port} (type: {type(args.port).__name__})")
```

1. `type=int` — `args.port` is an `int`, not a string; validation is free
2. `argparse.FileType("w")` — opens the file for writing; `"-"` means stdout
3. `choices=[1, 2, 4, 8]` — rejects any value not in the list

## Required vs Optional

```python title="Required Arguments" linenums="1"
import argparse

parser = argparse.ArgumentParser(description="Connect to a database")
parser.add_argument("--host", required=True, help="Database host")          # (1)!
parser.add_argument("--port", type=int, default=5432)
parser.add_argument("--database", "--db", required=True)                    # (2)!
parser.add_argument("--user", default="postgres")
parser.add_argument("--password", help="DB password (prefer env var DB_PASS)")

args = parser.parse_args()
```

1. `required=True` on an optional argument — argparse enforces it and shows it in the error
2. Multiple names for the same argument — `--database` or `--db` both work

## Automatic --help

`argparse` generates `--help` for free. Every argument's `help=` string appears:

```python title="Script with Help Text" linenums="1"
import argparse

parser = argparse.ArgumentParser(
    description="Deploy application to a target environment.",
    epilog="Example: deploy.py --environment prod --tag v2.1.0"    # (1)!
)
parser.add_argument("--environment", "-e", required=True,
                    choices=["dev", "staging", "prod"],
                    help="Target environment")
parser.add_argument("--tag", "-t", required=True,
                    help="Docker image tag to deploy (e.g. v2.1.0)")
parser.add_argument("--dry-run", action="store_true",
                    help="Print what would happen without executing")
parser.add_argument("--verbose", "-v", action="store_true")

args = parser.parse_args()
```

1. `epilog=` adds text after the argument list in `--help` output — good for examples

Running `python deploy.py --help`:
```text
usage: deploy.py [-h] --environment {dev,staging,prod} --tag TAG [--dry-run] [--verbose]

Deploy application to a target environment.

options:
  -h, --help            show this help message and exit
  --environment {dev,staging,prod}, -e {dev,staging,prod}
                        Target environment
  --tag TAG, -t TAG     Docker image tag to deploy (e.g. v2.1.0)
  --dry-run             Print what would happen without executing
  --verbose, -v

Example: deploy.py --environment prod --tag v2.1.0
```

No code required — this is completely free.

## Subcommands

Tools like `git`, `kubectl`, and `docker` use subcommands. `argparse` supports this with
subparsers:

```python title="Subcommands" linenums="1"
import argparse

parser = argparse.ArgumentParser(description="Manage application deployments")
subparsers = parser.add_subparsers(dest="command", required=True)   # (1)!

# 'deploy' subcommand
deploy_parser = subparsers.add_parser("deploy", help="Deploy a new version")
deploy_parser.add_argument("--environment", "-e", required=True)
deploy_parser.add_argument("--tag", "-t", required=True)
deploy_parser.add_argument("--dry-run", action="store_true")

# 'rollback' subcommand
rollback_parser = subparsers.add_parser("rollback", help="Roll back to previous version")
rollback_parser.add_argument("--environment", "-e", required=True)
rollback_parser.add_argument("--steps", type=int, default=1, help="How many versions to roll back")

# 'status' subcommand
status_parser = subparsers.add_parser("status", help="Show deployment status")
status_parser.add_argument("--environment", "-e")

args = parser.parse_args()

if args.command == "deploy":
    print(f"Deploying {args.tag} to {args.environment} (dry-run={args.dry_run})")
elif args.command == "rollback":
    print(f"Rolling back {args.steps} step(s) in {args.environment}")
elif args.command == "status":
    env = args.environment or "all"
    print(f"Status for: {env}")
```

1. `dest="command"` stores which subcommand was used in `args.command`

Usage:
```bash
python manage.py deploy --environment prod --tag v2.1.0
python manage.py rollback --environment prod --steps 2
python manage.py status
python manage.py --help        # Shows all subcommands
python manage.py deploy --help # Shows deploy-specific help
```

## A Complete Script Example

Here's a complete, production-style script using `argparse`:

```python title="Complete CLI Script" linenums="1"
#!/usr/bin/env python3
"""
check_hosts.py — Check connectivity to a list of hosts.
"""
import argparse
import logging
import os
import subprocess
import sys


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
    )


def check_host(host: str, count: int = 1) -> bool:
    """Ping a host. Returns True if reachable."""
    result = subprocess.run(
        ["ping", "-c", str(count), "-W", "2", host],
        capture_output=True
    )
    return result.returncode == 0


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check connectivity to one or more hosts.",
        epilog="Example: check_hosts.py web-01 web-02 --count 3 --output /tmp/report.txt"
    )
    parser.add_argument(
        "hosts",
        nargs="+",                                          # (1)!
        help="One or more hostnames or IP addresses"
    )
    parser.add_argument(
        "--count", "-c",
        type=int,
        default=1,
        help="Number of ping packets to send (default: 1)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Write results to this file (default: stdout)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show debug output"
    )
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Exit immediately on first failure"
    )

    args = parser.parse_args()
    setup_logging(args.verbose)
    log = logging.getLogger(__name__)

    results = []
    failed = False

    for host in args.hosts:
        log.debug("Checking %s with %d packets", host, args.count)
        reachable = check_host(host, args.count)
        status = "UP" if reachable else "DOWN"
        results.append(f"{host}: {status}")
        log.info("%s is %s", host, status)

        if not reachable:
            failed = True
            if args.fail_fast:
                log.error("Stopping on first failure (--fail-fast)")
                break

    output = "\n".join(results)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        log.info("Results written to %s", args.output)
    else:
        print(output)

    sys.exit(1 if failed else 0)                            # (2)!


if __name__ == "__main__":
    main()
```

1. `nargs="+"` — one or more positional arguments; stored as a list in `args.hosts`
2. Exit code 1 if any host is down — makes the script composable in pipelines and CI

Running it:
```bash
python check_hosts.py web-01 web-02 db-01
python check_hosts.py web-01 --count 3 --verbose
python check_hosts.py web-01 web-02 --output /tmp/host-check.txt --fail-fast
```

## Handling Mutually Exclusive Arguments

Some flags shouldn't be used together. `argparse` enforces this:

```python title="Mutually Exclusive Arguments" linenums="1"
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()   # (1)!
group.add_argument("--verbose", "-v", action="store_true")
group.add_argument("--quiet", "-q", action="store_true")

args = parser.parse_args()
```

1. `add_mutually_exclusive_group()` — passing both `--verbose` and `--quiet` is an error

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`add_argument("name")`** | Positional argument — required, no `--` prefix |
| **`add_argument("--flag")`** | Optional argument — identified by name, not position |
| **`required=True`** | Makes an optional argument mandatory |
| **`action="store_true"`** | Boolean flag — `True` if present, `False` if absent |
| **`type=int`** | Auto-converts string input to the specified type |
| **`default=value`** | Value when argument is not provided |
| **`choices=[...]`** | Restricts valid values; shown in `--help` |
| **`nargs="+"`** | One or more values; stored as a list |
| **`--help`** | Generated automatically — no code needed |
| **Subparsers** | `add_subparsers()` for `git`/`kubectl`-style subcommands |

## Practice Problems

??? question "Practice Problem 1: Script with Required and Optional Args"

    Write a script called `log_search.py` that accepts:

    - A required positional argument: the log file path
    - An optional `--pattern` flag (default `"ERROR"`)
    - An optional `--after` flag for a line number to start from (int, default 0)
    - A `--verbose` boolean flag

    Print what `args` would look like for `log_search.py /var/log/app.log --pattern WARN --after 100`.

    ??? tip "Answer"

        ```python title="log_search.py" linenums="1"
        import argparse

        parser = argparse.ArgumentParser(description="Search log files")
        parser.add_argument("logfile", help="Path to the log file")
        parser.add_argument("--pattern", default="ERROR", help="Pattern to search for")
        parser.add_argument("--after", type=int, default=0,
                            help="Start from this line number")
        parser.add_argument("--verbose", "-v", action="store_true")

        args = parser.parse_args()
        # For: log_search.py /var/log/app.log --pattern WARN --after 100
        # args.logfile  = '/var/log/app.log'
        # args.pattern  = 'WARN'
        # args.after    = 100   (int, not string)
        # args.verbose  = False
        ```

        `type=int` on `--after` means `args.after` is already an integer — no
        `int(args.after)` conversion needed.

??? question "Practice Problem 2: Add --version to a Script"

    How would you add a `--version` flag that prints `"myapp 2.1.0"` and exits?

    ??? tip "Answer"

        ```python title="Version Flag" linenums="1"
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--version", "-V",
            action="version",
            version="myapp 2.1.0"    # (1)!
        )
        args = parser.parse_args()
        ```

        1. `action="version"` is a special action that prints the version string
           and exits with code 0 — no code required.

        Running `python myapp.py --version` prints `myapp 2.1.0` and exits.

??? question "Practice Problem 3: Accept Multiple Values"

    Write an argument definition that accepts one or more environment names,
    like `deploy.py prod` or `deploy.py dev staging prod`. The environments should
    be stored as a list.

    ??? tip "Answer"

        ```python title="Multiple Values" linenums="1"
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument(
            "environments",
            nargs="+",                           # (1)!
            choices=["dev", "staging", "prod"],
            help="Target environments"
        )
        args = parser.parse_args()
        # deploy.py dev staging → args.environments = ['dev', 'staging']
        ```

        1. `nargs="+"` accepts one or more values as a list. Use `nargs="*"` for
           zero or more. Use `nargs=N` for exactly N values.

??? question "Practice Problem 4: getopts vs argparse Trade-offs"

    When would you still use `getopts` in Bash instead of switching to Python's `argparse`?

    ??? tip "Answer"

        Use `getopts` when:

        - The script is **pure Bash** with no other Python dependencies — adding Python
          just for argument parsing may not be worth it
        - The script is **very short** (< 20 lines) with only 1–2 simple flags
        - You need **POSIX portability** across systems where Python may not be available

        Switch to Python's `argparse` when:

        - You need **long flags** (`--environment`, not just `-e`)
        - You need **type conversion** (integers, floats, file paths)
        - You need **subcommands** or complex argument structures
        - You want **automatic `--help`** without writing help text yourself
        - The script is already doing other Python work (API calls, file processing, etc.)
        - You need **input validation** with good error messages

## Further Reading

### On This Site

- [Running Commands](../system/running_commands.md) — `subprocess` for the system calls your CLI tool makes
- [Exit Codes](exit_codes.md) — `sys.exit()` conventions for CLI tools
- [Logging](../system/logging.md) — `--verbose` flag wired to log level
- [Error Handling](../scripting_fundamentals/error_handling.md) — handling errors in CLI scripts

### Official Documentation

- [argparse — Official Python Docs](https://docs.python.org/3/library/argparse.html) — full reference
- [argparse Tutorial](https://docs.python.org/3/howto/argparse.html) — step-by-step guide

### External Resources

- [click](https://click.palletsprojects.com/) — decorator-based CLI framework; more ergonomic than `argparse` for complex tools
- [Typer](https://typer.tiangolo.com/) — CLI framework built on type hints; worth knowing for larger projects

---

`argparse` is the right tool for any script that takes more than one or two arguments.
The investment — describing your arguments once — pays off in automatic `--help`, type
validation, and error messages you didn't have to write. No more parsing `$1`, `$2`, `$3`
by hand.
