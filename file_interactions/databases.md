---
jupytext:
  formats: ipynb,md:myst
  main_language: python
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Databases with Python

Interacting with databases programmatically is a foundational skill for all Python developers.  The basic concepts with all *Relational Database Management Systems* (RDBMS) are similar, whether Oracle, IBM DB2, SQL Server, or MySQL (and many others).  Interestingly, Python has a built-in module that supports the use of a light-weight database - SQLite3 (see [`python_sqlite3`](../modules_packages/core_modules/sqlite3.md). It isn't an enterprise-grade database, but is very useful for both learning (teaching) purposes, and also building back-end tracking for Python applications.

As an example, it would be very common for a web-scraping application to store its information in an SQLite3 database.  User scores could be stored in one, or perhaps reference materials such as glossaries, projects, or anything else that should be tracked persistently through application startups/shutdowns.
