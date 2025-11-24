# `for` Loops

One of the defining features of computers is their ability to perform repetitive tasks with
precision and speed. 🔁 Python, like many other languages, offers powerful construct known as
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
the common "off by one" error. (We've all been there. 😅)

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

## Enumerate: Getting Index and Value

A common need is to track both the index and the value while looping. The rookie mistake is
to manually manage a counter:

``` python {title="The Manual Counter (Don't Do This)" linenums="1"}
# Works, but not Pythonic
fruits = ["apple", "banana", "cherry"]
index = 0
for fruit in fruits:
    print(f"{index}: {fruit}")
    index += 1
```

Python has a better way — `enumerate()`:

``` python {title="Using enumerate()" linenums="1"}
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Returns:

``` text
0: apple
1: banana
2: cherry
```

### Starting from a Different Index

By default, `enumerate()` starts at 0. You can change this with the `start` parameter:

``` python {title="enumerate() with Custom Start" linenums="1"}
# Start counting from 1 (great for display purposes)
menu_items = ["Pizza", "Burger", "Salad", "Tacos"]

print("Today's Menu:")
for number, item in enumerate(menu_items, start=1):
    print(f"  {number}. {item}")
```

Returns:

``` text
Today's Menu:
  1. Pizza
  2. Burger
  3. Salad
  4. Tacos
```

### Practical Uses for enumerate()

``` python {title="enumerate() Patterns" linenums="1"}
# Finding positions of matching items
text = "The quick brown fox jumps over the lazy dog"
words = text.split()

for i, word in enumerate(words):
    if word.startswith("t") or word.startswith("T"):
        print(f"Word '{word}' found at position {i}")

# Modifying items in a list by index
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    numbers[i] = num * 2
print(numbers)  # [2, 4, 6, 8, 10]
```

## Zip: Parallel Iteration

When you need to loop over multiple sequences simultaneously, `zip()` is your friend. It pairs
up elements from each sequence like a zipper bringing two sides together. 🤐

``` python {title="Basic zip()" linenums="1"}
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

Returns:

``` text
Alice: 85
Bob: 92
Charlie: 78
```

### Zipping Multiple Sequences

`zip()` isn't limited to two sequences — add as many as you need:

``` python {title="Zipping Multiple Sequences" linenums="1"}
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name} scored {score} ({grade})")
```

Returns:

``` text
Alice scored 85 (B)
Bob scored 92 (A)
Charlie scored 78 (C)
```

### What Happens with Unequal Lengths?

By default, `zip()` stops at the shortest sequence:

``` python {title="Unequal Lengths" linenums="1"}
a = [1, 2, 3, 4, 5]
b = ["one", "two", "three"]

for num, word in zip(a, b):
    print(f"{num} = {word}")
# Only prints 3 pairs — stops when 'b' runs out
```

If you need to process all items (filling in missing values), use `itertools.zip_longest`:

``` python {title="zip_longest for Unequal Sequences" linenums="1"}
from itertools import zip_longest

a = [1, 2, 3, 4, 5]
b = ["one", "two", "three"]

for num, word in zip_longest(a, b, fillvalue="???"):
    print(f"{num} = {word}")
```

Returns:

``` text
1 = one
2 = two
3 = three
4 = ???
5 = ???
```

### Combining enumerate() and zip()

These tools compose beautifully:

``` python {title="enumerate() with zip()" linenums="1"}
questions = ["What is 2+2?", "What is the capital of France?"]
answers = ["4", "Paris"]

print("Quiz Review:")
for i, (question, answer) in enumerate(questions, start=1):
    print(f"Q{i}: {questions[i-1]} → {answers[i-1]}")

# Or more elegantly:
for i, (q, a) in enumerate(zip(questions, answers), start=1):
    print(f"Q{i}: {q} → {a}")
```

## Range Patterns

We've seen basic `range()`, but it has more tricks up its sleeve.

### The Three-Argument Form

`range(start, stop, step)` gives you full control:

``` python {title="range() with Step" linenums="1"}
# Count by twos
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# Count by fives
for i in range(0, 51, 5):
    print(i, end=" ")  # 0 5 10 15 20 25 30 35 40 45 50
```

### Counting Backwards

Use a negative step to count down:

``` python {title="Reverse Range" linenums="1"}
# Countdown!
for i in range(10, 0, -1):
    print(i, end="...")
print("Liftoff! 🚀")
```

Returns:

``` text
10...9...8...7...6...5...4...3...2...1...Liftoff! 🚀
```

### Common range() Patterns

``` python {title="Useful range() Patterns" linenums="1"}
# Process every other item
items = ["a", "b", "c", "d", "e", "f"]
for i in range(0, len(items), 2):
    print(items[i], end=" ")  # a c e
print()

# Reverse iterate through a list (by index)
for i in range(len(items) - 1, -1, -1):
    print(items[i], end=" ")  # f e d c b a
print()

# Or just use reversed() — cleaner!
for item in reversed(items):
    print(item, end=" ")  # f e d c b a
```

!!! tip "reversed() vs Negative Step"

    `reversed()` is often cleaner than `range(len(x)-1, -1, -1)`. It works on any sequence
    and reads more naturally. Use it when you can. ✨

## Nested Loops

Loops can contain other loops. Each iteration of the outer loop runs the entire inner loop:

``` python {title="Nested Loops" linenums="1"}
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

Returns:

``` text
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
---
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
---
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
---
```

### Practical Nested Loop: Grid Coordinates

``` python {title="Grid Coordinates" linenums="1"}
rows = 3
cols = 4

for row in range(rows):
    for col in range(cols):
        print(f"({row},{col})", end=" ")
    print()  # New line after each row
```

Returns:

``` text
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

!!! warning "Nested Loop Performance"

    Nested loops multiply iterations. A loop of 1000 inside a loop of 1000 = 1,000,000 iterations.
    Be mindful of performance with large datasets. Sometimes there's a smarter approach. 🧠

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **enumerate()** | Get index AND value: `for i, item in enumerate(list)` |
| **enumerate(start=1)** | Change the starting index |
| **zip()** | Pair up multiple sequences: `for a, b in zip(list1, list2)` |
| **zip_longest** | Handle unequal lengths with `itertools.zip_longest` |
| **range(start, stop, step)** | Full control over numeric sequences |
| **Negative step** | `range(10, 0, -1)` counts backwards |
| **reversed()** | Cleaner than negative range for reversing sequences |
| **Nested loops** | Inner loop runs completely for each outer iteration |
