# Dictionaries

Dictionaries are one of the most important data structures in Python — and they're *everywhere*. 📖
Even when you don't see them directly, they're often working behind the scenes, quietly holding
things together.

For instance, while a string like `"hello"` isn’t itself a dictionary, many
Python objects (including strings) use internal dictionaries to store
attributes and metadata. And when you assign `a = "my_name"`, you're creating
a name (`a`) that points to a string object — which, like most Python objects,
has a dictionary of attributes under the hood.

The real magic of dictionaries is **association**. Linking keys to values
(`key: value`) creates fast and flexible lookups. Want to find a user’s email
by their username? Dictionary. Want to count how many times something appears?
Dictionary.

If you’ve used other programming languages, you might have heard these referred
to as *associative arrays*, *hash maps*, or just *maps*. It’s the same core
idea: match a key to a value. Think of it like an old-school phone book — you
know the name, and the dictionary gives you the number.

Dictionaries are a much less compute-intensive way to associate two values than say, keeping those
values in two lists (where the order is guaranteed). In fact, the lookup speed of a dictionary is
not affected by its size! ⚡ That's some serious performance.

??? tip

    Every key in a dictionary must be *unique* and *hashable*.  In practical
    terms, this means you can't use a *mutable* object as keys - so you can't
    use a `list` or a `dict` as as a key in a dictionary. This will throw a
    `TypeError` exception. Mutable objects **can** be assigned as values.
    For example, trying to assign the list `engine_parts` with
    `dream_car['engine_parts'] = 563`throws an error:

        Traceback (most recent call last):
        File "/home/brad/Documents/exploring_python/basics/data_structures/dictionaries.py", line 17, in <module>
            dream_car[engine_parts] = 563
            ~~~~~~~~~~^^^^^^^^^^^^^^
        TypeError: unhashable type: 'list'

The data type of a dictionary in Python is `dict`, and they're iterable, even
though they're not a sequence type like a [`list`](lists.md) or `set`. In lists,
you can insert a value at a specific index position in the sequence. With
dictionaries, position is determined by *insertion order*—new items are always
appended to the end. When iterating over a dictionary (see below), iteration
will always happen in insertion order. This isn't an index, but the natural
order of dictionaries.

??? info

    Prior to Python `v3.6`, there was no guaranteed order of dictionaries at all.
    As of `v3.6`, this changed, and dictionaries are guaranteed to iterate over
    the insertion order.

## Creating a Dictionary

Dictionaries can be declared with:

``` python {title="Creating a Dictionary" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}
```

To retrieve a value, use square brackets `[]` and supply a key (not an index
like a list):

``` python
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']}")
```

Would return:

``` text
Dream car: 1971 Ford Pinto
```

## Inserting or Changing a Value

You can insert or update a key/value pair using the same square bracket syntax
with an assignment:

```python {title="Inserting and Updating Key/Value Pairs" linenums="1"}
dream_car['make'] = "Ferrari"
dream_car['model'] = "365 GTS/4 Daytona"
dream_car['colour'] = "Rosso Chiaro"
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']} of the colour {dream_car['colour']}.")
```

This would output:

``` text
Dream car: 1971 Ferrari 365 GTS/4 Daytona of the colour Rosso Chiaro.
```

## Deleting a Key/Value Pair

Removing an entry is as easy as using the `del` keyword:

``` python {title="Deleting a Key/Value Pair" linenums="1"}
del dream_car['colour']
```

## Avoiding `KeyError` with `get()`

Attempting to read or delete a key that doesn’t exist will raise a `KeyError`
exception. For example, attempting to retrieve `dream_car['engine']` would
result in:

``` text
Traceback (most recent call last):
File "exploring_python/basics/data_structures/dictionaries.py", line 19, in <module>
    dream_car['engine']
    ~~~~~~~~~^^^^^^^^^^
KeyError: 'engine'
```

The `dict.get()` method tries to find a key in a dictionary and will not raise
an error if that key doesn't exist. Even better, you can assign a default value
to return if the key is missing (the default is `None`). So, if you search for
a key and it isn't present, the default value will be returned:

``` python {title="Creating a Dictionary" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

print(dream_car.get('engine', 'V8'))
```

Returns:

``` text
V8
```

???+ tip

    Note that the key/value pair `engine: V8` isn't inserted into the
    dictionary. Instead, this one-time value is returned to avoid throwing
    a `KeyError`.

## Clearing a Dictionary

If the data in a dictionary is no longer valuable, but you'd like to keep
the same dictionary object, use the `clear()` method to empty a dictionary
without changing the id.

``` python {title="Clear a Dictionary but Keep the Object" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400
}

print(f"Dream Car Object ID: {id(dream_car)}")
dream_car.clear()
print(f"Dream Car after clear: {dream_car}")
print(f"Dream Car Object ID after clear: {id(dream_car)}")
```

Results in:

``` text
Dream Car Object ID: 140457216790016
Dream Car after clear: {}
Dream Car Object ID after clear: 140457216790016
```

## Merging Dictionaries

Dictionaries often store related data, so merging them is a common task.
To do this, use the `update()` method. When you call `update()`, the
dictionary you pass in will **merge** with the original dictionary:
it will **update** any values with the **same key** and **add** any
key/value pairs that did not exist in the original dictionary.

``` python {title="Merging Dictionaries" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400
}

dream_car_engine = {
    "engine": "V8",
    "horsepower": 440,
    "cylinders": 8
}

dream_car.update(dream_car_engine) # (1)
print(f"Dream Car: {dream_car}")
print(f"Dream Car Engine: {dream_car_engine}")
```

1. The `update()` method is also available, with similar functionality, in
   [`sets`](sets.md#adding-elements)

Would output:

``` text
Dream Car: {'model': 'Pinto', 'make': 'Ford', 'year': 1971, 'mileage': 400, 'engine': 'V8', 'horsepower': 440, 'cylinders': 8}
Dream Car Engine: {'engine': 'V8', 'horsepower': 440, 'cylinders': 8}
```

Note how `dream_car_engine` was not modified by the `update()` function,
only `dream_car`.

### Merge Operator (Python 3.9+)

Python 3.9 introduced the `|` operator for merging dictionaries:

``` python {title="Merge Operator" linenums="1"}
defaults = {"theme": "dark", "font_size": 12, "language": "en"}
user_prefs = {"font_size": 14, "sidebar": True}

# Merge (user_prefs values win on conflict)
combined = defaults | user_prefs
print(combined)
# {'theme': 'dark', 'font_size': 14, 'language': 'en', 'sidebar': True}

# Update in place
defaults |= user_prefs
print(defaults)
# {'theme': 'dark', 'font_size': 14, 'language': 'en', 'sidebar': True}
```

## The setdefault() Method

`setdefault()` gets a value if the key exists, or sets it to a default if it doesn't:

``` python {title="setdefault()" linenums="1"}
inventory = {"apples": 5, "bananas": 3}

# Key exists — just returns the value
count = inventory.setdefault("apples", 0)
print(count)       # 5
print(inventory)   # {'apples': 5, 'bananas': 3}

# Key doesn't exist — sets it and returns the default
count = inventory.setdefault("oranges", 0)
print(count)       # 0
print(inventory)   # {'apples': 5, 'bananas': 3, 'oranges': 0}
```

This is particularly useful for building up collections:

``` python {title="Building Lists in a Dict" linenums="1"}
# Grouping items by category
items = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana")]

grouped = {}
for category, item in items:
    grouped.setdefault(category, []).append(item)

print(grouped)
# {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
```

## Dictionary Comprehensions

Just like [list comprehensions](../control_structures/comprehensions.md), you can create
dictionaries with a concise syntax:

``` python {title="Dict Comprehensions" linenums="1"}
# Basic: {key_expr: value_expr for item in iterable}
squares = {x: x**2 for x in range(6)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With filtering
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Transform existing dict
prices = {"apple": 0.50, "banana": 0.25, "orange": 0.75}
doubled = {fruit: price * 2 for fruit, price in prices.items()}
print(doubled)  # {'apple': 1.0, 'banana': 0.5, 'orange': 1.5}

# Swap keys and values
flipped = {v: k for k, v in prices.items()}
print(flipped)  # {0.5: 'apple', 0.25: 'banana', 0.75: 'orange'}
```

### Practical Dict Comprehension Patterns

``` python {title="Common Patterns" linenums="1"}
# Create lookup from list
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# Filter a dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
passing = {name: score for name, score in scores.items() if score >= 80}
print(passing)  # {'Alice': 85, 'Bob': 92, 'Diana': 95}

# Convert keys to uppercase
upper_scores = {name.upper(): score for name, score in scores.items()}
print(upper_scores)  # {'ALICE': 85, 'BOB': 92, 'CHARLIE': 78, 'DIANA': 95}
```

## defaultdict: Dictionaries with Default Values

The `defaultdict` from the `collections` module automatically creates missing keys with
a default value. No more `KeyError`! 🎉

``` python {title="defaultdict Basics" linenums="1"}
from collections import defaultdict

# Regular dict raises KeyError
regular = {}
# regular["missing"] += 1  # KeyError!

# defaultdict provides a default
counter = defaultdict(int)  # int() returns 0
counter["apples"] += 1
counter["apples"] += 1
counter["bananas"] += 1
print(dict(counter))  # {'apples': 2, 'bananas': 1}

# defaultdict with list
groups = defaultdict(list)
groups["fruit"].append("apple")
groups["fruit"].append("banana")
groups["veggie"].append("carrot")
print(dict(groups))  # {'fruit': ['apple', 'banana'], 'veggie': ['carrot']}
```

### Common defaultdict Factories

``` python {title="defaultdict Factories" linenums="1"}
from collections import defaultdict

# int — for counting
word_counts = defaultdict(int)

# list — for grouping
grouped_items = defaultdict(list)

# set — for unique grouping
unique_tags = defaultdict(set)

# Custom default
default_score = defaultdict(lambda: 100)
print(default_score["new_player"])  # 100
```

## Counter: Counting Made Easy

`Counter` is a specialized dict for counting hashable objects. Perfect for answering
questions like "How many times did someone order pepperoni?" (Spoiler: a lot. But at
least it wasn't on cheap pizza.)

``` python {title="Counter Basics" linenums="1"}
from collections import Counter

# Count from an iterable
word = "mississippi"
letter_counts = Counter(word)
print(letter_counts)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Count from a list
votes = ["alice", "bob", "alice", "charlie", "alice", "bob"]
results = Counter(votes)
print(results)
# Counter({'alice': 3, 'bob': 2, 'charlie': 1})

# Most common items
print(results.most_common(2))  # [('alice', 3), ('bob', 2)]

# Access counts like a dict
print(results["alice"])  # 3
print(results["nobody"])  # 0 (not KeyError!)
```

### Counter Operations

``` python {title="Counter Operations" linenums="1"}
from collections import Counter

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

# Add counts
print(c1 + c2)  # Counter({'a': 4, 'b': 3})

# Subtract counts
print(c1 - c2)  # Counter({'a': 2})

# Intersection (minimum counts)
print(c1 & c2)  # Counter({'a': 1, 'b': 1})

# Union (maximum counts)
print(c1 | c2)  # Counter({'a': 3, 'b': 2})

# Total count
print(c1.total())  # 4 (Python 3.10+)
```

## Iterating Over Dictionaries

Three ways to iterate, depending on what you need:

``` python {title="Dictionary Iteration" linenums="1"}
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Iterate over keys (default)
for key in person:
    print(key)

# Explicit keys
for key in person.keys():
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs (most common!)
for key, value in person.items():
    print(f"{key}: {value}")
```

!!! tip "items() is Your Friend"

    When you need both key and value, always use `items()`. It's cleaner than
    `for key in dict: value = dict[key]`.

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Creating** | `{"key": value}` or `dict()` |
| **Accessing** | `dict[key]` or `dict.get(key, default)` |
| **Adding/Updating** | `dict[key] = value` |
| **Deleting** | `del dict[key]` or `dict.pop(key)` |
| **Merging** | `dict.update(other)` or `dict1 \| dict2` (3.9+) |
| **setdefault()** | Get or set a default in one step |
| **Comprehensions** | `{k: v for k, v in items}` |
| **defaultdict** | Auto-creates missing keys with a factory |
| **Counter** | Specialized dict for counting |
| **Iteration** | `keys()`, `values()`, `items()` |
| **Order** | Insertion order preserved (Python 3.7+) |
