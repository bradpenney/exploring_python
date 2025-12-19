# Slicing Sequences

Slicing is a powerful technique that allows you to extract specific portions of data from
Python sequences such as [lists](lists.md), [strings](../data_types/strings.md), and
[tuples](tuples.md). 🔪 (The good kind of slicing, not the kitchen mishap kind.) It provides you with the ability to finely control what data you need,
whether it’s from the beginning, end, or anywhere in between. This slicing capability is
governed by both positive and negative index systems, making it a versatile tool for data
manipulation.

### Slicing Index System

``` text
Positive index system
  0      1      2      3      4      5      6
Negative index system
 -7     -6     -5     -4     -3     -2     -1
```

Consider the following index systems for a list:

``` python {title="Indexing Sequences" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

print(days[-2])
print(days[2])
```

Results in:

``` text
Saturday
Wednesday
```

Easily access specific portions of a list using slicing. For example, to access the 2nd, 3rd,
and 4th items of a list named days, you can use the following code:

``` python {title="Slicing Lists" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

sliced_days = days[1:4]
print(sliced_days)
```

Would output:

``` text
['Tuesday', 'Wednesday', 'Thursday']
```

Retrieve the first three items of a list by simply omitting the starting index:

``` python {title="Retrieving First 3 Items in a List" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

first_three_days = days[:3]
print(first_three_days)
```

Would result in:

``` text
['Monday', 'Tuesday', 'Wednesday']
```

To get the last three items, you can use negative indexing:

``` python {title="Negative Slicing of Lists" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

last_three_days = days[-3:]
print(last_three_days)
```

Outputs:

``` text
['Friday', 'Saturday', 'Sunday']
```

For everything except the last item, exclude it by slicing until one element from the end:

``` python {title="Exclude the Last Item in a List" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

everything_but_last = days[:-1]
print(everything_but_last)
```

Results in:

``` text
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
```

Similarly, you can exclude the last two items:

``` python {title="Exclude the Last 2 Items in a List" linenums="1"}
days = ["Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
    ]

everything_but_last_two = days[:-2]
print(everything_but_last_two)
```

Returns:

``` text
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```

## Slicing Strings and Tuples

Strings and tuples share the same slicing principles as lists. You can effortlessly extract
portions of text from a string or elements from a tuple using slicing. For example, consider
this example:

``` python {title="Slicing Strings" linenums="1"}
text = "Hello, World!"
sliced_text = text[7:12]
print(sliced_text)
```

Would output:

``` text
World
```

## Step Slicing

The full slice syntax is `sequence[start:stop:step]`. The `step` parameter controls
how many items to skip:

``` python {title="Step Slicing" linenums="1"}
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every second item
print(numbers[::2])   # [0, 2, 4, 6, 8]

# Every third item
print(numbers[::3])   # [0, 3, 6, 9]

# Every second item, starting from index 1
print(numbers[1::2])  # [1, 3, 5, 7, 9]

# From index 1 to 7, every second item
print(numbers[1:8:2])  # [1, 3, 5, 7]
```

### Reversing with Negative Step

A negative step traverses the sequence backwards. This is the Pythonic way to reverse:

``` python {title="Negative Step (Reversing)" linenums="1"}
numbers = [0, 1, 2, 3, 4, 5]

# Reverse the entire sequence
print(numbers[::-1])  # [5, 4, 3, 2, 1, 0]

# Reverse a string
text = "Hello, World!"
print(text[::-1])  # !dlroW ,olleH

# Every second item, reversed
print(numbers[::-2])  # [5, 3, 1]

# From index 4 to 1, backwards
print(numbers[4:0:-1])  # [4, 3, 2, 1]
```

!!! tip "Palindrome Check"

    The `[::-1]` trick makes checking palindromes elegant:

    ```python
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]

    print(is_palindrome("A man a plan a canal Panama"))  # True
    ```

## Slice Assignment

For mutable sequences like lists, you can assign to a slice to modify multiple elements
at once:

``` python {title="Basic Slice Assignment" linenums="1"}
numbers = [0, 1, 2, 3, 4, 5]

# Replace a portion
numbers[1:4] = [10, 20, 30]
print(numbers)  # [0, 10, 20, 30, 4, 5]

# Replace with different length (insert/delete)
numbers[1:4] = [100]
print(numbers)  # [0, 100, 4, 5]

# Insert without removing
numbers[1:1] = [7, 8, 9]
print(numbers)  # [0, 7, 8, 9, 100, 4, 5]

# Delete a portion
numbers[1:4] = []
print(numbers)  # [0, 100, 4, 5]
```

### Replacing All Elements

``` python {title="Replacing All Elements" linenums="1"}
original = [1, 2, 3]
backup = original  # Both point to same list

# This creates a NEW list (backup still points to old one)
original = [4, 5, 6]
print(backup)  # [1, 2, 3]

# This modifies IN PLACE (backup sees the change)
original = [1, 2, 3]
backup = original
original[:] = [4, 5, 6]
print(backup)  # [4, 5, 6] — same object, modified!
```

## Slice Objects

You can create reusable slice objects:

``` python {title="Slice Objects" linenums="1"}
# Create a slice object
first_three = slice(0, 3)
every_other = slice(None, None, 2)
last_two = slice(-2, None)

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(data[first_three])   # [0, 1, 2]
print(data[every_other])   # [0, 2, 4, 6, 8]
print(data[last_two])      # [8, 9]

# Useful when same slice is used on multiple sequences
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 92, 78, 95, 88]

top_three = slice(0, 3)
print(names[top_three])   # ['Alice', 'Bob', 'Charlie']
print(scores[top_three])  # [85, 92, 78]
```

## Common Slicing Patterns

These patterns come up constantly. Memorize them like your coffee order — you'll use
them every day.

``` python {title="Common Patterns" linenums="1"}
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# First N items
first_5 = data[:5]       # [0, 1, 2, 3, 4]

# Last N items
last_3 = data[-3:]       # [7, 8, 9]

# All except first N
skip_first_2 = data[2:]  # [2, 3, 4, 5, 6, 7, 8, 9]

# All except last N
skip_last_2 = data[:-2]  # [0, 1, 2, 3, 4, 5, 6, 7]

# Middle portion
middle = data[2:-2]      # [2, 3, 4, 5, 6, 7]

# Shallow copy
copy = data[:]           # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Reverse
reversed_data = data[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Slicing 2D Structures

When working with lists of lists (matrices), you need to slice each dimension:

``` python {title="Slicing 2D Data" linenums="1"}
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Get first two rows
print(matrix[:2])
# [[1, 2, 3, 4], [5, 6, 7, 8]]

# Get first column (need list comprehension)
first_col = [row[0] for row in matrix]
print(first_col)  # [1, 5, 9]

# Get a sub-matrix (first 2 rows, first 2 columns)
submatrix = [row[:2] for row in matrix[:2]]
print(submatrix)  # [[1, 2], [5, 6]]
```

!!! tip "For Heavy Matrix Work"

    For serious matrix operations, use NumPy which supports true multi-dimensional slicing:

    ```python
    import numpy as np
    arr = np.array(matrix)
    print(arr[:2, :2])  # First 2 rows, first 2 columns
    ```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Basic syntax** | `sequence[start:stop]` — stop is exclusive |
| **Omitting indices** | `[:3]` from start, `[3:]` to end, `[:]` copy all |
| **Negative indices** | `-1` is last, `-2` is second-to-last |
| **Step** | `[::2]` every other, `[::3]` every third |
| **Reverse** | `[::-1]` reverses any sequence |
| **Slice assignment** | `list[1:4] = [a, b]` — replace portion |
| **In-place modify** | `list[:] = [...]` modifies same object |
| **Slice objects** | `s = slice(0, 3)` — reusable slices |
| **Works on** | Lists, tuples, strings — any sequence |
