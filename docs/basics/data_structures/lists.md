# Lists

Lists are among Python's most valuable and frequently used data types, and they are the heart
of countless programs. 📋 So, what exactly is a `list`, and why are they so indispensable?

In essence, a `list` is a dynamic and mutable sequence of values. Think of it as a versatile
bag storing various items—numbers, words, and even a medley of data types—all within a single
container. This flexibility makes lists an invaluable asset for any Python programmer.

??? tip

    Closely related to lists are [tuples](tuples.md), which are *immutable*, but can be
    managed with similar syntax.

Let’s explore the concept further with a real-world analogy. Imagine you have a collection of
names, distances, and mixed data types like this:

``` python {title="Example Python Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
distance_in_kms = [32, 97, 51, 403, 21, 53, 81]
mixed_types = ["Jim", 23, 3.14, True, "Berzerk"]
```

In this example, `users` contains a `list` of names of `string` types, `distance_in_kms` stores
a `list` of distances in `int` type, and `mixed_types` seemingly defies convention by accommodating
a diverse set of data types. Lists are compelling because they allow you to organize and manipulate
such data effortlessly.

## Accessing List Items

List items can be accessed via their index system like this:

``` python {title="Accessing List Items via Indexc" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
print(f"What is your favourite moment when {users[0]} pulls a prank on {users[1]}?")
```

Returns:

``` text
What is your favourite moment when Jim pulls a prank on Dwight?
```

Lists can even be accessed through negative indexing like this:

``` python {title="Negative Indexing of Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
print(f"What was one thing that {users[-1]} did you found extra funny?")
```

Outputs:

``` text
What was one thing that Michael did you found extra funny?
```

## Adding and Removing Items from Lists

What makes lists genuinely exceptional is their *mutability*. Unlike some data types in Python,
lists can change and adapt as your program runs. Flexible, like a good morning stretch. 🧘 Adding, removing, or modifying elements within
a list makes it a dynamic tool for handling evolving data. This adaptability is particularly
useful when managing data collections that may grow or shrink in size.

``` python {title="Appending Items to Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
users.append("Pam")
print(f"We've added {users[-1]} to the list!")
```

Results in:
``` text
We've added Pam to the list!
```

### More Ways to Add Items

``` python {title="Insert at Specific Position" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
users.insert(1, "Andy")  # Insert at index 1
print(users)  # ['Jim', 'Andy', 'Dwight', 'Michael']

# Extend with multiple items
users.extend(["Pam", "Angela"])
print(users)  # ['Jim', 'Andy', 'Dwight', 'Michael', 'Pam', 'Angela']

# You can also use + to concatenate lists
more_users = users + ["Kevin", "Oscar"]
print(more_users)
```

### Removing Items

``` python {title="Removing List Items" linenums="1"}
users = ["Jim", "Dwight", "Michael", "Andy", "Pam"]

# Remove by value (first occurrence only)
users.remove("Andy")
print(users)  # ['Jim', 'Dwight', 'Michael', 'Pam']

# Remove by index and get the value back
last_user = users.pop()      # Removes and returns last item
print(f"Removed: {last_user}")  # Removed: Pam

second_user = users.pop(1)   # Remove at index 1
print(f"Removed: {second_user}")  # Removed: Dwight

# Remove by index without returning
del users[0]
print(users)  # ['Michael']

# Clear the entire list
users.clear()
print(users)  # []
```

!!! warning "Removing Non-existent Items"

    `remove()` raises a `ValueError` if the item doesn't exist. Use `if item in list:` first,
    or wrap in a try/except block.

## List Methods

Lists come with many useful built-in methods:

``` python {title="Useful List Methods" linenums="1"}
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Count occurrences
print(numbers.count(1))  # 2
print(numbers.count(7))  # 0

# Find index of first occurrence
print(numbers.index(5))  # 4
# numbers.index(99)  # ValueError if not found!

# Reverse in place
numbers.reverse()
print(numbers)  # [3, 5, 6, 2, 9, 5, 1, 4, 1, 3]

# Get length
print(len(numbers))  # 10
```

## Sorting Lists

Python offers two ways to sort: `sort()` modifies the list in place, while `sorted()`
returns a new sorted list. Knowing when to use each is like knowing when to brew fresh coffee
versus reheating yesterday's — one gives you something new, the other changes what you've got. ☕

``` python {title="Sorting Lists" linenums="1"}
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort in place (modifies original)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort in reverse
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() returns a NEW list, leaving original unchanged
original = [3, 1, 4, 1, 5]
sorted_copy = sorted(original)
print(original)     # [3, 1, 4, 1, 5] — unchanged!
print(sorted_copy)  # [1, 1, 3, 4, 5]
```

### Sorting with a Key Function

For complex sorting, use the `key` parameter:

``` python {title="Sorting with Key" linenums="1"}
words = ["banana", "pie", "Washington", "a"]

# Sort by length
words.sort(key=len)
print(words)  # ['a', 'pie', 'banana', 'Washington']

# Sort case-insensitively
words = ["banana", "Apple", "cherry"]
words.sort(key=str.lower)
print(words)  # ['Apple', 'banana', 'cherry']

# Sort objects by attribute
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
users.sort(key=lambda u: u["age"])
print([u["name"] for u in users])  # ['Bob', 'Alice', 'Charlie']
```

## Copying Lists

Be careful when copying lists — assignment creates a *reference*, not a copy!

``` python {title="The Aliasing Trap" linenums="1"}
original = [1, 2, 3]
alias = original  # Both point to the SAME list!

alias.append(4)
print(original)  # [1, 2, 3, 4] — original changed too! 😱
```

### Shallow Copy

Creates a new list, but nested objects are still shared:

``` python {title="Shallow Copy" linenums="1"}
original = [1, 2, 3]

# Three ways to shallow copy
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

copy1.append(4)
print(original)  # [1, 2, 3] — original unchanged ✅
print(copy1)     # [1, 2, 3, 4]
```

### Deep Copy (for Nested Lists)

For lists containing other lists or objects, you need a deep copy:

``` python {title="Deep Copy" linenums="1"}
import copy

original = [[1, 2], [3, 4]]

shallow = original.copy()
deep = copy.deepcopy(original)

# Modify nested list
shallow[0].append(999)
print(original)  # [[1, 2, 999], [3, 4]] — shallow copy shares nested lists!
print(shallow)   # [[1, 2, 999], [3, 4]]
print(deep)      # [[1, 2], [3, 4]] — deep copy is independent ✅
```

!!! tip "When to Deep Copy"

    Use `copy.deepcopy()` when your list contains:

    - Other lists or dicts
    - Custom objects
    - Any mutable nested structures

    For flat lists of immutable items (numbers, strings), shallow copy is fine.

## List Operations

``` python {title="List Operations" linenums="1"}
# Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

# Repetition
d = [0] * 5
print(d)  # [0, 0, 0, 0, 0]

# But be careful with mutable items!
matrix = [[0]] * 3  # Creates 3 references to the SAME list!
matrix[0].append(1)
print(matrix)  # [[0, 1], [0, 1], [0, 1]] — all changed! 😱

# Correct way for nested lists:
matrix = [[0] for _ in range(3)]
matrix[0].append(1)
print(matrix)  # [[0, 1], [0], [0]] — only first changed ✅
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Creating** | `[1, 2, 3]` or `list()` |
| **Accessing** | Zero-indexed: `list[0]`, negative: `list[-1]` |
| **Adding** | `append()`, `insert(i, x)`, `extend()`, `+` |
| **Removing** | `remove(x)`, `pop()`, `pop(i)`, `del`, `clear()` |
| **Sorting** | `list.sort()` in-place, `sorted(list)` returns new |
| **Key sorting** | `sort(key=len)` or `sort(key=lambda x: ...)` |
| **Shallow copy** | `list.copy()`, `list[:]`, `list(original)` |
| **Deep copy** | `copy.deepcopy(list)` for nested structures |
| **Gotcha** | `a = b` creates alias, not copy! |