---
title: Working with JSON in Python
description: "Replace curl | jq pipelines with Python's built-in json module. Parse API responses, navigate nested data, and handle errors without shell hackery."
---

# Working with JSON

Your `curl | jq` pipeline broke again. The API added a new wrapper object, a field got renamed, or it returned an error body instead of the expected array and `jq` silently produced nothing. You added another `// empty` guard. Then another. Now the pipeline is three lines of `jq` filters nobody remembers how to read.

Python's `json` module is part of the standard library — nothing to install. Once JSON is parsed, you navigate it with normal Python syntax. No filter language to learn. Errors are explicit. And when you need to handle pagination, retries, or auth, you're writing Python — not `jq` guards bolted onto a `curl` command.

## The `curl | jq` Pattern vs Python

=== ":simple-gnubash: Bash"

    ```bash title="Querying an API with curl and jq" linenums="1"
    # Get running pod names
    curl -s https://api.example.com/pods \
      | jq -r '.items[] | select(.status.phase == "Running") | .metadata.name'

    # Extract a nested field with a fallback
    curl -s https://api.example.com/pods \
      | jq -r '.items[0].metadata.labels.app // "unknown"'
    ```

    Works until: the API returns a 401 (jq sees HTML, outputs nothing), `.items` is null (jq errors), or you need to do something with the names beyond printing them.

=== ":material-language-python: Python"

    ```python title="Querying an API with urllib and json" linenums="1"
    import json
    import urllib.request

    with urllib.request.urlopen("https://api.example.com/pods") as resp:
        data = json.loads(resp.read())  # (1)!

    # Same filter logic — just Python
    running = [
        pod["metadata"]["name"]
        for pod in data["items"]
        if pod["status"]["phase"] == "Running"
    ]

    # Safe access with .get() — returns None instead of crashing
    app_label = data["items"][0]["metadata"].get("labels", {}).get("app", "unknown")  # (2)!
    ```

    1. `json.loads()` parses the response bytes into a Python dict — one call, no filter syntax
    2. `.get(key, default)` is the Python equivalent of `jq`'s `// "fallback"` — returns the default if the key is missing

The names are now a Python list. You can sort them, write them to a file, pass them to another function, or check their count — without another pipe.

## Parsing JSON

### From a String

```python title="json.loads() — Parse a String" linenums="1"
import json

# From a command that returned JSON (e.g. kubectl, aws cli)
json_str = '{"hostname": "web01", "status": "running", "cpu_pct": 72}'
data = json.loads(json_str)  # (1)!

print(data["hostname"])          # web01
print(data["cpu_pct"])           # 72  — integer, not string
print(type(data["cpu_pct"]))     # <class 'int'>
```

1. `json.loads()` — "load string". JSON types map directly to Python: objects become `dict`, arrays become `list`, numbers become `int` or `float`, `true`/`false` become `True`/`False`, `null` becomes `None`

### From a File

```python title="json.load() — Read a File" linenums="1"
import json
from pathlib import Path

# Option 1: pathlib (clean, one-liner)
config = json.loads(Path("/etc/myapp/config.json").read_text())

# Option 2: file object (better for large files)
with open("/etc/myapp/config.json") as f:
    config = json.load(f)  # (1)!
```

1. `json.load(f)` reads directly from a file object without loading the whole file into memory first — useful for large JSON files

### From a subprocess Command

```python title="Parse JSON from a Command" linenums="1"
import json
import subprocess

# kubectl, aws cli, and many other tools support -o json or --output json
result = subprocess.run(
    ["kubectl", "get", "pods", "-o", "json", "-n", "production"],
    capture_output=True, text=True, check=True
)
pods = json.loads(result.stdout)  # (1)!

running = [
    p["metadata"]["name"]
    for p in pods["items"]
    if p["status"].get("phase") == "Running"
]
print(f"Running pods: {len(running)}")
```

1. `result.stdout` is a string — feed it directly to `json.loads()`. This pattern replaces `kubectl ... | jq ...` entirely.

## Navigating Nested JSON

The rule: JSON objects are Python `dict`s, JSON arrays are Python `list`s. Navigate with `["key"]` and `[index]`.

```python title="Navigating a Kubernetes Pod Object" linenums="1"
import json

pod_json = '''
{
    "metadata": {"name": "web-abc12", "namespace": "prod",
                 "labels": {"app": "web", "version": "v2"}},
    "status": {
        "phase": "Running",
        "conditions": [
            {"type": "Ready", "status": "True"},
            {"type": "PodScheduled", "status": "True"}
        ],
        "podIP": "10.0.0.42"
    }
}
'''
pod = json.loads(pod_json)

# Direct access — raises KeyError if missing
name = pod["metadata"]["name"]              # "web-abc12"
phase = pod["status"]["phase"]              # "Running"

# Safe access — returns None (or your default) if missing
ip = pod["status"].get("podIP")            # "10.0.0.42"
node = pod["status"].get("hostIP")         # None — key doesn't exist
region = pod["metadata"].get("labels", {}).get("region", "unknown")  # (1)!

# Iterate over an array
for condition in pod["status"]["conditions"]:
    print(f'{condition["type"]}: {condition["status"]}')

# Find the first match in an array — replaces jq's select()
ready = next(
    (c for c in pod["status"]["conditions"] if c["type"] == "Ready"),
    None  # (2)!
)
if ready and ready["status"] == "True":
    print("Pod is ready")
```

1. Chain `.get()` calls for deeply nested optional fields — each level returns an empty dict `{}` if missing rather than crashing
2. `next(generator, default)` returns the first match or the default — the Python equivalent of `jq '.[] | select(.type=="Ready") | first'`

## Writing JSON

```python title="json.dumps() — Serialize to String" linenums="1"
import json
from pathlib import Path

inventory = {
    "hostname": "web01",
    "ip": "10.0.0.1",
    "tags": ["prod", "web"],
    "config": {"port": 80, "ssl": True},
    "uptime_seconds": 86400
}

# Compact (for sending over the wire)
compact = json.dumps(inventory)

# Human-readable (for files and debugging)
pretty = json.dumps(inventory, indent=2)  # (1)!

# Sorted keys (deterministic output — good for diffs)
sorted_output = json.dumps(inventory, indent=2, sort_keys=True)  # (2)!

# Write to file
Path("/tmp/inventory.json").write_text(pretty)
```

1. `indent=2` is the standard for human-readable JSON files — use it whenever writing files a human might read or diff
2. `sort_keys=True` makes output deterministic — important when JSON ends up in version control

## Real-World Patterns

### Parse `kubectl` or AWS CLI Output

```python title="AWS EC2 Instance Inventory" linenums="1"
import json
import subprocess

def get_ec2_instances(region: str = "us-east-1") -> list[dict]:
    result = subprocess.run(
        ["aws", "ec2", "describe-instances",
         "--region", region,
         "--output", "json"],
        capture_output=True, text=True, check=True
    )
    data = json.loads(result.stdout)

    instances = []
    for reservation in data["Reservations"]:
        for instance in reservation["Instances"]:
            name_tag = next(
                (t["Value"] for t in instance.get("Tags", [])
                 if t["Key"] == "Name"),
                "unnamed"  # (1)!
            )
            instances.append({
                "id": instance["InstanceId"],
                "name": name_tag,
                "state": instance["State"]["Name"],
                "ip": instance.get("PrivateIpAddress"),
            })
    return instances

for inst in get_ec2_instances():
    print(f'{inst["name"]} ({inst["id"]}): {inst["state"]}')
```

1. AWS tags are a `[{"Key": "Name", "Value": "..."}]` array — `next()` with a generator finds the Name tag cleanly

### Update a JSON Config File

```python title="Patch a JSON Config" linenums="1"
import json
from pathlib import Path

config_path = Path("/etc/myapp/config.json")
config = json.loads(config_path.read_text())

# Update values
config["log_level"] = "DEBUG"
config["max_connections"] = 100
config.setdefault("features", {})["dark_mode"] = True  # (1)!

config_path.write_text(json.dumps(config, indent=2))
print("Config updated")
```

1. `setdefault(key, default)` creates the key with the default value if it doesn't exist, then returns it — useful for nested updates without a KeyError

### Count and Group

```python title="Count Servers by Status" linenums="1"
import json
import subprocess
from collections import Counter

result = subprocess.run(
    ["kubectl", "get", "pods", "-o", "json", "-A"],
    capture_output=True, text=True, check=True
)
pods = json.loads(result.stdout)["items"]

# Count by phase
phase_counts = Counter(p["status"].get("phase", "Unknown") for p in pods)
for phase, count in phase_counts.most_common():
    print(f"{phase}: {count}")
```

## Handling JSON Errors

```python title="Robust JSON Parsing" linenums="1"
import json
import subprocess

result = subprocess.run(
    ["curl", "-s", "https://api.example.com/health"],
    capture_output=True, text=True
)

if result.returncode != 0:
    print(f"curl failed: {result.stderr}")
    raise SystemExit(1)

try:
    data = json.loads(result.stdout)  # (1)!
except json.JSONDecodeError as e:
    print(f"Response is not valid JSON: {e}")
    print(f"Got: {result.stdout[:200]}")  # (2)!
    raise SystemExit(1)

status = data.get("status", "unknown")
print(f"Service status: {status}")
```

1. `json.JSONDecodeError` is raised if the response isn't valid JSON — happens when APIs return HTML error pages, empty responses, or partial data
2. Print the first 200 chars of the bad response to help diagnose — APIs often return an HTML error page when your auth token is expired

## Practice Problems

??? question "Practice Problem 1: Parse Pod Status"

    Given this JSON string (a simplified `kubectl get pods -o json` response), print each pod's name and phase:

    ```python
    pods_json = '''{
        "items": [
            {"metadata": {"name": "web-abc12"}, "status": {"phase": "Running"}},
            {"metadata": {"name": "web-def34"}, "status": {"phase": "Pending"}},
            {"metadata": {"name": "db-xyz99"},  "status": {"phase": "Running"}}
        ]
    }'''
    ```

    ??? tip "Answer"

        ```python title="Parse Pod Status" linenums="1"
        import json

        pods = json.loads(pods_json)
        for pod in pods["items"]:
            name = pod["metadata"]["name"]
            phase = pod["status"]["phase"]
            print(f"{name}: {phase}")
        ```

        Output:
        ```
        web-abc12: Running
        web-def34: Pending
        db-xyz99: Running
        ```

??? question "Practice Problem 2: Count by Phase"

    Using the same JSON above, produce a count of pods per phase: `{"Running": 2, "Pending": 1}`.

    ??? tip "Answer"

        ```python title="Count Pods by Phase" linenums="1"
        import json
        from collections import Counter

        pods = json.loads(pods_json)
        counts = Counter(p["status"]["phase"] for p in pods["items"])
        print(dict(counts))
        # {'Running': 2, 'Pending': 1}
        ```

        `Counter` takes any iterable and counts occurrences. The generator expression pulls out each pod's phase without building an intermediate list.

??? question "Practice Problem 3: Safe Nested Access"

    You're parsing AWS EC2 `describe-instances` output. Some instances have a `PublicIpAddress` field, some don't. Write code that prints the instance ID and public IP (or `"no public IP"` if missing) for each instance in a list.

    ??? tip "Answer"

        ```python title="Safe EC2 IP Access" linenums="1"
        import json

        instances_json = '''[
            {"InstanceId": "i-abc123", "PublicIpAddress": "54.1.2.3"},
            {"InstanceId": "i-def456"},
            {"InstanceId": "i-ghi789", "PublicIpAddress": "54.9.8.7"}
        ]'''

        instances = json.loads(instances_json)
        for inst in instances:
            ip = inst.get("PublicIpAddress", "no public IP")
            print(f'{inst["InstanceId"]}: {ip}')
        ```

        `.get("PublicIpAddress", "no public IP")` returns the fallback string if the key is absent — no `KeyError`, no `if "PublicIpAddress" in inst` check needed.

## Key Takeaways

| Bash | Python | Notes |
|:-----|:-------|:------|
| `curl url \| jq '.field'` | `json.loads(resp)["field"]` | No filter language; errors are explicit |
| `jq '.items[].name'` | `[i["name"] for i in data["items"]]` | List comprehension replaces jq iteration |
| `jq 'select(.status == "ok")'` | `[x for x in data if x["status"] == "ok"]` | Filter in Python |
| `jq '.field // "default"'` | `.get("field", "default")` | Safe access with fallback |
| `json.loads(str)` | Parse JSON string → Python dict/list | Always for API responses and command output |
| `json.load(file)` | Parse JSON file object → Python dict/list | For large files |
| `json.dumps(obj, indent=2)` | Serialize to human-readable JSON | Use `indent=2` for files |

## Further Reading

### On This Site

- [Running System Commands](running_commands.md) — calling `kubectl`, `aws`, and other tools that return JSON
- [Error Handling](error_handling.md) — handling `JSONDecodeError` and HTTP errors properly
- [Calling HTTP APIs](../efficiency/http_apis.md) — the `requests` library for real API work (retries, auth, headers)

### Official Documentation

- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html) — full standard library reference
- [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) — counting JSON values by category

### External Resources

- [jq manual](https://jqlang.github.io/jq/manual/) — useful when migrating existing `jq` filters to Python

---

`json` is in the standard library and works the same everywhere Python runs. Once you're comfortable navigating dicts and lists in Python, `jq` becomes optional — most API work translates directly to `data["key"]` and list comprehensions. YAML configs and Kubernetes manifests follow the same pattern — load the file, navigate the resulting dict.
