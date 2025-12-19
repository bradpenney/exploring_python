# For Loops

Process a list of email addresses. Analyze each line in a log file. Generate multiplication tables. Calculate statistics across datasets. Render pixels in an image.

Every one of these tasks requires doing the same operation repeatedly—just with different data each time. That's what **for loops** enable: systematic iteration over collections.

Computers excel at repetition without fatigue or error. For loops are how you harness that power in Python.

## What is a For Loop?

A for loop executes a block of code once for each item in a sequence (list, string, range, etc.):

```python title="Basic For Loop Structure" linenums="1"
for item in sequence:  # (1)!
    # Code to execute for each item
    print(item)
```

1. The loop variable (`item`) takes on each value from the sequence in order

Here's a concrete example:

```python title="Iterating Over a List" linenums="1"
languages = ["Python", "JavaScript", "Go"]
for language in languages:  # (1)!
    print(f"I'm learning {language}")
```

1. `language` becomes "Python", then "JavaScript", then "Go" on successive iterations

Output:
```text
I'm learning Python
I'm learning JavaScript
I'm learning Go
```

## Why For Loops Matter

For loops solve a fundamental problem: applying operations across collections without writing repetitive code. This is [computational thinking](https://cs.bradpenney.io/fundamentals/computational_thinking/) in action—decomposing a large task (process 1000 items) into a simple, repeatable pattern (process one item, repeat).

Without loops, processing three items requires three nearly-identical code blocks:

```python title="Without Loops (Don't Do This)" linenums="1"
print(f"Processing {items[0]}")
print(f"Processing {items[1]}")
print(f"Processing {items[2]}")
# What if you have 100 items? 10,000?
```

With loops, one block handles any number of items:

```python title="With Loops (Better)" linenums="1"
for item in items:  # (1)!
    print(f"Processing {item}")
```

1. Works for 3 items, 300 items, or 3 million items

Loops make your code:

- **Scalable**: Works with any collection size
- **Maintainable**: Change the logic once, not N times
- **Readable**: Expresses intent clearly

## Looping Over Different Sequences

### Lists

The most common use case—iterate over list elements:

```python title="Processing List Items" linenums="1"
scores = [85, 92, 78, 90, 88]
total = 0
for score in scores:  # (1)!
    total += score
average = total / len(scores)
print(f"Average score: {average}")
```

1. Each iteration, `score` takes on the next value from the list (85, then 92, then 78, etc.)

### Strings

Strings are sequences of characters, so you can loop over them:

```python title="Iterating Over Characters" linenums="1"
word = "Python"
for letter in word:  # (1)!
    print(letter)
```

1. Each character becomes the loop variable in turn

Output:
```text
P
y
t
h
o
n
```

### Dictionaries

Loop over keys, values, or both:

```python title="Dictionary Iteration" linenums="1"
user = {"name": "Alice", "age": 30, "city": "Boston"}

# Loop over keys
for key in user.keys():  # (1)!
    print(key)

# Loop over values
for value in user.values():  # (2)!
    print(value)

# Loop over key-value pairs
for key, value in user.items():  # (3)!
    print(f"{key}: {value}")
```

1. `.keys()` returns the dictionary keys—actually the default behavior
2. `.values()` returns just the values
3. `.items()` returns tuples of `(key, value)` pairs—note we unpack into two variables

Output of `.items()` loop:
```text
name: Alice
age: 30
city: Boston
```

??? tip "Dictionary Unpacking"

    `for key, value in user.items()` uses **tuple unpacking**. Each iteration, `.items()` returns a tuple like `("name", "Alice")`, which Python automatically unpacks into the two variables.

## The `range()` Function

Need to repeat an action exactly N times? Generate a sequence of IDs? Count from 1 to 100? The `range()` function generates number sequences for counted loops:

```python title="Basic Range Usage" linenums="1"
for i in range(5):  # (1)!
    print(i)
```

1. `range(5)` generates numbers from 0 to 4 (not including 5)

Output:
```text
0
1
2
3
4
```

!!! danger "Off-By-One Trap"

    `range()` stops **before** the end value. `range(10)` generates 0-9, not 1-10. This is Python's most common off-by-one error.

### Range with Start and Stop

Skip header rows when processing files. Process items 10-20 from a dataset. Generate IDs starting from a specific number:

```python title="Range with Start and Stop" linenums="1"
for i in range(3, 8):  # (1)!
    print(i)
```

1. `range(start, stop)` goes from start (inclusive) to stop (exclusive)

Output:
```text
3
4
5
6
7
```

### Range with Step

Process every other row in a spreadsheet. Sample data (take every 100th record). Generate sequences like even numbers or multiples of 5:

```python title="Range with Step" linenums="1"
for i in range(0, 10, 2):  # (1)!
    print(i)
```

1. `range(start, stop, step)` increments by step each time

Output:
```text
0
2
4
6
8
```

### Counting Backwards

Countdown timers. Processing undo stack (most recent first). Reverse iteration when building output in reverse order:

```python title="Counting Backwards" linenums="1"
for i in range(10, 0, -1):  # (1)!
    print(i)
print("Liftoff!")
```

1. Start at 10, stop before 0, decrement by 1

Output:
```text
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

## Looping with Indices: `enumerate()`

Displaying numbered lists ("1. First item, 2. Second item..."). Tracking position while processing. Comparing items to their neighbors by index. When you need both the value and its position, `enumerate()` provides both:

```python title="Enumerate for Index and Item" linenums="1"
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):  # (1)!
    print(f"{index}: {fruit}")
```

1. `enumerate()` yields tuples of `(index, item)` which we unpack

Output:
```text
0: apple
1: banana
2: cherry
```

Start counting from 1 instead of 0:

```python title="Enumerate with Custom Start" linenums="1"
for index, fruit in enumerate(fruits, start=1):  # (1)!
    print(f"{index}. {fruit}")
```

1. `start=1` makes the index begin at 1 instead of 0

Output:
```text
1. apple
2. banana
3. cherry
```

## Nested Loops

Multiplication tables. Processing 2D grids (chess boards, images, spreadsheets). Comparing every item with every other item. Nested loops handle multidimensional problems:

```python title="Nested Loops" linenums="1"
for i in range(1, 4):  # (1)!
    for j in range(1, 4):  # (2)!
        print(f"{i} × {j} = {i * j}")
    print()  # Blank line between groups
```

1. Outer loop runs 3 times
2. For each outer iteration, inner loop runs 3 times (total: 3 × 3 = 9 iterations)

Output:
```text
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3

2 × 1 = 2
2 × 2 = 4
2 × 3 = 6

3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
```

!!! warning "Performance Warning"

    Nested loops multiply execution time. Two loops of 100 items each = 10,000 iterations. Three loops of 100 = 1,000,000 iterations. Be mindful with large datasets.

## Looping Over Multiple Sequences: `zip()`

Combining first names with last names. Matching products with prices. Processing parallel lists of data. When you have related data in separate lists, `zip()` pairs them element-by-element:

```python title="Zipping Sequences" linenums="1"
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

for name, age in zip(names, ages):  # (1)!
    print(f"{name} is {age} years old")
```

1. `zip()` pairs corresponding elements: ("Alice", 30), ("Bob", 25), ("Charlie", 35)

Output:
```text
Alice is 30 years old
Bob is 25 years old
Charlie is 35 years old
```

If sequences differ in length, `zip()` stops at the shortest:

```python title="Zip Stops at Shortest" linenums="1"
a = [1, 2, 3]
b = ['a', 'b']
for num, letter in zip(a, b):  # (1)!
    print(num, letter)
```

1. Only 2 pairs are created because `b` has only 2 elements

Output:
```text
1 a
2 b
```

## Practical Patterns

### Accumulating Values

Calculate totals from transactions. Count how many items match a criterion. Find the maximum value. Track a running average:

```python title="Summing a List" linenums="1"
numbers = [10, 20, 30, 40]
total = 0  # (1)!
for num in numbers:
    total += num  # (2)!
print(total)
```

1. Initialize the accumulator variable to 0 before the loop starts
2. Add each number to the accumulator on each iteration (final result: 100)

### Building New Lists

Apply tax to prices. Convert temperatures from Celsius to Fahrenheit. Extract specific fields from records. Generate derived data:

```python title="Transforming List Values" linenums="1"
prices = [10.99, 5.99, 23.50]
prices_with_tax = []  # (1)!
for price in prices:
    with_tax = price * 1.13  # (2)!
    prices_with_tax.append(with_tax)
print(prices_with_tax)
```

1. Create an empty list to hold the results before the loop
2. Calculate the new value (price plus 13% tax) and append it to the results list

??? tip "List Comprehensions"

    Python has a more concise syntax for this pattern called **list comprehensions**. See the [Comprehensions](comprehensions.md) article for details.

### Filtering Data

Remove invalid email addresses. Find all orders above $100. Separate active from inactive users. Extract matching search results:

```python title="Finding Specific Items" linenums="1"
numbers = [15, 8, 23, 4, 16, 42]
even_numbers = []
for num in numbers:
    if num % 2 == 0:  # (1)!
        even_numbers.append(num)
print(even_numbers)  # [8, 4, 16, 42]
```

1. Only append items that meet the condition

## For vs While Loops

Python has two types of loops:

- **For loops**: "Do this for each item" (iteration over known sequences)
- **While loops**: "Do this until condition becomes false" (iteration until something happens)

Use for loops when you know what you're iterating over:

```python title="For Loop (Known Sequence)" linenums="1"
for i in range(10):  # (1)!
    print(i)
```

1. We know we want exactly 10 iterations

Use while loops when you don't know how many iterations you need:

```python title="While Loop (Unknown Count)" linenums="1"
user_input = ""
while user_input != "quit":  # (1)!
    user_input = input("Enter command (or 'quit'): ")
```

1. Loop until user types "quit"—we don't know how many iterations that takes

See [While Loops](while_loops.md) for more on while loops.

## Common Pitfalls

### Modifying a List While Iterating

Don't modify a list you're currently iterating over:

```python title="Dangerous: Modifying During Iteration" linenums="1"
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # (1)!
```

1. ⚠️ Don't do this! Modifying the list during iteration causes elements to be skipped—a subtle and dangerous bug

**Solution**: Iterate over a copy or build a new list:

```python title="Safe: Building New List" linenums="1"
numbers = [1, 2, 3, 4, 5]
odd_numbers = []
for num in numbers:  # (1)!
    if num % 2 != 0:
        odd_numbers.append(num)
```

1. Iterate over original, build new list—safe and clear

### Range Off-By-One Error

```python title="Range Excludes End Value" linenums="1"
for i in range(10):
    print(i)  # (1)!
```

1. Prints 0-9, not 1-10! `range(10)` generates 0, 1, 2, ..., 9 (stops before 10)

To iterate from 1 to 10:

```python title="Correct Range for 1-10" linenums="1"
for i in range(1, 11):  # (1)!
    print(i)
```

1. Start at 1, stop before 11 (so last value is 10)

## Practice Problems

??? question "Practice Problem 1: Basic Iteration"

    Write a for loop that prints each character in the string `"Python"` on a separate line.

    ??? tip "Answer"

        ```python
        word = "Python"
        for letter in word:
            print(letter)
        ```

        Strings are sequences, so you can iterate over their characters.

??? question "Practice Problem 2: Range Usage"

    What does this code print?

    ```python
    for i in range(3, 10, 2):
        print(i)
    ```

    ??? tip "Answer"

        ```text
        3
        5
        7
        9
        ```

        `range(3, 10, 2)` starts at 3, stops before 10, increments by 2 each time.

??? question "Practice Problem 3: Enumerate"

    How would you print each item in `fruits = ["apple", "banana", "cherry"]` with its position number starting from 1?

    ??? tip "Answer"

        ```python
        fruits = ["apple", "banana", "cherry"]
        for index, fruit in enumerate(fruits, start=1):
            print(f"{index}. {fruit}")
        ```

        `enumerate(fruits, start=1)` yields `(1, "apple")`, `(2, "banana")`, `(3, "cherry")`.

??? question "Practice Problem 4: Accumulation"

    Write a loop that calculates the product of all numbers in `[2, 3, 4, 5]`.

    ??? tip "Answer"

        ```python
        numbers = [2, 3, 4, 5]
        product = 1  # Start at 1 (not 0!) for multiplication
        for num in numbers:
            product *= num
        print(product)  # 120 (2 × 3 × 4 × 5)
        ```

        For multiplication, initialize the accumulator to 1, not 0.

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **For loop** | Execute code once for each item in a sequence |
| **`range()`** | Generate sequences of numbers: `range(start, stop, step)` |
| **`enumerate()`** | Get both index and item: `for i, item in enumerate(seq)` |
| **`zip()`** | Pair elements from multiple sequences |
| **Loop variable** | Takes on each value from the sequence in turn |
| **Nested loops** | Loops inside loops—useful for multidimensional data |

## Further Reading

- [**Python For Loops Tutorial**](https://docs.python.org/3/tutorial/controlflow.html#for-statements) - Official Python documentation
- [**Itertools Module**](https://docs.python.org/3/library/itertools.html) - Advanced iteration tools
- [**List Comprehensions**](comprehensions.md) - More concise syntax for common loop patterns
- [**While Loops**](while_loops.md) - Loops based on conditions rather than sequences

---

For loops are one of the first control structures you'll learn, and one you'll use daily. They transform repetitive manual work into systematic, scalable operations. Master iteration—over lists, strings, ranges, and dictionaries—and you can process any collection Python throws at you.

Every complex program is built on simple loops. Learn to write them well.
