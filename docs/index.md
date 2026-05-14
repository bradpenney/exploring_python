---
title: "Exploring Python: Automation for Platform Engineers"
description: "Python automation for platform engineers and SREs — task-first guides for health checking, log parsing, config comparison, fleet operations, and more."
---

<img src="images/exploring_python.png" alt="Exploring Python" class="img-responsive-right" width="300">

# Exploring Python

You automate things. Bash has served you well — it's the right tool for one-liners, pipelines, and quick shell glue. But somewhere around the third time you've rewritten the same 60-line deploy script because error handling got too complicated, you need something that scales with you.

This site is Python for people who already know how to work in a terminal. Not a programming primer. Not syntax drills. Real automation tasks, organized by the problem you're trying to solve.

## Who This Is For

You work in platform engineering, infrastructure, SRE, or DevOps. You know `bash`. You've probably got a folder of scripts that "mostly work." You need Python to be useful — not eventually, right now.

You don't need to know what a decorator is before you can write a health-check poller. You don't need to understand generators before you can parse a log file.

This site starts with the task. The Python comes with it.

## The Path

=== "🐍 Day One"

    Each article starts with a real scenario you'd face at work. Just enough Python to solve it, no syntax drills.

    - [The Clean Setup](day_one/setup.md) — Stop "Python Hell" before it starts
    - [Why Python, Not Just Bash](day_one/why_python.md) — When `bash` is the right tool and when it isn't
    - [Is It Still Up?](day_one/health_check.md) — Poll a health endpoint during a redeploy
    - [What Just Broke?](day_one/parsing_logs.md) — Parse a log file to understand failures fast
    - [Did the Config Change?](day_one/comparing_configs.md) — Compare running config against what you deployed
    - [Run This Everywhere](day_one/run_everywhere.md) — Run a check across your whole fleet
    - [My Bash Script Is Getting Out of Hand](day_one/wrapping_bash.md) — Wrap complex shell logic in Python
    - [The "Don't Do This" Guide](day_one/safety_guide.md) — Safety rules before you run any of this in production

    [Start with the Overview →](day_one/overview.md)

=== "📦 Essentials"

    Core Python patterns for writing better, more maintainable automation. Deeper coverage of the tools you'll reach for every day.

    - [Environment Variables and Secrets](essentials/env_and_secrets.md) — Loading credentials at runtime, `.env` files, failing fast on missing vars
    - [Working with YAML](essentials/yaml.md) — Reading, modifying, and generating Kubernetes manifests

=== "⚡ Efficiency"

    Professional-grade Python: CLI tools with `click`, proper logging, testing your automation, building things your team can actually use.

    *Coming soon.*

=== "🎯 Mastery"

    Production Python: packaging tools for distribution, internal APIs with FastAPI, async operations, the Kubernetes Python client.

    *Coming soon.*

---

If `bash` is getting in your way, start with [Day One](day_one/overview.md).
