---
title: "Day One: Python for Platform Engineers, SREs, and DevOps"
description: "Python automation for platform engineers who know bash — task-first guides for health checking, log parsing, config comparison, and fleet operations."
---

# Day One: Python for Platform Engineers

You know your way around a terminal. You've written `bash` scripts. You understand what a return code means, why you check `$?`, and why you don't run things as `root` unless you have to.

What you don't have — yet — is Python that's useful in your actual work. Not tutorial Python. Not "write a number-guessing game" Python. Python that solves the specific problems that come up when you're managing platforms and deployments.

That's what Day One is.

## Who This Is For

Day One assumes you:

- Work in platform engineering, SRE, infrastructure, or DevOps
- Know `bash` well enough to write scripts that do real work
- Have a specific problem to solve, not a general interest in "learning Python"

Day One does **not** assume you've written Python before. It does assume you don't need basic programming explained to you — you already know what a loop is, what a function is, what an exit code means.

## What You'll Be Able to Do

By the end of Day One, you'll be able to handle these situations with Python:

| Situation | Article |
|:----------|:--------|
| You want to avoid breaking your system Python | [The Clean Setup](setup.md) |
| API needs to recover before traffic can cut back | [Is It Still Up?](health_check.md) |
| Something broke in production, you have a giant log file | [What Just Broke?](parsing_logs.md) |
| You need to verify running config against expected | [Did the Config Change?](comparing_configs.md) |
| You need to run a check across your whole fleet | [Run This Everywhere](run_everywhere.md) |
| Your `bash` deploy script has gotten unmanageable | [My Bash Script Is Getting Out of Hand](wrapping_bash.md) |

## Why Not Just Use Bash?

Short answer: use `bash` until you can't. [Why Python (Not Just Bash)](why_python.md) covers the decision framework in detail. The quick version:

- **Stay in `bash`** for one-liners, pipelines, and glue between commands
- **Reach for Python** when you need to do something with the output — count it, compare it, report on it, loop over a list and handle failures per-item

The articles in Day One are all situations where `bash` starts to cost you more than Python does.

## The Articles

Work through these in order, or jump to the scenario you're facing right now:

1. **[The Clean Setup](setup.md)** — Setting up your Python environment correctly
2. **[Why Python (Not Just Bash)](why_python.md)** — When to reach for Python instead of staying in `bash`
3. **[Is It Still Up?](health_check.md)** — Polling a health endpoint during a redeploy
4. **[What Just Broke?](parsing_logs.md)** — Parsing a log file to find and understand errors
5. **[Did the Config Change?](comparing_configs.md)** — Comparing running config against expected
6. **[Run This Everywhere](run_everywhere.md)** — Checking a condition across a fleet of servers or services
7. **[My Bash Script Is Getting Out of Hand](wrapping_bash.md)** — Wrapping shell commands in Python when `bash` gets unwieldy
8. **[The "Don't Do This" Guide](safety_guide.md)** — Security and safety rules for production automation

## One Rule Before You Start

Automation magnifies mistakes. A `bash` one-liner that goes wrong affects one run. A Python loop that goes wrong can affect 50 servers before you catch it.

Always test on one before you run on all. Always build a `--dry-run` flag before you build the real thing.

---

Start with **[Why Python (Not Just Bash)](why_python.md)** for the framework, or jump straight to whichever scenario you're dealing with today.
