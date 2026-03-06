# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Repository Overview

**Exploring Python** teaches Python to working engineers who have hit the ceiling of what Bash and shell tools can do. It is not a Python tutorial. It is a graduation guide — from shell scripting to Python — written for people who already know how to automate things and need better tools to do it.

**Site URL:** python.bradpenney.io
**Theme:** Material for MkDocs, Slate dark, black/amber

## Important Preferences

**Git Operations**: The user handles all git operations. Do not commit or push.
**MkDocs Operations**: The user handles `mkdocs serve` and `mkdocs build`. Do not run these.

---

## The Persona

### Who They Are

A working engineer — sysadmin, application admin, platform engineer, DevOps — who:

- Writes Bash (or ksh/zsh) fluently. It's their first language.
- Lives in the terminal. SSH, `grep`, `awk`, `sed`, `find`, `curl`, `jq` — daily tools.
- Knows Linux system administration deeply: processes, files, permissions, services, networking.
- Has hit the wall. Bash can't parse nested JSON cleanly. `curl | jq` pipelines are getting fragile. Error handling with `$?` is a nightmare. They need something better.
- Is NOT a software developer. They're not building web apps. They're writing automation, glue scripts, monitoring tools, deployment scripts, and API integrations.

### What They Already Know (Don't Explain These)

- Variables, loops, conditionals, functions — they know these from Bash
- Piping, redirection, stdin/stdout/stderr
- File permissions, processes, signals
- HTTP basics — they've used `curl` extensively
- JSON — they've wrangled it with `jq`
- YAML — they live in it (Kubernetes, Ansible, Docker Compose)

### What They Want

- To replace their brittle Bash scripts with maintainable Python
- To call APIs properly without shell hackery
- To parse structured data (JSON, YAML, CSV) reliably
- To write tools that handle errors gracefully
- To ship something they're not embarrassed to put in a repo

### What They Do NOT Need

- "What is a variable?" tutorials
- Academic exercises with `foo` and `bar`
- Explanations of basic programming concepts they already know
- Theory disconnected from the work they do right now

---

## The ROI Rule — Non-Negotiable

**Every single article must deliver a useable skill the reader walks away with.**

This is not a reference site. It's not a comprehensive language guide. Every article answers one question from the reader's perspective: **"What can I do now that I couldn't do before?"**

Before writing any article, answer: *After reading this, what can the engineer actually build or do?*

If the answer is vague — "they'll understand X better" — the article concept is wrong. Reframe it around a concrete task.

**Good:** "After this article, I can replace my `curl | jq` pipeline with a Python script that actually handles errors."
**Bad:** "After this article, I'll understand Python dictionaries."

---

## Site Structure

### 📦 Essentials — Replace your Bash scripts today

The minimum viable Python skillset for engineers graduating from Bash. After completing Essentials, the reader can write real, working Python scripts for the problems they face daily.

| Article | The Skill |
|:--------|:----------|
| `python_vs_bash.md` | Know when Python wins, have it installed and running |
| `running_commands.md` | Replace shell calls with `subprocess.run()` |
| `reading_files_and_parsing_text.md` | Replace `cat \| awk \| grep` pipelines |
| `working_with_json.md` | Replace `curl \| jq` |
| `error_handling.md` | Replace `$?`, `set -e`, `\|\| exit 1` |
| `cli_scripts.md` | Replace `getopts`, accept real arguments |

### ⚡ Efficiency — Write Python, not Bash with more characters

For engineers who can write Python but aren't yet writing *good* Python. These articles make the difference between "it works" and "I'd actually put this in production."

| Article | The Skill |
|:--------|:----------|
| `http_apis.md` | Hit REST endpoints properly without `curl` |
| `files_and_directories.md` | Replace `find`, `ls`, `cp`, `mv`, `mkdir` |
| `config_files.md` | Parse YAML/INI/TOML configs properly |
| `environment_and_secrets.md` | Stop hardcoding credentials |
| `logging.md` | Replace `echo` to stderr with real log levels |
| `functions_and_modules.md` | Stop copy-pasting between scripts |

### 🎯 Mastery — Build tools, not just scripts

For engineers who want to go beyond one-off scripts to tools they can distribute and maintain.

| Article | The Skill |
|:--------|:----------|
| `proper_cli_tools.md` | Ship a tool others can install and run |
| `testing_scripts.md` | Stop testing by hand |
| `reliable_api_clients.md` | Retries, timeouts, pagination, auth |
| `csv_and_tabular_data.md` | Process real data exports cleanly |
| `packaging_and_sharing.md` | Distribute tools to your team |

---

## Directory Structure

```
docs/
├── essentials/          # Replace your Bash scripts today
├── efficiency/          # Write Python, not Bash with more characters
├── mastery/             # Build tools, not just scripts
├── images/
├── stylesheets/
│   └── extra.css
└── index.md
```

**No `basics/` directory. No `data_types/` directory. No articles about what a string or dict is.**

---

## Article Structure

Every article follows this pattern. No exceptions.

### 1. Opening — The Problem They Already Have

Start with a real scenario from their working life. A Bash script that's getting fragile. A `curl | jq` pipeline that breaks on edge cases. A `$?` check that's lying to them. They should read the first paragraph and think *"yes, that's exactly my situation."*

**Never open with Python syntax. Always open with their problem.**

### 2. The Bash Version First

Show what they'd write in Bash. Side-by-side or inline. This grounds the article in what they know.

```markdown
## The Bash Way

You've been doing this with a pipeline:

```bash title="What You've Been Doing"
curl -s "https://api.example.com/pods" \
  | jq -r '.items[].metadata.name'
```

It works until the API changes shape, the token expires, or you need to retry on failure.
```

### 3. The Python Solution

Show the Python equivalent. Introduce any new concepts (dicts, lists, etc.) naturally within the solution — never as standalone topics. The reader learns what a dict is because they need one to parse JSON. Not because they're reading a "dicts" article.

### 4. Why Python Wins Here

One tight paragraph or short list explaining what Python gives them that Bash couldn't. Error handling. Readability. Maintainability. Performance. Be specific.

### 5. Going Deeper (as needed)

Cover the variations, edge cases, and gotchas they'll actually encounter. Keep it grounded in real scenarios.

### 6. Practice Problems (2–4 problems)

Sysadmin-flavored. Real scenarios. No `foo`/`bar`.

```markdown
??? question "Practice Problem 1: Parse a Health Check Response"

    You have a script that curls a health endpoint returning JSON like:
    `{"status": "ok", "version": "1.4.2", "uptime_seconds": 3600}`

    Write Python to print `"Service is ok (v1.4.2)"` or `"Service is DOWN"`.

    ??? tip "Answer"

        ```python title="Health Check Parser" linenums="1"
        import json
        import subprocess

        result = subprocess.run(
            ["curl", "-s", "https://api.example.com/health"],
            capture_output=True, text=True, check=True
        )
        data = json.loads(result.stdout)
        if data["status"] == "ok":
            print(f"Service is ok (v{data['version']})")
        else:
            print("Service is DOWN")
        ```
```

### 7. Key Takeaways Table

```markdown
## Key Takeaways

| Bash | Python Equivalent | Why It's Better |
|:-----|:-----------------|:----------------|
| `curl url \| jq '.field'` | `requests.get(url).json()["field"]` | Error handling, retries, type safety |
```

### 8. Further Reading (split format — required)

```markdown
## Further Reading

### On This Site
- [Error Handling](error_handling.md) — what to do when the API returns 500

### Official Documentation
- [requests library](https://docs.python-requests.org/) — the standard for HTTP in Python

### External Resources
- [Real Python: HTTP Requests](https://realpython.com/...) — deeper dive
```

---

## Code Formatting Rules

### All Code Blocks

```
```python title="Descriptive Title" linenums="1"
```

Title must describe what the code DOES, not what it IS. "Parse JSON API Response" not "JSON Example".

### Code Annotations

Use `# (1)!` inline annotations to explain non-obvious lines. After the block, provide numbered explanations. Annotate things a Bash scripter would find surprising — not obvious things.

```python title="subprocess with Error Handling" linenums="1"
result = subprocess.run(
    ["systemctl", "status", "nginx"],
    capture_output=True,  # (1)!
    text=True,            # (2)!
    check=False           # (3)!
)
```

1. Captures both stdout and stderr into `result.stdout` / `result.stderr` — no more `2>&1`
2. Decodes bytes to string automatically — no `.decode("utf-8")` needed
3. Don't raise on non-zero exit — we'll check `result.returncode` ourselves

### Technical Terms in Prose

Always backtick command names, Python types, and language-specific values in prose:
- ✅ `subprocess.run()`, `dict`, `None`, `True`, `False`, `json.loads()`
- ❌ subprocess.run(), dict, None, True, False, json.loads()

### Bash Comparison Blocks

Always include the Bash equivalent early in the article:

```markdown
=== ":simple-gnubash: Bash"

    ```bash title="The Old Way" linenums="1"
    # What you've been doing
    ```

=== ":material-language-python: Python"

    ```python title="The Python Way" linenums="1"
    # What you'll do now
    ```
```

---

## Content Standards

### The Bash Comparison Is Required

Every Essentials and Efficiency article must show the Bash equivalent. The reader needs to see the bridge from where they are to where they're going. Not optional.

### No Language-Feature Articles

There are no articles about:
- What strings are
- What dicts are
- What lists are
- What for loops are

These concepts appear organically when solving real problems. If a reader needs to understand what a dict is, they'll learn it because parsing JSON returned a dict — not because we wrote a "dicts" article.

### Sysadmin-Flavored Examples Only

Every example must be grounded in the work this engineer actually does:

✅ Parsing `/etc/hosts`. Checking systemd service status. Hitting a Kubernetes API. Reading a `.env` file. Processing a CSV export from a monitoring tool. Parsing an nginx access log.

❌ Shopping carts. Student grade calculators. Fibonacci sequences. Anything involving `foo`, `bar`, `baz`.

### No Hand-Holding

Don't explain what a loop is. Don't explain what a function is. These engineers have written hundreds of both in Bash. Show them the Python syntax and trust them to understand the concept.

### Closing Paragraphs

End each article with one grounded paragraph that connects back to their work. What will they do differently tomorrow? What problem is now solved? No generic "Python is great!" endings.

---

## Publishing Workflow

### Draft/Publish via Exclude Plugin

The `mkdocs-exclude` plugin in `mkdocs.yaml` controls what appears on the live site. Draft articles exist in the repo but are excluded from builds, sitemaps, and search.

**To publish:** Remove from the `exclude:` glob list in `mkdocs.yaml` AND uncomment in `nav:`.

### Required Frontmatter

Every published article MUST have:

```yaml
---
title: "Title With Colon: Must Be Quoted"
description: Compelling 150-160 char description for search results.
---
```

Titles with colons MUST be quoted — unquoted colons break PyYAML silently.

### Pre-Publication Checklist

**Content:**
- [ ] Opens with a real problem scenario (Bash pain point), NOT Python syntax
- [ ] Shows the Bash equivalent before the Python solution
- [ ] Every Python concept introduced within a real task context
- [ ] Examples use sysadmin/ops scenarios only — no toy examples
- [ ] Practice problems are sysadmin-flavored (2–4 problems)
- [ ] Key Takeaways table present (Bash → Python → Why Better format)
- [ ] Further Reading split into On This Site / Official Documentation / External Resources
- [ ] Closing paragraph connects back to their actual work
- [ ] No hardcoded local paths (e.g., `/home/brad/...`)

**Formatting:**
- [ ] All code blocks have `title="..."` and `linenums="1"`
- [ ] Code annotations on non-obvious lines
- [ ] Blank lines before ALL lists (recurring MkDocs issue)
- [ ] Technical terms backticked in prose
- [ ] Admonitions use `??? tip` — never `??? note` or `!!! note`
- [ ] Internal links use relative paths

**Integration:**
- [ ] All internal links point to published articles only
- [ ] External links validated (URLs break over time)
- [ ] Removed from `exclude:` list in `mkdocs.yaml`
- [ ] Uncommented in `nav:` in `mkdocs.yaml`
- [ ] Frontmatter present (title and description)

---

## Mermaid Diagram Color Scheme

Slate dark theme — use consistently:

- **Standard Node:** `fill:#2d3748,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- **Highlighted Node:** `fill:#4a5568,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- **Darker Node:** `fill:#1a202c,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- **Accent (Amber):** `fill:#d69e2e,stroke:#cbd5e0,stroke-width:2px,color:#000`

---

## Video Summary Section

When a video exists, embed at the bottom:

```markdown
## Video Summary

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Descriptive Title" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
```

---

## Common Commands

```bash
# Install dependencies
poetry install

# Serve locally
poetry run mkdocs serve

# Build (ALWAYS use --strict)
poetry run mkdocs build --strict
```

`mkdocs-htmlproofer-plugin` validates all internal links. Always build with `--strict`.
