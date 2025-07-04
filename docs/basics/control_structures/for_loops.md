# `for` Loops

One of the defining features of computers is their ability to perform repetitive tasks with
precision and speed. Python, like many other languages, offers powerful construct known as
the `for` loop to automate and simplify such repetitive actions.

## What is a `for` Loop?

A `for` loop is a programming structure that enables you to execute a specific code block
repeatedly. It iterates over a sequence of items, performing the same actions for each item.
Whether you want to process a list of values, manipulate strings, or iterate over the elements
of a dictionary, the `for` loop is a go-to tool.

## Basic Structure of a For Loop

In Python, a `for` loop is defined using the for keyword, followed by a variable (often called
an *iterator*) that represents each item in the sequence, the in keyword, and the sequence itself.
The indented code block immediately following the for statement defines what you want to do with
each item in the sequence.

``` python {title="Basic For Loop" linenums="1"}
for i in range(1,3):
    # Code to be executed for each item
    print(i)
```

Would return:

``` text
1
2
```

## Using For Loops with Lists

??? tip "See Also"

    [Lists in Python](../data_structures/lists.md)

One common use case for `for` loops is iterating over lists. Lists are collections of data elements,
and you can effortlessly process each element in the list using a `for` loop. Here’s an example:

``` python {title="For Loop Iterating Over a List" linenums="1"}
fav_books = ['mastery', 'the signal and the noise', 'the organized mind']

print("My favourite books include:")
for book in fav_books:
    print("   - " + book.title())
```

Results in:

``` text
My favourite books include:
   - Mastery
   - The Signal And The Noise
   - The Organized Mind
```

In the above code, the `for` loop iterates over the `fav_books` list, converting each book title to
title case and printing it.

## For Loops and the `range()` Function

`for` loops can also work in tandem with the `range()` function, which generates a sequence of
numbers. This is particularly useful when you must repeat an action a specific number of times.
However, it’s essential to remember that `range()` generates numbers *up to, but not including*
the specified end value. Here’s an example:

``` python {title="For Loop Using range()" linenums="1"}
for number in range(1,11):
    print(number)
```

Returns:

``` text
1
2
3
4
5
6
7
8
9
10
```

This code snippet will print numbers from 1 to 10, emphasizing the importance of being mindful of
the common “off by one” error.

## Looping Over Dictionaries

??? tip "See Also"

    [Dictionaries in Python](../data_structures/dictionaries.md)

Python’s `for` loop can efficiently iterate over dictionaries
([the `dict` object](../data_structures/dictionaries.md))as well. Dictionaries are collections
of key-value pairs, and you can loop over their keys, values, or both.  Lets start with a
basic `dict` of names (keys) and phone numbers (values):

``` python {title="Basic Dictionary" linenums="1"}
phone_numbers = {
    "Jim": "+37682929928",
    "Dwight": "+423998200919",
    "Michael": "+876230123654"
    }
```

Looping over the keys is the default behaviour, so it is possible to use `for
name in phone_numbers:`.  However, being a bit more explicit is recommended:

``` python {title="Iterating Over Dictionary Keys" linenums="1"}
for name in phone_numbers.keys():
    print("## KEYS")
    print(name)
    print(' ')
```
Returns:

``` bash
Jim
Dwight
Michael
```

It is also possible to loop over the values of a `dict` object:

``` python {title="Iterating Over Dictionary Values" linenums="1"}
# looping over values
for number in phone_numbers.values():
    print("## VALUES")
    print(number)
    print(' ')
```

Which would return:

``` text
+37682929928
+423998200919
+876230123654
```

Depending on the use case, it might also be necessary to return both the keys and the values of
a `dict` object:

``` python {title="Iterating Over Dictionary Items (Key and Value)" linenums="1"}
for name, number in phone_numbers.items():
    print(name, number)
```

Resulting with:

``` text
Jim +37682929928
Dwight +423998200919
Michael +876230123654
```

??? tip

    Note that `dict.items()` returns a [`tuple`](../data_structures/tuples.md) so we *unpack* it
    by using two variables in the `for` loop.
