---
date: "2026-07-30 13:00"
title: "Essentials: Core Python Patterns for Automation"
description: "Core Python patterns for platform engineers past the first script — handling credentials safely and working with the YAML your team already has everywhere."
---

# Essentials: Core Python for Platform Engineers

Day One got you a script that solves one specific problem. Essentials is where those one-off scripts turn into patterns you reuse — pulling secrets and config the right way, working with the YAML your team already has everywhere (Kubernetes manifests, CI configs, Ansible playbooks).

## Who This Is For

Essentials assumes you:

- Finished Day One, or already write basic Python scripts that work
- Want patterns that hold up once a script becomes something your team relies on
- Are ready for peer-to-peer tone — no hand-holding on the basics

## What You'll Be Able to Do

| Situation | Article |
|:----------|:--------|
| A script hardcoded a password once, and you don't want to do that again | [Environment Variables and Secrets](env_and_secrets.md) |
| Your team's Kubernetes manifests, CI configs, and Ansible files are all YAML | [Working with YAML](yaml.md) |

## The Articles

1. **[Environment Variables and Secrets](env_and_secrets.md)** — loading API keys, passwords, and tokens with environment variables, `.env` files, and secrets stores, without hardcoding anything
2. **[Working with YAML](yaml.md)** — reading, modifying, and generating YAML with PyYAML, including multi-document files, safe loading, and the pitfalls that bite people first

---

Start with **[Environment Variables and Secrets](env_and_secrets.md)** — hardcoded credentials are usually the first thing worth fixing.

After Essentials, **[Efficiency](../efficiency/overview.md)** covers professional-grade Python: CLI tools, logging, and testing your automation.
