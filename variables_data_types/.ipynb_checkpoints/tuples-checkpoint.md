---
jupyter:
  jupytext:
    formats: md,ipynb
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.7
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Tuples

Similar to `Lists`{.interpreted-text role="ref"}, a `tuple`{.p .python} is a collection of data in Python. Unlike a `list`{.p .python}, however, a `tuple`{.p .python} cannot be changed once it is declared. Methods such as `append()`{.p .python} and `pop()`{.p .python} cannot be used with a `tuple`{.p .python}. This makes a `tuple`{.p .python} the ideal place to store values that should not change, such as the results from a `SELECT`{.p .python} statement (`SQL`{.p .python})l which will be used in the Python program but not altered.

Creating a `tuple`{.p .python} is similar to a `list`{.p .python}, but instead of square brackets, parenthesis are used:

```python
servers = ('web01', 'web02', 'app01', 'db01')
ages = (12, 19, 32, 41)
print(ages[0])
```

Tuples can be sliced, see [Slicing](../slicing/index.md) for more details.
