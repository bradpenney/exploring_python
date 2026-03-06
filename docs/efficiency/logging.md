---
title: Logging in Python
description: "Python's logging module — log levels, handlers, formatters, and structured logging patterns that replace print() and echo in production scripts."
---

# Logging

Bash scripts log with `echo`. Python scripts too often follow the same habit. Both work fine in
development, but `print()` to stdout doesn't give you log levels, file output, timestamps, or any
way to control verbosity without modifying code.

Python's `logging` module is a lightweight but production-ready logging system built into the
standard library. It takes five minutes to set up and saves hours of debugging.

## Coming from Bash

```bash title="Bash Logging" linenums="1"
# Logging in Bash: echo with timestamps, redirect to file
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a /var/log/myapp.log
}

log "INFO: Starting deployment"
log "ERROR: Failed to connect to database" >&2

# Verbosity: manual flags
[[ "$VERBOSE" == "true" ]] && log "DEBUG: Connecting to $DB_HOST"
```

```python title="Python Logging" linenums="1"
import logging

# One-time setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger(__name__)

# Same operations as Bash — but with built-in level filtering
log.info("Starting deployment")
log.error("Failed to connect to database")   # Goes to stderr automatically
log.debug("Connecting to %s", db_host)       # Only prints if level is DEBUG
```

Key differences:

| Bash | Python |
|:-----|:-------|
| `echo "[$(date)] $msg"` | `log.info("msg")` — timestamp added by formatter |
| Redirect `>&2` for errors | `logging.error()` goes to stderr by default |
| `[[ "$VERBOSE" == "true" ]]` | Set log level to `DEBUG` — no code changes needed |
| `tee -a logfile` | Add a `FileHandler` — writes to both file and console |
| Roll your own levels | Built-in: DEBUG, INFO, WARNING, ERROR, CRITICAL |

## Log Levels

Python logging has five built-in levels, in increasing severity:

| Level | Numeric | When to use |
|:------|:--------|:------------|
| `DEBUG` | 10 | Detailed diagnostic info — only in development |
| `INFO` | 20 | Confirmation that things are working — normal operation |
| `WARNING` | 30 | Something unexpected happened, but script can continue |
| `ERROR` | 40 | A serious problem — something failed |
| `CRITICAL` | 50 | The script cannot continue |

```python title="Using Log Levels" linenums="1"
import logging

log = logging.getLogger(__name__)

log.debug("Processing file: %s", filename)         # Development only
log.info("Deployment started for %s", app_name)    # Normal operation
log.warning("Disk at %d%%, approaching limit", pct) # Needs attention
log.error("Failed to connect to %s", db_host)       # Something broke
log.critical("Database unreachable, aborting")      # Fatal
```

The level you set determines what's printed: `INFO` shows INFO and above (WARNING, ERROR,
CRITICAL), but suppresses DEBUG. Change one line to get more or less output.

## Basic Setup

### Quick Setup with basicConfig

For simple scripts, `basicConfig()` gets you running in one line:

```python title="basicConfig Setup" linenums="1"
import logging

logging.basicConfig(
    level=logging.INFO,                          # (1)!
    format="%(asctime)s %(levelname)-8s %(message)s",   # (2)!
    datefmt="%Y-%m-%d %H:%M:%S"
)

log = logging.getLogger(__name__)                # (3)!
log.info("Script started")
```

1. `level=logging.INFO` — suppress DEBUG messages; show INFO and above
2. `%(levelname)-8s` pads level name to 8 chars for alignment (INFO vs WARNING)
3. `__name__` uses the module name as the logger name — standard practice

Sample output:
```text
2024-01-15 09:23:45 INFO     Script started
2024-01-15 09:23:46 WARNING  Disk at 90%, approaching limit
2024-01-15 09:23:47 ERROR    Failed to write /var/log/app.log
```

### Format Variables

Common format variables for the `format` string:

| Variable | What it provides |
|:---------|:----------------|
| `%(asctime)s` | Timestamp (format controlled by `datefmt`) |
| `%(levelname)s` | Log level name: DEBUG, INFO, WARNING, ERROR, CRITICAL |
| `%(name)s` | Logger name (usually the module name) |
| `%(message)s` | The log message itself |
| `%(filename)s` | Source filename |
| `%(lineno)d` | Line number |
| `%(funcName)s` | Function name |

## Handlers: Where Logs Go

Handlers control where log output goes. A logger can have multiple handlers:

```python title="Multiple Handlers" linenums="1"
import logging
import sys

# Create logger
log = logging.getLogger("myapp")
log.setLevel(logging.DEBUG)          # (1)!

# Console handler — INFO and above to stdout
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))

# File handler — DEBUG and above to file
file_handler = logging.FileHandler("/var/log/myapp.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s %(filename)s:%(lineno)d %(message)s"
))

log.addHandler(console)
log.addHandler(file_handler)         # (2)!
```

1. The logger level is the minimum — handlers can further restrict what they handle
2. Both handlers are active — INFO+ goes to console, DEBUG+ goes to file

## A Reusable Setup Function

For scripts you'll actually deploy, a setup function keeps configuration centralized:

```python title="Reusable Logging Setup" linenums="1"
import logging
import sys
from pathlib import Path

def setup_logging(
    level: str = "INFO",
    log_file: str | None = None
) -> logging.Logger:
    """Configure logging for a script.

    Args:
        level: Log level string (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional path to write logs to (in addition to stdout)
    """
    log = logging.getLogger()
    log.setLevel(getattr(logging, level.upper(), logging.INFO))

    fmt = logging.Formatter(
        "%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Always log to stdout
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(fmt)
    log.addHandler(handler)

    # Optionally log to a file
    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(log_file)
        fh.setFormatter(fmt)
        log.addHandler(fh)

    return log


# Usage
import os
log = setup_logging(
    level=os.environ.get("LOG_LEVEL", "INFO"),   # Controllable via env var
    log_file="/var/log/myapp/deploy.log"
)
```

## Controlling Verbosity Without Code Changes

The value of log levels: flip verbosity with an environment variable, not a code change:

```python title="Environment-Controlled Verbosity" linenums="1"
import logging
import os

level = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=getattr(logging, level, logging.INFO))
log = logging.getLogger(__name__)

# This only prints when LOG_LEVEL=DEBUG
log.debug("Connecting to %s:%d", db_host, db_port)
```

```bash
# Normal run
python deploy.py

# Verbose debug run
LOG_LEVEL=DEBUG python deploy.py
```

## Logging Exceptions

When catching exceptions, log the full traceback with `log.exception()`:

```python title="Logging Exceptions" linenums="1"
import logging

log = logging.getLogger(__name__)

try:
    result = risky_operation()
except FileNotFoundError as e:
    log.error("Config file not found: %s", e)          # (1)!
    raise
except Exception as e:
    log.exception("Unexpected error in deployment")    # (2)!
    raise
```

1. `log.error()` — logs the message only
2. `log.exception()` — logs the message AND the full traceback (only call inside `except`)

Output of `log.exception()`:
```text
2024-01-15 09:23:45 ERROR    Unexpected error in deployment
Traceback (most recent call last):
  File "deploy.py", line 45, in main
    result = risky_operation()
  ...
RuntimeError: Connection refused
```

## Structured Logging

For scripts that feed into log aggregation systems (Datadog, CloudWatch, Splunk, ELK), JSON
log output makes filtering and querying much easier:

```python title="JSON Structured Logging" linenums="1"
import logging
import json
import sys
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Emit logs as JSON lines for structured logging systems."""

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)


# Setup
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JSONFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])
log = logging.getLogger(__name__)

# Usage
log.info("Deployment started")
log.error("Connection failed", extra={"host": "db01", "port": 5432})
```

Output:
```json
{"timestamp": "2024-01-15T09:23:45Z", "level": "INFO", "logger": "__main__", "message": "Deployment started"}
{"timestamp": "2024-01-15T09:23:46Z", "level": "ERROR", "logger": "__main__", "message": "Connection failed"}
```

## Practical Patterns

### Script Template with Logging

```python title="Script Template" linenums="1"
#!/usr/bin/env python3
"""
deploy.py — Deploy application to target environment.
"""
import logging
import os
import sys

# Setup logging before any other imports
logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout
)
log = logging.getLogger(__name__)


def deploy(environment: str) -> None:
    log.info("Starting deployment to %s", environment)
    try:
        # ... deployment logic ...
        log.info("Deployment complete")
    except Exception:
        log.exception("Deployment failed")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        log.error("Usage: %s <environment>", sys.argv[0])
        sys.exit(1)
    deploy(sys.argv[1])
```

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`logging.getLogger(__name__)`** | Create a named logger — use `__name__` by convention |
| **`basicConfig()`** | Quick setup for simple scripts |
| **Log levels** | DEBUG < INFO < WARNING < ERROR < CRITICAL |
| **`LOG_LEVEL` env var** | Control verbosity without code changes |
| **`log.exception()`** | Log error + full traceback — only inside `except` |
| **Handlers** | Where logs go: `StreamHandler` (stdout/stderr), `FileHandler` |
| **Formatters** | What log lines look like: timestamp, level, message |
| **Structured logging** | JSON output for log aggregation systems |

## Practice Problems

??? question "Practice Problem 1: Replace print() with logging"

    This script uses `print()` for all output. Rewrite it to use `logging` with appropriate
    log levels for each message.

    ```python
    def backup_database(host, db_name):
        print(f"Starting backup of {db_name} on {host}")
        print(f"DEBUG: connecting to {host}:5432")
        # ... backup logic ...
        print(f"WARNING: backup took longer than expected")
        print(f"Backup complete: {db_name}.sql.gz")
    ```

    ??? tip "Answer"

        ```python title="Logging Version" linenums="1"
        import logging

        log = logging.getLogger(__name__)

        def backup_database(host: str, db_name: str) -> None:
            log.info("Starting backup of %s on %s", db_name, host)
            log.debug("Connecting to %s:5432", host)
            # ... backup logic ...
            log.warning("Backup took longer than expected")
            log.info("Backup complete: %s.sql.gz", db_name)
        ```

        Now `log.debug()` is silenced in production (INFO level) and visible in development
        (`LOG_LEVEL=DEBUG`). No code changes needed.

??? question "Practice Problem 2: Verbosity Flag"

    How would you make a script's log level configurable via both a `--verbose` flag AND
    a `LOG_LEVEL` environment variable, with `--verbose` taking precedence?

    ??? tip "Answer"

        ```python title="Configurable Log Level" linenums="1"
        import argparse
        import logging
        import os

        parser = argparse.ArgumentParser()
        parser.add_argument("--verbose", "-v", action="store_true")
        args = parser.parse_args()

        if args.verbose:
            level = logging.DEBUG
        else:
            level_name = os.environ.get("LOG_LEVEL", "INFO").upper()
            level = getattr(logging, level_name, logging.INFO)

        logging.basicConfig(level=level, format="%(levelname)-8s %(message)s")
        ```

??? question "Practice Problem 3: Log and Re-raise"

    Write a function wrapper that logs any exception before re-raising it, adding context
    about which function failed.

    ??? tip "Answer"

        ```python title="Exception Logging Wrapper" linenums="1"
        import logging
        import functools

        log = logging.getLogger(__name__)

        def log_exceptions(func):
            """Decorator that logs exceptions before re-raising."""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    log.exception("Exception in %s()", func.__name__)
                    raise
            return wrapper

        @log_exceptions
        def deploy(env):
            raise RuntimeError("Connection refused")
        ```

??? question "Practice Problem 4: When to Use Each Level"

    For each scenario, choose the appropriate log level and explain why:

    1. A scheduled job starting its daily run
    2. A retry attempt because a connection failed (but succeeded on second try)
    3. A config value isn't set — using hardcoded default
    4. Database is unreachable and the script cannot continue
    5. Loop iteration details while processing 10,000 records

    ??? tip "Answer"

        1. `INFO` — normal operation, worth recording
        2. `WARNING` — something unusual happened (failure then recovery)
        3. `WARNING` — config should be set; using default is a fallback, not ideal
        4. `CRITICAL` or `ERROR` followed by `sys.exit(1)` — fatal failure
        5. `DEBUG` — too verbose for normal operation; useful only when diagnosing issues

## Further Reading

### On This Site

- [**Error Handling**](../essentials/error_handling.md) — `log.exception()` and `try/except` work together
- [**Environment Variables and Secrets**](environment_and_secrets.md) — controlling log level via environment variables

### Official Documentation

- [**logging — Logging facility for Python**](https://docs.python.org/3/library/logging.html) — full reference
- [**Logging HOWTO**](https://docs.python.org/3/howto/logging.html) — practical guide
- [**Logging Cookbook**](https://docs.python.org/3/howto/logging-cookbook.html) — recipes for common patterns

---

Every production script should use `logging` instead of `print()`. The setup cost is five lines.
The payoff: timestamps, levels, file output, and verbosity control — all without touching the
code that does the actual work.
