# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Core Philosophy: Task-First, Not Concept-First

**This is the most important thing to understand about this site.**

Every other Python tutorial teaches concepts first: "here's what a string is, here's why you use it." This site teaches tasks first: "you need to check an API during a redeploy — here's why Python is the right tool and here's how to do it."

Python concepts appear in service of solving a specific problem. The reader arrives because they have a task at work, not because they want to learn about data types.

**Before writing any article, name the real-world scenario the reader is in. If you can't name it, the article isn't ready.**

---

## Target Persona

**Who they are:** Platform engineer, SRE, or DevOps engineer who works in production environments.

**What they already know:**
- Bash scripting — they know what a loop is, what an exit code means, why you don't run as root
- Linux command line — comfortable in a terminal
- Their infrastructure — Kubernetes, cloud providers, deployment pipelines

**What they don't have yet:** Python that's useful in their actual work. Not tutorial Python — production automation Python.

**What they are NOT:**
- Programming beginners who need basic concepts explained
- CS students learning Python for the first time
- Developers who write application code (this is infrastructure automation)

**Opening pattern:** Start with THEIR situation — a specific task they face at work — then introduce Python as the right tool for it.

- ❌ Wrong: "Strings are sequences of characters..."
- ✅ Right: "You're deploying and need to know when the API comes back up. Here's why a Python poller beats a bash curl loop."

---

## Site Structure

### 🐍 Day One (Essential tier — always free)

For engineers who need Python to solve a specific problem today. Task-first, one scenario per article, just enough Python to understand what's happening.

**Tone:** Mentorship, but peer-level. No hand-holding on basic programming. Assume they know bash and can follow code.

**Articles are titled by the task, not the concept:**
- ✅ "Is It Still Up?" (teaches requests, loops, sys.exit)
- ✅ "What Just Broke?" (teaches file I/O, Counter, string parsing)
- ❌ "Introduction to the requests library"

### 📦 Essentials (Efficient tier — free)

Core patterns for engineers who've done Day One and want to write better automation. Peer-to-peer tone. No hand-holding.

**Required section in every Essentials article:** "Where You've Seen This" — connects the Python concept to something they already do in bash or their existing workflow.

### ⚡ Efficiency (Efficient/professional tier — free)

Professional-grade Python: argparse, logging, testing, things your team can actually use.

### 🎯 Mastery (Mastery tier — eventually paywalled)

Production Python: packaging, FastAPI, async, Kubernetes client. Professionals with training budgets.

---

## Tone by Tier

| Tier | Tone | What to assume |
|------|------|----------------|
| Day One | Mentorship, practical | They know bash; they don't know Python |
| Essentials | Peer-to-peer | They can write Python scripts; want to write better ones |
| Efficiency | Colleague-to-colleague | Working professional; no hand-holding |
| Mastery | Expert-to-expert | Senior engineer; deep production context |

**Tone shifts at Essentials** — drop the guiding hand, treat them as peers.

---

## Article Structure (Day One)

1. **Frontmatter** — `title` (50-60 chars), `description` (150-160 chars)
2. **"Part of Day One" callout** — links back to overview
3. **The scenario** — specific situation the reader is in right now
4. **The bash version first** (if applicable) — show what they'd normally do and where it falls short
5. **The Python solution** — code with annotations
6. **Extensions** — natural next steps (check a JSON field, add parallelism, etc.)
7. **Practice exercises** — `??? question` with nested `??? tip "Answer"`
8. **Quick Recap table** — concept → what it does
9. **What's Next** — link to the next article in the path
10. **Further Reading** — organized by category

---

## Code Standards

**All code blocks must have:**
- `title=` attribute describing what the code demonstrates
- `linenums="1"`
- Language specified (`python`, `bash`)
- Annotations (`# (1)!`) for non-obvious lines

**Python code must:**
- Be tested and actually work
- Use realistic variable names (not `foo`, `x`, `my_list`)
- Show actual output in comments or separate output blocks
- Exit with meaningful codes (`sys.exit(1)`, not always `sys.exit(0)`)

**Don't use `shell=True` in code examples** without an explicit comment explaining why and the security trade-off.

---

## Critical Rules

### No repetition
Cross-link instead of repeating. If `subprocess.run` is covered in `wrapping_bash.md`, the `run_everywhere.md` article links to it rather than re-explaining it.

### Blank line before every list
This is a recurring MkDocs rendering issue. Every bullet list must have a blank line before it.

### Command names in backticks
In prose: ✅ `requests`, `subprocess.run()`, `sys.exit()` — ❌ requests, subprocess.run, sys.exit

### Never link to unpublished articles
Check `mkdocs.yaml` nav. If an article is commented out, don't link to it.

---

## Publishing Workflow

1. Write the article
2. Pass the quality checklist (below)
3. Add to the `nav:` section in `mkdocs.yaml`
4. Do NOT run `mkdocs` commands — the user handles builds and deploys

### Quality Checklist

- [ ] Task/scenario clearly identified in the opening paragraph
- [ ] Bash version shown first (if applicable) with its limitations explained
- [ ] Python solution is complete and actually works
- [ ] Code annotations on non-obvious lines
- [ ] `title=` and `linenums="1"` on all code blocks
- [ ] Blank lines before all lists
- [ ] Practice exercises with nested solutions
- [ ] Quick Recap table
- [ ] What's Next link
- [ ] Further Reading by category
- [ ] "Part of Day One" (or Essentials/Efficiency/Mastery) callout
- [ ] SEO frontmatter: title 50-60 chars, description 150-160 chars
- [ ] No links to unpublished articles

---

## What NOT to Do

- ❌ Write concept-first articles ("Today we'll learn about dictionaries...")
- ❌ Write articles without a named real-world scenario
- ❌ Use `shell=True` without explaining why and the security trade-off
- ❌ Hardcode credentials in code examples
- ❌ Run git commits, pushes, or mkdocs commands (user handles these)
- ❌ Link to unpublished articles

## File Structure

- `docs/` — Published content
  - `day_one/` — Day One task articles (all published)
  - `essentials/` — Essentials articles (coming)
  - `efficiency/` — Efficiency articles (coming)
  - `mastery/` — Mastery articles (coming)
- `_archive/` — Old content from the previous concept-first structure
- `mkdocs.yaml` — Nav and configuration
