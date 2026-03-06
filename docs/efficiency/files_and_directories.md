---
title: Files and Paths in Python
description: "Python's pathlib for filesystem operations — reading, writing, globbing, and directory work that replaces find, ls, cp, and mv in your scripts."
---

# Files and Paths

Your Bash scripts are full of file operations. `find /var/log -name "*.log" -mtime -1`. `cp -r
/etc/nginx /backup/nginx-$(date +%Y%m%d)`. `grep -r "ERROR" /var/log/app/ > errors.txt`. `mkdir
-p /opt/app/config/prod`.

Python handles all of this — more reliably, with better error handling, and without spawning
subprocesses for basic filesystem work.

## Coming from Bash

```bash title="Common Bash File Operations" linenums="1"
# List files
ls -la /var/log/*.log

# Find files recursively
find /etc -name "*.conf" -type f

# Read a file
cat /etc/hosts
content=$(< /etc/hosts)

# Write a file
echo "new content" > /tmp/output.txt
cat >> /tmp/output.txt << EOF
more content
EOF

# Copy and move
cp -r /etc/nginx /backup/nginx
mv /tmp/old.conf /etc/app.conf

# Check existence
if [[ -f /etc/config.conf ]]; then echo "exists"; fi
if [[ -d /var/log/app ]]; then echo "dir exists"; fi

# Create directories
mkdir -p /opt/app/config/prod
```

```python title="Python Equivalents (pathlib)" linenums="1"
from pathlib import Path

# List files
for f in Path("/var/log").glob("*.log"):
    print(f)

# Find files recursively
for conf in Path("/etc").rglob("*.conf"):
    print(conf)

# Read a file
content = Path("/etc/hosts").read_text()

# Write a file
Path("/tmp/output.txt").write_text("new content\n")

# Copy and move (shutil for directories)
import shutil
shutil.copytree("/etc/nginx", "/backup/nginx")
Path("/tmp/old.conf").rename("/etc/app.conf")

# Check existence
if Path("/etc/config.conf").is_file(): print("exists")
if Path("/var/log/app").is_dir(): print("dir exists")

# Create directories
Path("/opt/app/config/prod").mkdir(parents=True, exist_ok=True)
```

The key shift: instead of thinking in terms of command-line tools, you work with `Path` objects
that have methods for every operation you need.

## The pathlib.Path Object

`pathlib`, introduced in Python 3.4, is the modern API for filesystem operations. A `Path` object
represents a path — file or directory — and provides methods for everything you'd reach for in Bash.

```python title="Creating Path Objects" linenums="1"
from pathlib import Path

# Absolute path
config = Path("/etc/nginx/nginx.conf")

# Relative path (resolved from current working directory)
log_dir = Path("logs")

# Home directory (~ expansion)
home = Path.home()           # (1)!
dotfile = home / ".bashrc"   # (2)!

# Current working directory
cwd = Path.cwd()
```

1. `Path.home()` returns the current user's home directory — no `$HOME` needed
2. The `/` operator joins path components — cleaner than string concatenation

### Path Attributes and Properties

```python title="Inspecting Paths" linenums="1"
from pathlib import Path

p = Path("/var/log/nginx/access.log")

print(p.name)       # (1)!
print(p.stem)       # (2)!
print(p.suffix)     # (3)!
print(p.parent)     # (4)!
print(p.parts)      # (5)!
```

1. `access.log` — filename with extension
2. `access` — filename without extension
3. `.log` — the extension
4. `/var/log/nginx` — parent directory as a Path
5. `('/', 'var', 'log', 'nginx', 'access.log')` — all components as a tuple

### Checking Existence and Type

```python title="Existence Checks" linenums="1"
from pathlib import Path

p = Path("/etc/nginx/nginx.conf")

p.exists()    # (1)!
p.is_file()   # (2)!
p.is_dir()    # (3)!
p.is_symlink()
```

1. Returns `True` if the path exists (file or directory)
2. `True` only if it's a regular file
3. `True` only if it's a directory

## Reading Files

### The Context Manager Pattern

Always use `with open()` to read files. It ensures the file is closed even if an exception occurs
— the Python equivalent of Bash's `trap` for cleanup:

```python title="Reading a File" linenums="1"
with open("/etc/hosts") as f:       # (1)!
    content = f.read()              # Read entire file as string

# Line by line (memory-efficient for large files)
with open("/var/log/syslog") as f:
    for line in f:                  # (2)!
        if "ERROR" in line:
            print(line.rstrip())
```

1. `with` opens the file and automatically closes it when the block exits — no `finally` needed
2. Iterating over a file object reads one line at a time — efficient for large log files

### pathlib Shortcuts

For smaller files, `pathlib` offers one-liners:

```python title="pathlib Read Methods" linenums="1"
from pathlib import Path

# Read entire file as string
content = Path("/etc/nginx/nginx.conf").read_text()    # (1)!

# Read as a list of lines
lines = Path("/etc/hosts").read_text().splitlines()    # (2)!

# Read binary files
data = Path("/var/run/app.pid").read_bytes()
```

1. `read_text()` opens, reads, and closes the file — handles encoding automatically
2. `.splitlines()` splits on `\n` and strips the newline — cleaner than `.split("\n")`

### Parsing Line by Line

A common pattern: read a config-style file and parse each line:

```python title="Parsing /etc/hosts" linenums="1"
from pathlib import Path

hosts = {}
for line in Path("/etc/hosts").read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):  # (1)!
        continue
    parts = line.split()
    ip = parts[0]
    for hostname in parts[1:]:
        hosts[hostname] = ip

print(hosts.get("localhost"))  # 127.0.0.1
```

1. Skip blank lines and comments — the same logic you'd use in `awk '/^[^#]/'`

## Writing Files

```python title="Writing Files" linenums="1"
from pathlib import Path

# Write (overwrites if exists)
Path("/tmp/output.txt").write_text("new content\n")

# Append to a file
with open("/tmp/output.txt", "a") as f:   # (1)!
    f.write("appended line\n")

# Write multiple lines
lines = ["line 1", "line 2", "line 3"]
Path("/tmp/output.txt").write_text("\n".join(lines) + "\n")
```

1. Mode `"a"` appends; `"w"` overwrites; `"r"` is the default (read-only)

## Finding Files

### glob() and rglob()

```python title="Finding Files" linenums="1"
from pathlib import Path

# Non-recursive — like ls /var/log/*.log
for log in Path("/var/log").glob("*.log"):
    print(log)

# Recursive — like find /etc -name "*.conf"
for conf in Path("/etc").rglob("*.conf"):
    print(conf)

# Pattern matching — find all Python files in a project
for py_file in Path(".").rglob("*.py"):
    print(py_file)

# Collect as a sorted list
log_files = sorted(Path("/var/log").glob("*.log"))
```

### Filtering Results

```python title="Filtering with Conditions" linenums="1"
from pathlib import Path
import time

log_dir = Path("/var/log")
one_day_ago = time.time() - 86400

# Modified in the last 24 hours (like find -mtime -1)
recent_logs = [
    f for f in log_dir.glob("*.log")
    if f.stat().st_mtime > one_day_ago   # (1)!
]

# Files larger than 100MB
large_files = [
    f for f in log_dir.rglob("*")
    if f.is_file() and f.stat().st_size > 100 * 1024 * 1024
]
```

1. `f.stat().st_mtime` is the modification time as a Unix timestamp — same as Bash's `find -newer`

## Directory Operations

```python title="Directory Operations" linenums="1"
from pathlib import Path

# Create directory (like mkdir -p)
Path("/opt/app/config/prod").mkdir(parents=True, exist_ok=True)  # (1)!

# List directory contents (like ls)
for item in Path("/etc/nginx").iterdir():
    if item.is_file():
        print(f"FILE: {item.name}")
    elif item.is_dir():
        print(f"DIR:  {item.name}/")

# Get file info (like ls -la)
p = Path("/etc/nginx/nginx.conf")
stat = p.stat()
print(f"Size: {stat.st_size} bytes")
print(f"Modified: {stat.st_mtime}")
```

1. `parents=True` creates intermediate directories; `exist_ok=True` doesn't error if it already exists — equivalent to `mkdir -p`

## Copying, Moving, and Deleting

Python's `shutil` module handles operations that go beyond a single path:

```python title="shutil Operations" linenums="1"
import shutil
from pathlib import Path

# Copy a file
shutil.copy2("/etc/nginx/nginx.conf", "/backup/nginx.conf")  # (1)!

# Copy a directory tree (like cp -r)
shutil.copytree("/etc/nginx", "/backup/nginx-20240115")

# Move (like mv)
Path("/tmp/new.conf").rename("/etc/app/new.conf")            # (2)!
shutil.move("/tmp/new.conf", "/etc/app/")                    # (3)!

# Delete a file
Path("/tmp/tempfile.txt").unlink()

# Delete a directory tree (like rm -rf — be careful!)
shutil.rmtree("/tmp/build")
```

1. `copy2` preserves metadata (timestamps, permissions); `copy` preserves only permissions
2. `rename()` works within the same filesystem; fails across filesystems
3. `shutil.move()` works across filesystems — safer for general use

!!! warning "shutil.rmtree is rm -rf"

    `shutil.rmtree()` recursively deletes everything without confirmation. There's no
    trash/recycle bin. Use it carefully, especially with user-provided paths.

## Practical Patterns

### Backup Before Modifying

```python title="Backup Pattern" linenums="1"
from pathlib import Path
import shutil
from datetime import datetime

def backup_config(config_path: str) -> Path:
    """Create a dated backup before modifying a config file."""
    src = Path(config_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = src.parent / f"{src.stem}.{timestamp}.bak"
    shutil.copy2(src, backup)
    print(f"Backed up to {backup}")
    return backup

backup_config("/etc/nginx/nginx.conf")
```

### Process All Files Matching a Pattern

```python title="Process Log Files" linenums="1"
from pathlib import Path

error_count = 0
log_dir = Path("/var/log/app")

for log_file in sorted(log_dir.glob("*.log")):
    for line in log_file.read_text().splitlines():
        if "ERROR" in line:
            error_count += 1
            print(f"{log_file.name}: {line}")

print(f"\nTotal errors: {error_count}")
```

### Safe Temp Files

```python title="Using tempfile" linenums="1"
import tempfile
from pathlib import Path

# Create a named temp file (deleted when closed)
with tempfile.NamedTemporaryFile(mode="w", suffix=".conf", delete=False) as tmp:
    tmp.write("[section]\nkey = value\n")
    tmp_path = Path(tmp.name)

# Process it
print(tmp_path.read_text())

# Clean up explicitly
tmp_path.unlink()
```

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **`Path` object** | Represents any filesystem path; has methods for common operations |
| **`/` operator** | Join path components: `Path("/etc") / "nginx" / "nginx.conf"` |
| **`read_text()`** | Read entire file as string — handles encoding automatically |
| **`write_text()`** | Write a string to a file (overwrites) |
| **`glob()`** | Non-recursive pattern matching — like `ls *.log` |
| **`rglob()`** | Recursive pattern matching — like `find -name "*.log"` |
| **`mkdir(parents=True, exist_ok=True)`** | Create directory tree — equivalent to `mkdir -p` |
| **`with open() as f:`** | Always use context manager — ensures file is closed |
| **`shutil`** | Copy/move/delete trees; use for cross-filesystem moves and recursive copies |
| **`stat()`** | File metadata: size, timestamps, permissions |

## Practice Problems

??? question "Practice Problem 1: Count Log Errors by File"

    Write a function that takes a directory path and returns a dictionary mapping each
    `.log` filename to the number of lines containing "ERROR".

    ??? tip "Answer"

        ```python title="Count Errors by File" linenums="1"
        from pathlib import Path

        def count_errors(log_dir: str) -> dict:
            results = {}
            for log_file in Path(log_dir).glob("*.log"):
                error_lines = [
                    line for line in log_file.read_text().splitlines()
                    if "ERROR" in line
                ]
                results[log_file.name] = len(error_lines)  # (1)!
            return results

        errors = count_errors("/var/log/app")
        for filename, count in sorted(errors.items()):
            print(f"{filename}: {count} errors")
        ```

        1. `log_file.name` gives just the filename without the parent path

??? question "Practice Problem 2: Rotate a Config File"

    Write a function that:
    1. Creates a timestamped backup of a config file
    2. Writes new content to the original path
    3. Returns the backup path

    ??? tip "Answer"

        ```python title="Config Rotation" linenums="1"
        from pathlib import Path
        import shutil
        from datetime import datetime

        def rotate_config(config_path: str, new_content: str) -> Path:
            src = Path(config_path)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup = src.with_suffix(f".{timestamp}.bak")  # (1)!

            shutil.copy2(src, backup)
            src.write_text(new_content)
            return backup

        backup = rotate_config("/etc/app/config.ini", "[new]\nkey = value\n")
        print(f"Old config saved to: {backup}")
        ```

        1. `with_suffix()` changes the extension — here we use it to add a timestamp suffix

??? question "Practice Problem 3: Find Large Files"

    Write a one-liner (or short function) to find all files in `/var/log` larger than 50MB,
    returning them sorted by size descending.

    ??? tip "Answer"

        ```python title="Find Large Files" linenums="1"
        from pathlib import Path

        large_files = sorted(
            (f for f in Path("/var/log").rglob("*") if f.is_file()),
            key=lambda f: f.stat().st_size,
            reverse=True
        )

        for f in large_files:
            size_mb = f.stat().st_size / (1024 * 1024)
            if size_mb > 50:
                print(f"{size_mb:.1f}MB  {f}")
        ```

??? question "Practice Problem 4: Parse Key=Value Config"

    Write a function that reads a simple `key=value` config file (one per line, `#` for
    comments) and returns a dictionary.

    ??? tip "Answer"

        ```python title="Parse Key=Value Config" linenums="1"
        from pathlib import Path

        def parse_config(path: str) -> dict:
            config = {}
            for line in Path(path).read_text().splitlines():
                line = line.strip()
                if not line or line.startswith("#"):  # (1)!
                    continue
                if "=" in line:
                    key, _, value = line.partition("=")  # (2)!
                    config[key.strip()] = value.strip()
            return config

        # Example file:
        # # Database config
        # DB_HOST=db01.prod
        # DB_PORT=5432
        config = parse_config("/etc/app/config.env")
        print(config)
        # {'DB_HOST': 'db01.prod', 'DB_PORT': '5432'}
        ```

        1. Skip blank lines and comments — same as `grep -v '^#' | grep -v '^$'`
        2. `partition("=")` splits on the first `=` only — handles values that contain `=`

## Further Reading

### On This Site

- [**Running Commands**](../essentials/running_commands.md) — when you do need to call `find`, `rsync`, or other tools from Python
- [**Error Handling**](../essentials/error_handling.md) — handling `FileNotFoundError`, `PermissionError`, and other filesystem exceptions

### Official Documentation

- [**pathlib — Object-oriented filesystem paths**](https://docs.python.org/3/library/pathlib.html) — complete reference
- [**shutil — High-level file operations**](https://docs.python.org/3/library/shutil.html) — copy, move, archive
- [**tempfile — Temporary files and directories**](https://docs.python.org/3/library/tempfile.html) — safe temp file creation

### External Resources

- [**Python Pathlib Cheatsheet**](https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module) — mapping from old `os.path` to `pathlib`

---

`pathlib` replaced the old `os.path` approach in Python 3.4 and should be your default for any
filesystem work. It's more readable, more object-oriented, and handles Windows paths correctly if
your scripts ever need to be cross-platform. Use `shutil` for operations that involve copying trees
or moving across filesystems. Reach for `subprocess` only when you genuinely need an external tool
that Python can't replace.
