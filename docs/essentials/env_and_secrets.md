---
title: "Managing Credentials in Python Automation Scripts"
description: "Load API keys, passwords, and tokens in Python automation scripts using environment variables, .env files, and secrets stores — without hardcoding anything."
---

# Environment Variables and Secrets

!!! tip "Part of Essentials"
    This is part of [Essentials](../index.md#essentials) — core Python patterns for working platform engineers.

The [Day One safety guide](../day_one/safety_guide.md) told you not to hardcode credentials. This article shows you the full pattern for doing it properly — reading from environment variables, falling back gracefully, validating at startup, and working with `.env` files.

---

## Where You've Seen This

You already do this in `bash`:

```bash title="Credentials in bash"
export DB_PASSWORD="hunter2"
./deploy.sh
```

And in CI/CD — GitHub Actions calls them "secrets", GitLab calls them "CI/CD variables", but the mechanism is the same: the value is injected into the environment at runtime. Your script reads `$DB_PASSWORD` without ever seeing where it came from.

Docker Compose uses `.env` files. Kubernetes uses Secrets mounted as environment variables. The pattern is universal. Python gives you a cleaner API for reading and validating them.

---

## Reading from the Environment

```python title="Reading environment variables" linenums="1"
import os

api_key = os.environ["API_KEY"]          # (1)!
db_password = os.environ.get("DB_PASSWORD")  # (2)!
log_level = os.environ.get("LOG_LEVEL", "INFO")  # (3)!
```

1. `os.environ["API_KEY"]` raises `KeyError` if the variable isn't set. Use this for required variables — you want to fail immediately, not silently continue.
2. `os.environ.get("DB_PASSWORD")` returns `None` if the variable isn't set. Use for optional variables, or when you want to handle the missing case yourself.
3. `os.environ.get("LOG_LEVEL", "INFO")` returns `"INFO"` if `LOG_LEVEL` isn't set. Use for variables that have a sensible default.

---

## Fail Fast on Missing Required Credentials

A script that starts without its credentials and fails 30 steps later is painful to debug. Validate at startup:

```python title="Validate required environment variables" linenums="1"
import os
import sys

REQUIRED_VARS = [
    "API_KEY",
    "DB_HOST",
    "DB_PASSWORD",
]

def check_env():
    """Exit immediately if any required environment variables are missing."""
    missing = [var for var in REQUIRED_VARS if not os.environ.get(var)]
    if missing:
        print("✗ Missing required environment variables:")
        for var in missing:
            print(f"  {var}")
        sys.exit(1)

check_env()  # Call this before anything else in your script
```

Run this before you open database connections, before you import configuration, before you do anything. Missing credentials surface in the first second, not after a 45-second deploy sequence.

---

## The `.env` File Pattern

For local development, setting `export` for every variable before running a script is tedious. A `.env` file is the standard solution:

```text title=".env"
API_KEY=sk-abc123
DB_HOST=localhost
DB_PASSWORD=devpassword
LOG_LEVEL=DEBUG
```

**Never commit `.env` to git.** Add it to `.gitignore` immediately.

```bash title=".gitignore"
.env
.env.*
```

### Parsing a `.env` File Without a Library

For simple cases, you don't need `python-dotenv`:

```python title="Manual .env loading" linenums="1"
import os

def load_dotenv(path=".env"):
    """Load environment variables from a .env file.
    
    Does not override variables already set in the environment.
    """
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):  # (1)!
                    continue
                if "=" not in line:
                    continue
                key, _, value = line.partition("=")  # (2)!
                key = key.strip()
                value = value.strip().strip('"').strip("'")  # (3)!
                if key and key not in os.environ:  # (4)!
                    os.environ[key] = value
    except FileNotFoundError:
        pass  # No .env file is fine; rely on actual environment

load_dotenv()
```

1. Skip blank lines and comments (lines starting with `#`).
2. `partition("=")` splits on the first `=` only — handles values that contain `=` (like base64 tokens).
3. Strip surrounding quotes — `.env` files often quote values, Python's `os.environ` doesn't need them.
4. Don't override variables already set in the real environment. CI/CD secrets take precedence over `.env`.

### Using `python-dotenv`

If your project already has dependencies, `python-dotenv` is the standard library:

```bash title="Install python-dotenv"
pip install python-dotenv
```

```python title="python-dotenv usage" linenums="1"
from dotenv import load_dotenv
import os

load_dotenv()  # Reads .env from the current directory

api_key = os.environ["API_KEY"]
```

That's the full integration. `load_dotenv()` loads the file and populates `os.environ`. The rest of your code reads from `os.environ` normally — it doesn't need to know about `python-dotenv`.

---

## Grouping Credentials Into a Config Object

As scripts grow, passing individual environment variables through function arguments gets messy. Group them:

```python title="Config object from environment" linenums="1"
import os
import sys
from dataclasses import dataclass


@dataclass
class Config:  # (1)!
    api_key: str
    db_host: str
    db_password: str
    log_level: str = "INFO"

    @classmethod
    def from_env(cls):
        """Load config from environment. Exits if required vars are missing."""
        missing = []
        for field in ["API_KEY", "DB_HOST", "DB_PASSWORD"]:
            if not os.environ.get(field):
                missing.append(field)
        if missing:
            print(f"✗ Missing: {', '.join(missing)}")
            sys.exit(1)

        return cls(
            api_key=os.environ["API_KEY"],
            db_host=os.environ["DB_HOST"],
            db_password=os.environ["DB_PASSWORD"],
            log_level=os.environ.get("LOG_LEVEL", "INFO"),
        )


config = Config.from_env()
print(f"Connecting to {config.db_host} as configured")
# Not: print(f"Password: {config.db_password}")  ← never
```

1. `@dataclass` generates `__init__`, `__repr__`, and comparison methods automatically. `config.api_key` instead of `os.environ["API_KEY"]` scattered through the codebase.

Now your functions take a `config` object. Credentials live in one place, are validated once at startup, and are never passed as strings through function arguments.

---

## What Not to Log

```python title="❌ Logging secrets" linenums="1"
print(f"Connecting with key: {api_key}")      # ← in CI logs forever
print(f"Config: {vars(config)}")              # ← dumps all fields including password
import logging
logging.debug("Config loaded: %s", config)   # ← same problem
```

```python title="✅ Log the intent, not the value" linenums="1"
print(f"API key loaded ({len(api_key)} chars)")
print(f"Connecting to {config.db_host}")
print(f"Config loaded: {len(vars(config))} variables")
```

If your `@dataclass` has a `__repr__`, override it to mask sensitive fields:

```python title="Masking secrets in repr" linenums="1"
@dataclass
class Config:
    api_key: str
    db_password: str
    db_host: str

    def __repr__(self):
        return f"Config(db_host={self.db_host!r}, api_key='***', db_password='***')"
```

---

## Practice Exercises

??? question "Exercise 1: Validate and report"
    Write a `check_env()` function that takes a list of required variable names and a list of optional variable names. It should print a summary of which required vars are set, which are missing, and which optional vars were found. Exit with a non-zero code only if required vars are missing.

    ??? tip "Answer"
        ```python title="check_env with optional vars" linenums="1"
        def check_env(required, optional=None):
            optional = optional or []
            missing = [v for v in required if not os.environ.get(v)]
            found_optional = [v for v in optional if os.environ.get(v)]

            for var in required:
                status = "✓" if os.environ.get(var) else "✗ MISSING"
                print(f"  {status}  {var}")
            for var in optional:
                status = "✓" if os.environ.get(var) else "  (not set)"
                print(f"  {status}  {var} (optional)")

            if missing:
                sys.exit(1)
        ```

??? question "Exercise 2: Mask a secret in output"
    Write a `mask(value)` function that returns the last 4 characters of a string with everything before it replaced by `*`. For example, `mask("sk-abc123def456")` returns `"**********e456"`. This is useful for confirming a key was loaded without revealing it.

    ??? tip "Answer"
        ```python title="mask() function" linenums="1"
        def mask(value, show=4):
            if not value or len(value) <= show:
                return "***"
            return "*" * (len(value) - show) + value[-show:]

        print(f"API key: {mask(api_key)}")
        # API key: **********e456
        ```

---

## Quick Recap

| Pattern | When to Use |
|:--------|:------------|
| `os.environ["VAR"]` | Required variable — fail fast if missing |
| `os.environ.get("VAR")` | Optional variable — handle `None` yourself |
| `os.environ.get("VAR", "default")` | Variable with a sensible fallback |
| `load_dotenv()` | Local development with a `.env` file |
| `@dataclass` + `from_env()` | Group credentials for scripts with multiple vars |
| Fail-fast validation at startup | Surface missing credentials immediately |

---

## What's Next

- **[Working with YAML](yaml.md)** — Reading, modifying, and generating Kubernetes manifests and other YAML configs

## Further Reading

### Official Documentation
- [`os.environ`](https://docs.python.org/3/library/os.html#os.environ) — The environment variable mapping
- [`dataclasses`](https://docs.python.org/3/library/dataclasses.html) — `@dataclass` decorator reference

### Libraries
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — The standard `.env` file library
- [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) — For larger projects that need type validation and settings management
