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

# `for` Loops

The real power of computers is that they can repeat the same action billions of times without complaint or fatigue.  In Python (as most other languages), programmers can use a `for` loop to repeatedly execute a block of code. 

```{warning}
Like most Python syntax, `for` loops are white-space sensitive.  The lines indented below the initializing `for` loop line will be included in the loop, while those which are below but not indented will not be part of the `for` loop.  
```

The keyword `for` signals that a loop is being initialized, with the keyword `in` indicating what is being looped over. A `for` loop can be created as follows:

```{code-cell} ipython3
for letter in 'abc':
    print(letter.upper())
```

In the above example, The `for` loop repeatedly printed each individual element in the string, converting each element of the string to uppercase using the `upper()` string method.

```{note}
The variable that comes after :p:`for` is known as the *iterator*.  When looping (iterating) over a list, it is common to use the singular form of the list name (i.e. :p:`book` may iterate over list :p:`books`).  Another common convention is to use the letter :p:`i`, short for *iterator*.
```

### Looping Over Lists

[`lists`](./lists.md) and `for` loops are often combined.  It is extremely common to declare a list and then iterate over it:

```{code-cell} ipython3
favBooks = ['mastery', 'the signal and the noise', 'the organized mind']

print("My favourite books include:")
for book in favBooks:
    print("   - " + book.title())
```

### `for` Loops and the `range()` Function

It is very common to loop over a :p:`range()` function to create a list of numbers:

```{code-cell} ipython3
for number in range(1,11):
    print(number)
```

```{warning}
This is a very common source of the *"off by one"* error - remember that the :p:`range()` function stops *before* the last number - so counting from 1 to 10 means designating a range of 1 to 11.
```

`range()` also accepts a third parameter, which indicates what the output should count by (i.e. count by 2, count by 3, etc.). For example, to print all the odd numbers up to 20, as it started counting from 1 and adds 2 each time:

```{code-cell} ipython3
for number in range(1,21,2):
        print(number)
```

### Looping Over Dictionaries

You can loop over [`dictionaries`](../variables_and_data_types/dictionaries.md) as follows:

```{code-cell} ipython3
phone_numbers = {"Fred Flintstone":"+37682929928","Barney Rubble":"+423998200919"}
for value in phone_numbers.keys():
    print(value)
```

You can loop over dictionary values:

```{code-cell} ipython3
phone_numbers = {"Fred Flintstone":"+37682929928","Barney Rubble":"+423998200919"}
for value in phone_numbers.values():
    print(value)
```

It is also possible to loop over dictionary items:

```{code-cell} ipython3
phone_numbers = {"Fred Flintstone":"+37682929928","Barney Rubble":"+423998200919"}
for key, value in phone_numbers.items():
    print(key, value)
```
