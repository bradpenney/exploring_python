---
title: Environment Variables and Config in Python
description: "Reading environment variables with os.environ, loading .env files, parsing INI and JSON config, and managing configuration safely in Python scripts."
---

# Environment Variables and Config

Bash scripts read config the same way as everything else: environment variables, positional
arguments, or text files parsed with `awk` and `sed`. It works, but config scattered across
`/etc/default/myapp`, `~/.myapprc`, environment variables, and `--flags` is hard to reason about.

Python has standard library modules for every config format you'll encounter — and a clear
pattern for choosing which one to use.

## Coming from Bash

```bash title="Bash Configuration" linenums="1"
# Environment variables
DB_HOST="${DB_HOST:-localhost}"     # With default
: "${API_KEY:?API_KEY must be set}" # Exit if not set

# Source a file of exports
source /etc/app/config
. ~/.appenv

# Parse key=value file
while IFS='=' read -r key value; do
    export "$key=$value"
done < /etc/app/config.env
```

```python title="Python Configuration" linenums="1"
import os
from pathlib import Path

# Environment variables
db_host = os.environ.get("DB_HOST", "localhost")         # With default

# Exit if not set
api_key = os.environ.get("API_KEY")
if api_key is None:
    raise SystemExit("Error: API_KEY must be set")

# Parse key=value file (or use python-dotenv for .env files)
config = {}
for line in Path("/etc/app/config.env").read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        key, _, value = line.partition("=")
        config[key.strip()] = value.strip()
```

Key differences:

| Bash | Python |
|:-----|:-------|
| `${VAR:-default}` | `os.environ.get("VAR", "default")` |
| `: "${VAR:?error}"` | Check and `sys.exit()` manually |
| `source /etc/app/config` | Parse the file yourself, or use `python-dotenv` |
| `export KEY=value` | Set with `os.environ["KEY"] = "value"` |

## Reading Environment Variables

### os.environ

`os.environ` is a dictionary-like object containing all environment variables:

```python title="os.environ Basics" linenums="1"
import os

# Read a variable (raises KeyError if missing)
path = os.environ["PATH"]

# Read with a default (preferred for optional variables)
debug = os.environ.get("DEBUG", "false")           # (1)!
log_level = os.environ.get("LOG_LEVEL", "INFO")

# Check if a variable is set
if "API_KEY" in os.environ:
    api_key = os.environ["API_KEY"]

# Get all environment variables
for key, value in os.environ.items():
    print(f"{key}={value}")
```

1. `.get()` never raises — returns the default if the variable is missing

### Validating Required Variables

For scripts with required environment variables, validate them upfront:

```python title="Validate Required Variables" linenums="1"
import os
import sys

REQUIRED_VARS = ["DB_HOST", "DB_PORT", "DB_NAME", "API_KEY"]

missing = [var for var in REQUIRED_VARS if var not in os.environ]
if missing:
    sys.exit(f"Error: missing required environment variables: {', '.join(missing)}")

# Now safe to use
db_host = os.environ["DB_HOST"]
db_port = int(os.environ["DB_PORT"])     # (1)!
db_name = os.environ["DB_NAME"]
api_key = os.environ["API_KEY"]
```

1. Environment variables are always strings — convert to `int`, `bool`, etc. as needed

### Type Conversion from Environment Variables

```python title="Converting Environment Variable Types" linenums="1"
import os

# String → int
port = int(os.environ.get("PORT", "8080"))

# String → bool (environment variables don't have native booleans)
debug_str = os.environ.get("DEBUG", "false").lower()
debug = debug_str in ("true", "1", "yes", "on")          # (1)!

# String → list (comma-separated)
allowed_hosts_str = os.environ.get("ALLOWED_HOSTS", "localhost")
allowed_hosts = [h.strip() for h in allowed_hosts_str.split(",")]
```

1. No built-in `bool("false")` that works intuitively — `bool("false")` returns `True`
   because the string is non-empty. Parse explicitly.

### Setting Environment Variables

```python title="Setting Variables for Subprocesses" linenums="1"
import os
import subprocess

# Set a variable in the current process (affects child processes)
os.environ["KUBECONFIG"] = "/home/deploy/.kube/config"

# Pass a modified environment to a subprocess (without polluting the current env)
env = os.environ.copy()
env["KUBECONFIG"] = "/home/deploy/.kube/config"

result = subprocess.run(
    ["kubectl", "get", "pods"],
    env=env,                              # (1)!
    capture_output=True, text=True
)
```

1. Pass a custom environment dict to `subprocess.run()` — isolated, doesn't affect other calls

## Loading .env Files

Production environments use proper secret management, but development and CI/CD commonly use
`.env` files. The `python-dotenv` library loads them into `os.environ`:

```bash title="Install python-dotenv"
pip install python-dotenv
```

```ini title=".env file"
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myapp

# API Keys (never commit this file!)
API_KEY=sk-abc123
WEBHOOK_SECRET=whsec_xyz789
```

```python title="Loading .env" linenums="1"
from dotenv import load_dotenv
import os

load_dotenv()                            # (1)!

db_host = os.environ.get("DB_HOST", "localhost")
api_key = os.environ["API_KEY"]
```

1. `load_dotenv()` reads `.env` from the current directory and sets variables in `os.environ`.
   Variables already set in the environment are NOT overridden by default.

### Finding .env in Different Locations

```python title="Explicit .env Path" linenums="1"
from dotenv import load_dotenv
from pathlib import Path

# Load from a specific path
env_file = Path(__file__).parent.parent / ".env"
load_dotenv(env_file)

# Override=True: .env values override existing env vars
load_dotenv(override=True)
```

## Parsing INI/Config Files

The standard library's `configparser` handles `.ini` style config — the format used by many
Linux system configs and Python tooling:

```ini title="app.conf"
[database]
host = db01.prod
port = 5432
name = myapp

[server]
host = 0.0.0.0
port = 8080
workers = 4
debug = false
```

```python title="Reading INI Config" linenums="1"
import configparser

config = configparser.ConfigParser()
config.read("/etc/app/app.conf")          # (1)!

# Access sections and keys
db_host = config["database"]["host"]      # (2)!
db_port = config["database"].getint("port")        # (3)!
debug = config["server"].getboolean("debug")       # (4)!

# Check if a section/key exists
if "database" in config:
    print(config["database"].get("password", ""))  # (5)!
```

1. `config.read()` is silent if the file doesn't exist — use `config.read_file()` to raise on missing
2. Access like a nested dict: `config[section][key]`
3. `.getint()` returns an integer — handles the type conversion
4. `.getboolean()` understands `true`/`false`, `yes`/`no`, `1`/`0`
5. `.get()` with a default — never raises `KeyError`

### Fallback Values

```python title="ConfigParser with Defaults" linenums="1"
import configparser

# Defaults apply to all sections
config = configparser.ConfigParser(defaults={"debug": "false", "workers": "2"})
config.read("/etc/app/app.conf")

workers = config["server"].getint("workers")   # Falls back to 2 if not in file
```

## Reading JSON Config

```python title="JSON Config Files" linenums="1"
import json
from pathlib import Path

config = json.loads(Path("/etc/app/config.json").read_text())  # (1)!

db_host = config["database"]["host"]
allowed_users = config.get("allowed_users", [])     # (2)!
```

1. `json.loads()` parses a string; `json.load(file_object)` parses directly from a file handle
2. JSON becomes native Python types — dict, list, str, int, float, bool, None

## Reading YAML Config

YAML is everywhere in infrastructure work — Kubernetes manifests, Ansible playbooks,
Docker Compose files, CI/CD pipelines. Install `PyYAML`:

```bash
pip install pyyaml
```

```yaml title="config.yaml"
database:
  host: db01.prod
  port: 5432
  name: myapp

servers:
  - web01.prod
  - web02.prod

feature_flags:
  enable_cache: true
  debug_mode: false
```

```python title="Reading YAML" linenums="1"
import yaml
from pathlib import Path

config = yaml.safe_load(Path("/etc/app/config.yaml").read_text())  # (1)!

db_host = config["database"]["host"]
servers = config["servers"]                        # Returns a list
enable_cache = config["feature_flags"]["enable_cache"]

for server in servers:
    print(f"Checking {server}...")
```

1. Use `yaml.safe_load()`, not `yaml.load()` — `safe_load` prevents arbitrary code execution
   from malicious YAML

## A Complete Configuration Pattern

A common pattern for production scripts: check env vars first, fall back to a config file,
then fall back to hardcoded defaults:

```python title="Layered Configuration" linenums="1"
import os
import json
from pathlib import Path

def load_config() -> dict:
    """Load config with env var → file → defaults priority."""

    # Defaults
    config = {
        "db_host": "localhost",
        "db_port": 5432,
        "log_level": "INFO",
    }

    # Override from config file if present
    config_file = Path(os.environ.get("CONFIG_FILE", "/etc/app/config.json"))
    if config_file.exists():
        file_config = json.loads(config_file.read_text())
        config.update(file_config)                # (1)!

    # Environment variables take highest priority
    if "DB_HOST" in os.environ:
        config["db_host"] = os.environ["DB_HOST"]  # (2)!
    if "DB_PORT" in os.environ:
        config["db_port"] = int(os.environ["DB_PORT"])
    if "LOG_LEVEL" in os.environ:
        config["log_level"] = os.environ["LOG_LEVEL"]

    return config
```

1. File values override defaults
2. Environment variables override file values — the standard twelve-factor app pattern

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`os.environ.get()`** | Read env var with optional default — never raises |
| **`os.environ["KEY"]`** | Read env var — raises `KeyError` if missing |
| **Type conversion** | Env vars are always strings — convert to `int`, `bool` explicitly |
| **`python-dotenv`** | Load `.env` files into `os.environ` for development |
| **`configparser`** | INI-style config — `.getint()`, `.getboolean()` for type conversion |
| **`json` module** | JSON config — becomes native Python types automatically |
| **`yaml.safe_load()`** | YAML config — always use `safe_load`, never `load` |
| **Layered config** | Defaults → file → env vars; env vars win |

## Practice Problems

??? question "Practice Problem 1: Required Variable Check"

    Write a function `require_env(*names)` that takes variable names, checks all are set,
    and raises `SystemExit` with a helpful message listing any missing ones.

    ??? tip "Answer"

        ```python title="Require Environment Variables" linenums="1"
        import os
        import sys

        def require_env(*names: str) -> dict:
            """Return dict of required env vars, or exit if any are missing."""
            missing = [n for n in names if n not in os.environ]
            if missing:
                sys.exit(f"Missing required env vars: {', '.join(missing)}")
            return {n: os.environ[n] for n in names}  # (1)!

        config = require_env("DB_HOST", "DB_PORT", "API_KEY")
        db_host = config["DB_HOST"]
        ```

        1. Returns a dict of just the requested variables — convenient for passing around

??? question "Practice Problem 2: Parse a Boolean Environment Variable"

    Environment variables are strings, not booleans. Write a helper `get_bool_env(name, default=False)`
    that correctly handles `"true"`, `"1"`, `"yes"`, `"false"`, `"0"`, `"no"`.

    ??? tip "Answer"

        ```python title="Boolean Env Var" linenums="1"
        import os

        def get_bool_env(name: str, default: bool = False) -> bool:
            value = os.environ.get(name)
            if value is None:
                return default
            return value.lower() in ("true", "1", "yes", "on")  # (1)!

        debug = get_bool_env("DEBUG")
        verbose = get_bool_env("VERBOSE", default=True)
        ```

        1. Explicit string comparison is the only safe way — `bool("false")` returns `True`
           because non-empty strings are truthy

??? question "Practice Problem 3: Load JSON Config with Defaults"

    Write a function that loads a JSON config file, merges it with provided defaults, and
    returns the result. If the file doesn't exist, return just the defaults.

    ??? tip "Answer"

        ```python title="Load Config with Defaults" linenums="1"
        import json
        from pathlib import Path

        def load_json_config(path: str, defaults: dict) -> dict:
            config = defaults.copy()                      # (1)!
            config_path = Path(path)

            if config_path.exists():
                file_config = json.loads(config_path.read_text())
                config.update(file_config)               # (2)!

            return config

        DEFAULTS = {"host": "localhost", "port": 8080, "debug": False}
        config = load_json_config("/etc/app/config.json", DEFAULTS)
        ```

        1. `.copy()` prevents mutating the original defaults dict
        2. File values override defaults; missing file keys fall back to defaults

??? question "Practice Problem 4: Which Config Format?"

    Match each scenario to the best config format or approach:

    1. Storing a database password for a Kubernetes deployment
    2. A Python script's dev settings that shouldn't be committed to git
    3. A complex nested config with lists of servers and feature flags
    4. A simple Linux-style config that admins edit directly on the server

    ??? tip "Answer"

        1. **Kubernetes Secret / HashiCorp Vault** — never store passwords in files in the container image; inject as environment variables
        2. **`.env` file + `python-dotenv`** — add `.env` to `.gitignore`; team shares a `.env.example`
        3. **YAML** — human-readable, supports nested structures and lists natively
        4. **INI (`configparser`)** — familiar to Linux admins, simple syntax, standard library

## Further Reading

### On This Site

- [**Error Handling**](../essentials/error_handling.md) — handling `FileNotFoundError` when config files are missing
- [**Files and Directories**](files_and_directories.md) — reading config files with `pathlib`

### Official Documentation

- [**os.environ**](https://docs.python.org/3/library/os.html#os.environ) — environment variable access
- [**configparser**](https://docs.python.org/3/library/configparser.html) — INI file parsing
- [**json module**](https://docs.python.org/3/library/json.html) — JSON encoding and decoding

### External Resources

- [**python-dotenv**](https://pypi.org/project/python-dotenv/) — `.env` file loading
- [**PyYAML**](https://pyyaml.org/wiki/PyYAMLDocumentation) — YAML parsing
- [**The Twelve-Factor App: Config**](https://12factor.net/config) — the standard for config management in deployed apps

---

Environment variables are the right layer for secrets and environment-specific values. Config
files are the right layer for structured, non-secret configuration. Python's standard library
handles both. The pattern: validate env vars at startup, load config files with defaults, and
let env vars override everything.
