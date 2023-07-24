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

# Integers

In Python (as most programming languages), numbers are treated differently than [`strings`](./strings.md).  They are interpreted as numbers, therefore standard mathematical operations can be performed on them.  Integers are whole numbers (as opposed to [`floats`](./floats.md)).  Any two integers can be declared and then used mathematically. 

```{note}
Be careful of division in Python - the quotient of two `ints` could result in a `float` if the numbers cannot be divided evenly.
```

Declaring `ints`, as all other variables in Python, is simple syntax:

```{code-cell} ipython3
# Declaring basic integer values   
rank = 10
eggs = 12
people = 3
```

```{warning}
When using an `int` in combination with [`strings`](./strings.md), it is important to *cast* the `int` as a `string` in order for it to print out correct.  For example, `print("My age is " + str(myAge))` casts the `int` `myAge` as a string within the context of the `print` statement.
```

The most common usage of `ints` is in for mathematical operations, such as:

```{code-cell} ipython3
length = 10
width = 5
height = 3
base = 10
side = 6
rectangle_area = length * width # the value of 30 would now be assigned to the variable area
triangle_area = (0.5 * base * height) # one half base multipled by height
square_area = side**2 # exponents
print("The area of a the rectangle is " + str(rectangle_area))
print("The area of the triangle is " + str(triangle_area))
print("The area of the square is " + str(square_area))
```
