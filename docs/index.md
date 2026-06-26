---
date: "2025-06-04 10:14"
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

## Where do you start?

<div class="grid cards two-col" markdown>

-   :material-flag-checkered: **Day One**

    ---

    Each article starts with a real scenario you'd face at work — just enough Python to solve it, no syntax drills.

    [:octicons-arrow-right-24: Start with Day One](day_one/overview.md)

-   :material-package-variant: **Essentials**

    ---

    Core Python patterns for writing better, more maintainable automation — deeper coverage of the tools you'll reach for every day.

    [:octicons-arrow-right-24: Start with Essentials](essentials/env_and_secrets.md)

</div>

## ⚡ Efficiency *(Coming soon)*

Professional-grade Python: CLI tools with `click`, proper logging, testing your automation, building things your team can actually use.

## 🎯 Mastery *(Coming soon)*

Production Python: packaging tools for distribution, internal APIs with FastAPI, async operations, the Kubernetes Python client.

---

If `bash` is getting in your way, start with [Day One](day_one/overview.md).
