# Exploring Python

**Automate everything. Build reliable tools. Scale your impact.**

A practical guide to Python for SREs and Platform Engineers. Part of the [BradPenney.io](https://bradpenney.io) learning ecosystem.

**Live Site:** [python.bradpenney.io](https://python.bradpenney.io)

## Overview

You manage 100 servers. You type the same kubectl commands 50 times a day. You manually parse JSON from APIs. You copy-paste deployment steps from a wiki. There's got to be a better way.

**There is. It's called Python.**

### The Automation Language

Python isn't just another programming language—it's the **automation language** for infrastructure:

- Write a script once, run it on 100 servers
- Parse JSON/YAML with 2 lines of code instead of manual grep
- Turn tribal knowledge into repeatable tools
- Build CLI tools that your whole team can use
- Automate deployments, backups, monitoring, everything

### Who This Is For

**SREs and Platform Engineers** who:

- Need to automate repetitive tasks (deployments, server configs, data migrations)
- Write "glue code" connecting systems (APIs, databases, cloud services)
- Build internal tools for their team (CLI utilities, monitoring scripts)
- Manage infrastructure as code (Terraform, Ansible wrappers)
- Work primarily in terminal environments

You may or may not have traditional programming experience. You might be a sysadmin learning to script, an operator building automation, or a DevOps engineer scaling infrastructure. **This site is for you.**

## Site Structure

Content is organized by **skill progression**:

### 📦 Basics (Your First Python Scripts)

The Python knowledge you need to write useful automation **today**:

- **Data Types** - Strings, numbers, booleans, None
- **Control Structures** - If statements, loops, functions
- **Data Structures** - Lists, dictionaries, sets for organizing data
- **File I/O** - Reading configs, parsing logs, writing reports

Start here if you're new to Python or scripting.

### ⚡ Intermediate (Production-Ready Scripts)

Build reliable, maintainable automation:

- **Error Handling** - Try/except, logging, graceful failures
- **Working with APIs** - requests library, JSON parsing, authentication
- **CLI Tools** - argparse for professional command-line interfaces
- **Working with YAML** - PyYAML for K8s manifests and Ansible
- **Subprocess** - Calling shell commands from Python safely

Master these to build tools your team will actually use.

### 🎯 Advanced (Frameworks and Scale)

Build sophisticated systems and frameworks:

- **Testing** - pytest for reliable automation
- **Packaging** - Distributing your tools
- **Async Python** - For concurrent operations
- **Web Frameworks** - Flask/FastAPI for APIs and dashboards
- **Performance** - Optimization for large-scale operations

Optional deep dives for when you need maximum capability.

## Project Structure

```
exploring_python/
├── docs/                       # Markdown content organized by skill level
│   ├── basics/                 # Fundamental Python
│   │   ├── data_types/         # Strings, ints, floats, booleans, None
│   │   ├── control_structures/ # If, loops, functions, comprehensions
│   │   └── data_structures/    # Lists, tuples, dicts, sets
│   ├── intermediate/           # Production-ready scripting
│   │   ├── error_handling/     # Exception handling, logging
│   │   ├── apis/               # requests, JSON, authentication
│   │   ├── cli_tools/          # argparse, user interaction
│   │   └── file_formats/       # JSON, YAML, CSV parsing
│   ├── advanced/               # Frameworks and scale
│   │   ├── testing/            # pytest, test automation
│   │   ├── async/              # Asyncio, concurrent operations
│   │   └── web_frameworks/     # Flask, FastAPI
│   ├── images/                 # Site images and screenshots
│   └── stylesheets/            # Custom CSS
├── mkdocs.yaml                 # Site configuration and navigation
├── pyproject.toml              # Poetry dependencies
├── CLAUDE.md                   # Content guidelines and quality standards
└── README.md                   # This file
```

## Development

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)

### Setup

```bash
# Install dependencies
poetry install

# Serve locally (http://localhost:8000)
poetry run mkdocs serve

# Build static site with link validation
poetry run mkdocs build --strict
```

### Writing Content

Articles follow rigorous quality standards:

**Content Standards:**
- Real-world automation scenario openings
- Code examples with actual output
- Multiple approaches shown (beginner → Pythonic)
- Common pitfalls highlighted
- Practice problems with full solutions
- Key takeaways tables
- Further reading organized by category

**Formatting Requirements:**
- Function names in backticks (`print()`, `len()`, `range()`)
- Blank lines before all lists
- External links validated with WebFetch
- Code blocks with titles and line numbers
- Code annotations for non-obvious logic

**Quality Checklist:**
- NO REPETITION audit across published articles
- Pre-publication link audit (4-step process)
- Visual elements present (diagrams where helpful)
- Serves multiple learning styles
- Cross-links to [cs.bradpenney.io](https://cs.bradpenney.io) for CS fundamentals

See `CLAUDE.md` for comprehensive content guidelines (~50 quality standards).

## Deployment

The site deploys automatically via GitHub Actions on push to `main`:

1. GitHub Actions builds the site using `mkdocs gh-deploy`
2. Static files are pushed to the `gh-pages` branch
3. GitHub Pages serves the content
4. Custom domain: `python.bradpenney.io` (via CNAME in `docs/`)

## Tech Stack

- **Framework**: [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Theme**: Material (slate color scheme, black/amber palette)
- **Features**: Code annotations, tabs, Mermaid diagrams, copy buttons
- **Plugins**: Search, htmlproofer (link validation)
- **Deployment**: GitHub Pages with custom domain

## Contributing

This is a personal learning repository. Content improvements and corrections are welcome via issues or pull requests.

## License

Content is available for personal and educational use. See individual files for specific licensing.

## Related Sites

This site is part of an integrated learning ecosystem:

- **[cs.bradpenney.io](https://cs.bradpenney.io)** - Computer Science fundamentals (algorithms, data structures, theory)
- **[linux.bradpenney.io](https://linux.bradpenney.io)** - Linux for SREs (where you'll run your Python scripts)
- **[k8s.bradpenney.io](https://k8s.bradpenney.io)** - Kubernetes (Python automates K8s operations)
- **[tools.bradpenney.io](https://tools.bradpenney.io)** - Development tools (Git, editors for writing Python)
- **[networking.bradpenney.io](https://networking.bradpenney.io)** - Networking (Python scripts for network automation)
- **[storage.bradpenney.io](https://storage.bradpenney.io)** - Storage (Python for backup scripts, data management)
- **[bradpenney.io](https://bradpenney.io)** - Main hub

**How they connect:**
- Linux site + Python site = Complete automation capability
- Kubernetes site + Python site = K8s automation and tooling
- Tools site + Python site = Efficient Python development
- CS site provides theory behind algorithms you'll implement in Python

---

Built with Material for MkDocs | Deployed on GitHub Pages
