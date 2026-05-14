---
title: "The Don't Do This Guide: Python Automation Safety Rules"
description: "Production safety rules for Python automation — no hardcoded credentials, no shell injection, always build dry-run first, and never let exceptions fail silently."
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

```python title="❌ Never do this" linenums="1"
db_password = "hunter2"
api_key = "sk-a8f3c..."
```

Scripts get committed to git. Git history is forever. Even if you delete the file, the credential is in the history. Even if the repo is private, it may not always be.

Your script should read from the environment. The environment should be populated from a secrets manager at runtime — not by typing the value into your shell:

```bash title="✅ Retrieve from a secrets manager at runtime" linenums="1"
# HashiCorp Vault
export DB_PASSWORD=$(vault kv get -field=password secret/myapp/db)

# AWS Secrets Manager
export DB_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id myapp/db-password --query SecretString --output text)

python deploy.py
```

For the full pattern — reading from `os.environ`, fail-fast validation, `.env` files for local dev — see **[Environment Variables and Secrets](../essentials/env_and_secrets.md)**.

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

CI/CD logs are stored, shared, and searchable. Log what you're connecting to — not the credential itself. This applies to passwords, API keys, tokens, and anything that came from a secrets store.

---

## Always Build the `--dry-run` Flag First

Before you write the code that does the thing, write the code that prints what it would do:

```python title="Dry-run pattern" linenums="1"
import click

@click.command()
@click.option("--dry-run", is_flag=True, help="Print actions without executing them")
def main(dry_run):
    for server in servers:
        if dry_run:
            print(f"[DRY RUN] Would restart myapp on {server}")
        else:
            restart_service(server, "myapp")

if __name__ == "__main__":
    main()
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
import sys
import requests

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
| No hardcoded credentials | Git history is forever — use environment variables and a secrets manager |
| No `shell=True` with variables | Shell injection is a real attack vector |
| Always check return codes | Silent failures cascade into bigger failures |
| Never log credentials | CI logs are stored and searchable |
| `--dry-run` before production | Automation magnifies mistakes |
| Never swallow exceptions | Silent failures are the hardest to debug |

---

## Practice Exercises

??? question "Exercise 1: Audit a script for security problems"
    Identify all the security problems in this script and describe how to fix each one.

    ```python title="audit_this.py — find the problems" linenums="1"
    import subprocess

    API_KEY = "sk-9f3a21b..."
    DB_URL = "postgres://admin:password123@db.prod.internal:5432/mydb"

    def deploy(env):
        subprocess.run(
            f"kubectl set env deployment/myapp API_KEY={API_KEY} -n {env}",
            shell=True
        )
        print(f"Deployed to {env} with key: {API_KEY}")

    deploy(input("Enter environment: "))
    ```

    ??? tip "Answer"
        Five problems:

        1. **Hardcoded `API_KEY`** — use `os.environ.get("API_KEY")` instead
        2. **Hardcoded `DB_URL` with credentials** — use environment variables or a secrets manager
        3. **`shell=True` with string interpolation** — `API_KEY` and `env` are injected into a shell string; injection risk if either contains shell metacharacters
        4. **Credential printed to stdout** — `print(f"...key: {API_KEY}")` leaks the key to CI/CD logs
        5. **`env` comes from `input()`** — user-controlled string passed directly into a shell command

??? question "Exercise 2: Add dry-run to an existing function"
    Add `--dry-run` support to this script using `click`.

    ```python title="restart.py — add dry-run" linenums="1"
    import subprocess

    def restart_on_server(server, service):
        subprocess.run(["ssh", server, "systemctl", "restart", service])

    servers = ["web-01.prod", "web-02.prod", "web-03.prod"]
    for s in servers:
        restart_on_server(s, "nginx")
    ```

    ??? tip "Answer"
        ```python title="restart.py — with dry-run" linenums="1"
        import subprocess
        import click

        def restart_on_server(server, service):
            subprocess.run(["ssh", server, "systemctl", "restart", service])

        @click.command()
        @click.option("--dry-run", is_flag=True, help="Print actions without executing them")
        def main(dry_run):
            servers = ["web-01.prod", "web-02.prod", "web-03.prod"]
            for server in servers:
                if dry_run:
                    print(f"[DRY RUN] Would restart nginx on {server}")
                else:
                    restart_on_server(server, "nginx")

        if __name__ == "__main__":
            main()
        ```

---

## Further Reading

### Security References
- [OWASP Command Injection](https://owasp.org/www-community/attacks/Command_Injection) — Why `shell=True` with untrusted input is dangerous
- [Python `subprocess` security considerations](https://docs.python.org/3/library/subprocess.html#security-considerations) — Official docs on the `shell=True` risk

### Tools
- [`python-dotenv`](https://pypi.org/project/python-dotenv/) — Load environment variables from a `.env` file during development; never commit the `.env` file itself
- [`click`](https://click.palletsprojects.com/) — Building CLI tools with `--dry-run` and other flags (covered in depth in the Efficiency section)

### Exploring Linux
- [Linux Safety Guide](https://linux.bradpenney.io/day_one/safety_guide/) — The same safety mindset applied to Linux commands: read before you write, understand before you run

---

## What's Next

Day One gave you working scripts. Essentials makes them maintainable.

The gap between "it works on my machine" and "my team can run this in production" comes down to a few patterns you haven't needed yet: loading credentials cleanly without `.env` files scattered everywhere, reading and modifying the YAML that describes your infrastructure, handling failures in a way that gives you useful output instead of a traceback.

Start here:

- **[Environment Variables and Secrets](../essentials/env_and_secrets.md)** — Loading credentials at runtime from environment variables and secret stores, without hardcoding or `.env` sprawl
- **[Working with YAML](../essentials/yaml.md)** — Reading, modifying, and generating Kubernetes manifests programmatically
