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

# Strings

Whenever a Python uses a block of text (of any size) it is called a `string`. They are always surrounded by either single quotes (`'myString'`) or double quotes (`"myString"`).

Strings have many built-in methods (manipulators) in Python, such as changing the letters to upper / lower case or breaking up (slicing) a string based on white space (or any character).

Strings can be sliced, see ["Slicing"](../slicing/index.md) for more details.

Strings are declared as follows:

```{code-cell} ipython3
# Declaring basic strings
myName = "Brad"
location = 'Bridgewater'
occupation = 'IT Specialist'
```

```{note}
Strings can be surrounded by either single quotes (`''`) or double quotes (`""`). If for some reason, a string must include both single and double quotes, backslash (\\) can be used as escape character. This forces Python to interpret the character following the backslash literally, thereby ignoring the quotes.
```

+++

## String Methods

Strings can accept methods which alter the contents of the string. Some examples of string methods that are built into Python include:

```{code-cell} ipython3
bookTitle = "mastery by Robert greene"
print(bookTitle.upper())
print(bookTitle.lower())
print(bookTitle.title())
```

## Concatenating Strings

Strings can be combined together with simple plus (`+`) signs:

```{code-cell} ipython3
firstName = "Albert"
lastName = "Einstien"
print("There was a famous scientist named " + firstName + lastName)
```

## Adding & Removing Whitespace

Special characters can be added to strings that add whitespace. These include:

1.  `\t` which adds a tab (4 spaces)
2.  `\n` which adds a newline

Example:

```{code-cell} ipython3
print("Hello, I'm \t \t Brad!")
print("and you are learning \n \t Python")
```

Whitespace can also be stripped out using methods. These include `strip()`  (both sides), `rstrip()` (right side) and `lstrip` (left side).

Example:

```{code-cell} ipython3
name = "      Albert Einstein       "
print("Hello I am " + name + ".") # whitespace remains
print("Hello I am " + name.strip() + ".") # whitespace stripped
print("Hello I am " + name.rstrip() + ".") # whitespace on righ stripped
print("Hello I am " + name.lstrip() + ".") # whitespace on left stripped
```

```{code-cell} ipython3

```
