# Lists

You need to track a shopping list. Process log file entries. Store user responses. Manage a collection of database records. What do all these tasks have in common?

They require storing multiple values in a single, flexible data structure. In Python, that structure is the **list**.

Lists are ordered, mutable sequences—arguably Python's most versatile data structure. You'll use them constantly, from small scripts to large applications. Understanding lists deeply transforms what you can build.

## What is a List?

A list is an ordered collection of items, defined with square brackets:

```python title="Creating Lists" linenums="1"
fruits = ["apple", "banana", "cherry"]  # (1)!
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 30, 3.14, True]  # (2)!
empty = []  # (3)!
```

1. Lists are created with square brackets `[...]` and items separated by commas
2. Lists can contain different types—strings, numbers, booleans, even other lists
3. Empty lists are valid and common as starting points

Lists maintain insertion order and allow duplicates:

```python title="Order and Duplicates" linenums="1"
colors = ["red", "blue", "red", "green"]  # (1)!
print(colors[0])  # "red" - first item
print(colors[2])  # "red" - third item (duplicate)
```

1. Lists preserve order and permit duplicate values

## Why Lists Matter

Lists solve a fundamental programming problem: managing collections of related data. This reflects core [computational thinking](https://cs.bradpenney.io/fundamentals/computational_thinking/)—abstracting individual items into structured collections you can process systematically.

- **User input**: Store multiple form entries, search queries, uploaded files
- **Data processing**: Read CSV rows, parse log lines, accumulate results
- **Game development**: Track inventory items, enemy positions, player scores
- **Web scraping**: Collect links, extract product details, gather search results
- **APIs**: Process JSON arrays, build request parameters, aggregate responses

Without lists (or similar structures), you'd need separate variables for every value. Three users? `user1`, `user2`, `user3`. Ten users? This doesn't scale. Lists do.

## Accessing List Elements

Display the first search result. Get the last log entry. Process every third item. Skip the header row in a CSV file. All require accessing specific positions in a list.

Lists use zero-based indexing:

```python title="List Indexing" linenums="1"
languages = ["Python", "JavaScript", "Go", "Rust"]
print(languages[0])   # (1)!
print(languages[2])
print(languages[-1])  # (2)!
print(languages[-2])
print(len(languages)) # (3)!
```

1. Returns `"Python"` - Python uses zero-based indexing so the first element is at index 0
2. Returns `"Rust"` - negative indices count backward from the end: -1 is last, -2 is second-to-last
3. Returns `4` - `len()` returns the total number of elements in the list

Attempting to access an invalid index raises an `IndexError`:

```python title="Index Out of Range" linenums="1"
fruits = ["apple", "banana"]
print(fruits[0])      # (1)!
print(fruits[1])      # (2)!
# print(fruits[5])    # Would raise IndexError!
```

1. Returns `"apple"` - valid index (list has indices 0 and 1)
2. Returns `"banana"` - the last valid index

Accessing `fruits[5]` would raise `IndexError: list index out of range` since only indices 0 and 1 exist.

## List Mutability: Changing Lists

Users add items to shopping carts. You filter invalid entries from data. Tasks get completed and removed. Collections grow and shrink as programs run. This is why lists are mutable—they reflect dynamic, changing data.

Unlike [strings](../data_types/strings.md), lists are **mutable**—they can be modified after creation:

### Adding Elements

**Appending** - User adds item to shopping cart. You're accumulating search results. Building a list of errors as you validate data:

```python title="Appending to Lists" linenums="1"
tasks = ["email", "code review"]
tasks.append("meeting")  # (1)!
print(tasks)  # ["email", "code review", "meeting"]
```

1. `.append()` adds an element to the end—the most common way to grow lists

**Inserting** - Adding a high-priority task at the top of a todo list. Inserting a header row into CSV data. Maintaining sorted order while building a list:

```python title="Inserting at Specific Positions" linenums="1"
numbers = [1, 2, 4]
numbers.insert(2, 3)  # (1)!
print(numbers)  # [1, 2, 3, 4]
```

1. `.insert(index, value)` adds an element at the specified position

**Extending** - Merging results from multiple API calls. Combining data from different sources. Loading additional items as user scrolls (pagination):

```python title="Extending with Multiple Items" linenums="1"
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # (1)!
print(list1)  # [1, 2, 3, 4, 5, 6]
```

1. `.extend()` adds all items from another list—different from `.append()` which adds the entire list as a single element

### Removing Elements

User removes item from cart. Filter out invalid entries during data cleaning. Task completed and needs removal from active list:

```python title="Removing Items" linenums="1"
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")  # (1)!
print(fruits)  # ["apple", "cherry", "banana"]

popped = fruits.pop()  # (2)!
print(popped)  # "banana"
print(fruits)  # ["apple", "cherry"]

first = fruits.pop(0)  # (3)!
print(first)  # "apple"
print(fruits)  # ["cherry"]
```

1. `.remove(value)` removes the first occurrence of the value
2. `.pop()` removes and returns the last element
3. `.pop(index)` removes and returns the element at the specified index

```python title="Deleting by Index" linenums="1"
numbers = [10, 20, 30, 40]
del numbers[1]  # (1)!
print(numbers)  # [10, 30, 40]
```

1. `del` removes an element by index—useful but doesn't return the value

### Modifying Elements

Update a score after recalculation. Correct an error in imported data. Apply a transformation to a specific position:

```python title="Changing Values" linenums="1"
scores = [85, 90, 78]
scores[1] = 95  # (1)!
print(scores)  # [85, 95, 78]
```

1. Assign to an index to change the value at that position

## Sorting and Reversing

Leaderboards rank scores. Product listings sort by price. Search results order by relevance. Log entries display newest first. Sorting and reversing are essential for presenting data meaningfully:

```python title="Sorting Lists" linenums="1"
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # (1)!
print(numbers)  # [1, 1, 3, 4, 5, 9]

words = ["zebra", "apple", "banana"]
words.sort(reverse=True)  # (2)!
print(words)  # ["zebra", "banana", "apple"]
```

1. `.sort()` sorts the list in place—modifies the original list
2. `reverse=True` sorts in descending order

```python title="Sorted Without Modifying" linenums="1"
original = [3, 1, 4]
sorted_copy = sorted(original)  # (1)!
print(original)      # [3, 1, 4] - unchanged
print(sorted_copy)   # [1, 3, 4] - new sorted list
```

1. `sorted()` returns a new sorted list—original remains unchanged

```python title="Reversing Lists" linenums="1"
items = [1, 2, 3, 4]
items.reverse()  # (1)!
print(items)  # [4, 3, 2, 1]
```

1. `.reverse()` reverses the list in place

## Checking Membership

Is this username already taken? Does the shopping cart contain this item? Has this email been processed? Membership testing answers these questions efficiently:

```python title="Testing Membership" linenums="1"
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # (1)!
print("grape" in fruits)
print("grape" not in fruits) # (2)!
```

1. Returns `True` - the `in` operator checks if an element exists in the list
2. Returns `True` - the `not in` operator checks if an element doesn't exist

## List Slicing

Show the top 10 search results. Process data in batches of 100. Get the last 5 log entries. Display page 3 of results (items 20-30). Slicing extracts exactly the portion you need:

Slicing extracts portions of a list:

```python title="Slicing Lists" linenums="1"
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # (1)!
print(numbers[:3])    # (2)!
print(numbers[3:])
print(numbers[-2:])
print(numbers[::2])   # (3)!
```

1. Returns `[1, 2, 3]` - slicing uses `[start:end]` which includes start but excludes end
2. Returns `[0, 1, 2]` - omitting start slices from the beginning
3. Returns `[0, 2, 4]` - the third parameter is step: `[start:end:step]`

Slices create new lists—they don't modify the original:

```python title="Slicing Creates Copies" linenums="1"
original = [1, 2, 3, 4]
subset = original[1:3]  # (1)!
subset[0] = 99
print(original)  # [1, 2, 3, 4] - unchanged
print(subset)    # [99, 3] - modified
```

1. Slices are shallow copies—modifying the slice doesn't affect the original

## Common Patterns

### Iterating Over Lists

Process each email in an inbox. Validate every form field. Send notifications to all subscribers:

```python title="Looping Through Lists" linenums="1"
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:  # (1)!
    print(f"I like {fruit}")
```

1. The most Pythonic way to iterate—directly over elements, not indices (see [For Loops](../control_structures/for_loops.md))

### Finding Elements

Locate where a specific user appears in a list. Count how many times an error occurred. Find the position of a selected item:

```python title="Finding Index of Element" linenums="1"
colors = ["red", "green", "blue", "green"]
index = colors.index("green")  # (1)!
print(index)  # 1 - first occurrence

count = colors.count("green")  # (2)!
print(count)  # 2 - number of occurrences
```

1. `.index(value)` returns the index of the first occurrence (raises ValueError if not found)
2. `.count(value)` returns how many times the value appears

### Copying Lists

Preserve original data before modifications. Create a backup before filtering. Pass a copy to a function that might modify it:

```python title="Copying Lists" linenums="1"
original = [1, 2, 3]
shallow_copy = original.copy()  # (1)!
another_copy = original[:]      # (2)!

shallow_copy.append(4)
print(original)      # [1, 2, 3] - unchanged
print(shallow_copy)  # [1, 2, 3, 4]
```

1. `.copy()` creates a shallow copy—explicit and readable
2. `[:]` (slice everything) also creates a copy—common idiom

## Lists vs. Tuples

Python has another sequence type called **tuples**, which are immutable:

```python title="Lists vs Tuples" linenums="1"
my_list = [1, 2, 3]   # Mutable - can change
my_tuple = (1, 2, 3)  # Immutable - cannot change (1)!

my_list[0] = 99   # ✓ Allowed
# my_tuple[0] = 99  # ✗ TypeError!
```

1. Tuples use parentheses `(...)` instead of brackets `[...]`

Use lists when you need a collection that can grow, shrink, or change. Use tuples for fixed collections. (See the [Tuples](tuples.md) article for details.)

## Practice Problems

??? question "Practice Problem 1: Indexing"

    Given `names = ["Alice", "Bob", "Charlie", "Diana"]`, what does `names[-2]` return?

    ??? tip "Answer"

        It returns `"Charlie"` (the second-to-last element). Negative indices count from the end: `-1` is last, `-2` is second-to-last, etc.

??? question "Practice Problem 2: Mutability"

    What's the difference between `.append([1, 2])` and `.extend([1, 2])` when called on a list?

    ??? tip "Answer"

        ```python
        list1 = [0]
        list1.append([1, 2])
        print(list1)  # [0, [1, 2]] - adds the entire list as a single element

        list2 = [0]
        list2.extend([1, 2])
        print(list2)  # [0, 1, 2] - adds each element individually
        ```

        `.append()` adds its argument as a single element. `.extend()` adds each element from an iterable.

??? question "Practice Problem 3: Slicing"

    How would you get the last 3 elements of a list without knowing its length?

    ??? tip "Answer"

        ```python
        numbers = [1, 2, 3, 4, 5, 6, 7]
        last_three = numbers[-3:]
        print(last_three)  # [5, 6, 7]
        ```

        `[-3:]` means "from third-from-end to the end"—works regardless of list length.

??? question "Practice Problem 4: Removing Elements"

    What's the difference between `.remove(value)` and `.pop(index)`?

    ??? tip "Answer"

        - `.remove(value)` finds and removes the first occurrence of a value (raises ValueError if not found)
        - `.pop(index)` removes and returns the element at a specific index (raises IndexError if invalid)

        ```python
        fruits = ["apple", "banana", "cherry"]
        fruits.remove("banana")  # Removes by value
        print(fruits)  # ["apple", "cherry"]

        numbers = [10, 20, 30]
        removed = numbers.pop(1)  # Removes by index, returns value
        print(removed)  # 20
        print(numbers)  # [10, 30]
        ```

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **List** | Ordered, mutable collection of items |
| **Mutability** | Lists can be modified after creation (unlike [strings](../data_types/strings.md) or [tuples](tuples.md)) |
| **Indexing** | Access elements by position (zero-based, negative from end) |
| **Slicing** | Extract portions: `[start:end:step]` |
| **`.append()`** | Add single element to end |
| **`.extend()`** | Add multiple elements from iterable |
| **`.remove()`** | Remove first occurrence of value |
| **`.pop()`** | Remove and return element by index |

## Further Reading

- [**Python List Documentation**](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) - Official tutorial on lists
- [**Time Complexity of List Operations**](https://wiki.python.org/moin/TimeComplexity) - Performance characteristics
- [**List Comprehensions**](../control_structures/comprehensions.md) - Elegant way to create lists
- [**Sorting HOW TO**](https://docs.python.org/3/howto/sorting.html) - Advanced sorting techniques

---

Lists are the workhorse of Python data structures. They're flexible enough for quick scripts and powerful enough for production systems. Learn to use them fluently—appending, slicing, sorting, iterating—and you'll handle most data management tasks with ease.

Arrays in C require fixed sizes. JavaScript arrays have quirky behavior. Python lists just work, with intuitive methods and predictable semantics. That's part of what makes Python a joy to use.
