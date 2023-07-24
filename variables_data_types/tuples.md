---
jupytext:
  formats: ipynb,md:myst
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

# Tuples

Similar to [Lists](./lists.md), a `tuple` is a collection of data in Python. Unlike a `list`, however, a `tuple` cannot be changed once it is declared. Methods such as `append()` and `pop()` cannot be used with a `tuple`. This makes a `tuple` the ideal place to store values that should not change, such as the results from a `SELECT` statement (`SQL`)l which will be used in the Python program but not altered.

Creating a `tuple` is similar to a `list`, but instead of square brackets, parenthesis are used:

```{code-cell} ipython3
servers = ('web01', 'web02', 'app01', 'db01')
ages = (12, 19, 32, 41)
print(ages[0])
```

Tuples can be sliced, see [Slicing](../slicing/index.md) for more details.
