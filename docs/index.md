<img src="images/exploring_python.png" alt="Explore Python" class="img-responsive-right" width="300">

# Exploring Python

Your Bash scripts are getting long. The `jq` pipeline breaks whenever the API changes shape.
Error handling is a maze of `$?` checks that still let things slip through. A colleague asked
you to add logging and you said "later."

That's the ceiling. Python is what's on the other side.

This site is a graduation guide — from shell scripting to Python — for engineers who already
know how to automate things. It doesn't explain what a variable is. It shows you Python through
the lens of what you already do in Bash, demonstrates where Python's approach is cleaner or more
capable, and gets you writing real Python for real infrastructure work.

## 📦 Essentials — Replace your Bash scripts today

The minimum viable Python skillset for engineers graduating from Bash:

- [**Python vs Bash: When to Graduate**](essentials/python_vs_bash.md) — Know when Python wins, have it installed and running
- [**Running System Commands**](essentials/running_commands.md) — Replace shell calls with `subprocess.run()`
- [**Working with JSON**](essentials/working_with_json.md) — Replace `curl | jq` pipelines
- [**Error Handling**](essentials/error_handling.md) — Replace `$?`, `set -e`, `|| exit 1`

## ⚡ Efficiency — Write Python, not Bash with more characters

For engineers who can write Python but aren't yet writing *good* Python:

- [**Calling HTTP APIs**](efficiency/http_apis.md) — Hit REST endpoints properly without `curl`
- [**File and Directory Operations**](efficiency/files_and_directories.md) — Replace `find`, `ls`, `cp`, `mv`, `mkdir`
- [**Environment Variables and Secrets**](efficiency/environment_and_secrets.md) — Stop hardcoding credentials
- [**Logging**](efficiency/logging.md) — Replace `echo` to stderr with real log levels

---

Start with [Python vs Bash: When to Graduate](essentials/python_vs_bash.md) if you're new here.
Jump straight to whatever problem you're solving if you're not.
