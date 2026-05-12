---
title: "The Don't Do This Guide: Python Automation Safety"
description: "Production safety rules for Python automation scripts — credentials, shell injection, dry runs, error handling, and the automation golden rule."
---

# The "Don't Do This" Guide

!!! tip "Part of Day One"
    This is part of [Day One: Python for Platform Engineers](overview.md).

Automation is force multiplication. That's the point. It's also the risk. A `bash` one-liner that has a bug affects one run. A Python script that loops over your fleet and has a bug affects every server it touches before you catch it.

These are the rules that keep automation bugs from becoming incidents.

---

## The Golden Rule

**Automation magnifies mistakes. Test on one before you run on all.**

No exceptions. Before you run a new script against production:

1. Run it with `--dry-run` to see what it would do
2. Run it against one non-critical target
3. Verify the result manually
4. Then run it at scale

This sounds like it slows you down. It doesn't. Cleaning up a fleet-wide mistake takes far longer than testing on one server.

---

## Don't Put Credentials in Your Script

```python title="❌ Never do this"
db_password = "hunter2"
api_key = "sk-a8f3c..."
```

Scripts get committed to git. Git history is forever. Even if you delete the file, the credential is in the history. Even if the repo is private, it may not always be.

```python title="✅ Use environment variables" linenums="1"
import os

db_password = os.environ.get("DB_PASSWORD")
api_key = os.environ.get("API_KEY")

if not db_password:
    print("✗ DB_PASSWORD environment variable not set")
    sys.exit(1)
```

```bash title="Setting credentials at runtime"
export DB_PASSWORD="hunter2"
python deploy.py
```

Or use a secrets manager. But the minimum bar is environment variables — not hardcoded strings.

---

## Don't Use `shell=True` With Variables You Didn't Control

```python title="❌ Shell injection risk" linenums="1"
namespace = input("Enter namespace: ")
subprocess.run(f"kubectl get pods -n {namespace}", shell=True)
```

If `namespace` is `myapp; rm -rf /`, that `rm -rf /` runs. Shell injection in automation tools is real.

```python title="✅ Always use list form" linenums="1"
namespace = input("Enter namespace: ")
subprocess.run(["kubectl", "get", "pods", "-n", namespace])
```

In list form, each argument is passed directly to the process. No shell is involved. Shell metacharacters are treated as literal text.

---

## Don't Ignore Return Codes

```python title="❌ Ignoring failure" linenums="1"
subprocess.run(["kubectl", "apply", "-f", "manifests/"])
subprocess.run(["kubectl", "rollout", "status", "deployment/myapp"])
# If apply failed, rollout status will also fail — but you might not notice
```

```python title="✅ Check return codes" linenums="1"
result = subprocess.run(
    ["kubectl", "apply", "-f", "manifests/"],
)
if result.returncode != 0:
    print("✗ Apply failed — stopping deploy")
    sys.exit(result.returncode)
```

Or use the `run()` wrapper from [My Bash Script Is Getting Out of Hand](wrapping_bash.md) which handles this for you.

---

## Don't Print Credentials to stdout

```python title="❌ Leaking credentials to logs" linenums="1"
print(f"Connecting to database with password: {db_password}")
```

CI/CD logs are often stored, shared, and searchable. Credentials in log output get leaked.

```python title="✅ Log the intent, not the secret" linenums="1"
print(f"Connecting to database as {db_user}...")
# Not the password. Never the password.
```

The same applies to API keys, tokens, and any value that came from an environment variable or secrets store.

---

## Always Build the `--dry-run` Flag First

Before you write the code that does the thing, write the code that prints what it would do:

```python title="Dry-run pattern" linenums="1"
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true",
                    help="Print actions without executing them")
args = parser.parse_args()

for server in servers:
    if args.dry_run:
        print(f"[DRY RUN] Would restart myapp on {server}")
    else:
        restart_service(server, "myapp")
```

If you're not sure a script is correct, `--dry-run` is how you check. Make it the first thing you add to any automation script that modifies state.

---

## Don't Swallow Exceptions Silently

```python title="❌ Silent exception" linenums="1"
try:
    result = requests.get(url)
    data = result.json()
except Exception:
    pass  # Everything is fine (it isn't)
```

This hides failures. Your script continues as if nothing happened, and you debug for an hour trying to figure out why downstream steps produced wrong results.

```python title="✅ At minimum, log what failed" linenums="1"
try:
    result = requests.get(url, timeout=5)
    result.raise_for_status()
    data = result.json()
except requests.exceptions.ConnectionError as e:
    print(f"✗ Could not connect to {url}: {e}")
    sys.exit(1)
except requests.exceptions.HTTPError as e:
    print(f"✗ {url} returned {e.response.status_code}")
    sys.exit(1)
```

Catch specific exceptions. Handle each one explicitly. If you can't recover, exit with a non-zero code and a useful message.

---

## Quick Reference

| Rule | Why |
|:-----|:----|
| No hardcoded credentials | Git history is forever; repos get leaked |
| No `shell=True` with variables | Shell injection is a real attack vector |
| Always check return codes | Silent failures cascade into bigger failures |
| Never log credentials | CI logs are stored and searchable |
| `--dry-run` before production | Automation magnifies mistakes |
| Never swallow exceptions | Silent failures are the hardest to debug |

---

## What's Next

Day One is complete. You can now:

- Poll an API until it recovers during a deploy → [Is It Still Up?](health_check.md)
- Parse a log file to understand a failure → [What Just Broke?](parsing_logs.md)
- Compare running config against expected → [Did the Config Change?](comparing_configs.md)
- Run checks across your fleet → [Run This Everywhere](run_everywhere.md)
- Wrap a complex `bash` script in Python → [My Bash Script Is Getting Out of Hand](wrapping_bash.md)

When you're ready to go deeper — proper logging, CLI tools your team can use, testing your automation — that's the Essentials section. Coming soon.
