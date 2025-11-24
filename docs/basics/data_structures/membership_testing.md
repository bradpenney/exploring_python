# Membership Testing

When working with data structures, one of the most common questions is
*"Does this value exist in this data structure?"* 🔍 Python comes to the rescue here with two
operators: `in` and `not in`.

## Testing Membership in Sequences

Recall that the sequence types in Python are [`list`](lists.md) and [`tuples`](tuples.md). While
they can contain any data type, the order of the elements is guaranteed.

Testing membership using the `in` and `not in` operators combined with an
[`if` statement](../control_structures/if_statements.md) returns a *truthy* value
([`boolean`](../data_types/booleans.md)) to indicate membership:

``` python {title="Testing Membership in a List" linenums="1"}
fav_books = ['mastery', 'the signal and the noise', 'the organized mind']

if 'mastery' in fav_books:
    print("One of your favourites!")
else:
    print("Maybe something new to consider?")
```

Returns:

``` text
One of your favourites!
```

Using `not in` works the opposite:

``` python {title="Negative Testing Membership in a List" linenums="1"}
fav_books = ['mastery', 'the signal and the noise', 'the organized mind']

if 'discipline is destiny' not in fav_books:
    print("Have your read this one? Maybe you should!")
else:
    print("Ye ole` favourites once again!")
```

Would result in:

``` text
Have your read this one? Maybe you should!
```

## Testing Membership in Dictionaries

Dictionaries (the [`dict` data structure](../data_structures/dictionaries.md)) present a little
bit of a special case in testing membership, the caveat being you must remember that by default,
the test runs against the *key* of the dictionary, not the entire *key/value* pair, nor against
the *value* itself.

``` python {title="Testing Membership in Dictionary Keys" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

if 'year' in dream_car:
    print("Good to know the year of your dream car!")
else:
    print("What year is your dream car?")
```

Would output:

``` text
Good to know the year of your dream car!
```

If you'd like to test to see if a specific value is in a dictionary, remmember to use the
`dict.values()` method:

``` python {title="Negative Testing Membership in Dictionary Values" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

if 'Pinto' not in dream_car.values():
    print("Your dream car isn't a Pinto???!??")
else:
    print("Nothing quite as sweet as a lovely Pinto!")
```

Which would return:

``` text
Nothing quite as sweet as a lovely Pinto!
```

## Testing Membership in Strings

Strings support `in` for substring checking:

``` python {title="Substring Testing" linenums="1"}
message = "Hello, World!"

print("World" in message)     # True
print("world" in message)     # False — case-sensitive!
print("Hello" in message)     # True
print("xyz" not in message)   # True

# Case-insensitive check
print("world" in message.lower())  # True
```

This is more readable than using `find()` or `index()`:

``` python {title="in vs find()" linenums="1"}
text = "The quick brown fox"

# Preferred — clean and readable
if "fox" in text:
    print("Found it!")

# Works, but less Pythonic
if text.find("fox") != -1:
    print("Found it!")
```

## Performance: Choosing the Right Data Structure

Not all membership tests are created equal. The choice of data structure dramatically
affects performance — like the difference between a hand-crafted espresso and that sad
office drip coffee. Both contain caffeine, but one sparks joy. ⚡

| Data Structure | `in` Performance | Notes |
|:---------------|:-----------------|:------|
| `list` | O(n) — slow | Checks each element sequentially |
| `tuple` | O(n) — slow | Same as list |
| `set` | O(1) — fast! | Hash-based lookup |
| `frozenset` | O(1) — fast! | Same as set |
| `dict` keys | O(1) — fast! | Hash-based lookup |
| `str` | O(n) — depends | Substring search |

### The Practical Impact

``` python {title="Performance Comparison" linenums="1"}
import time

# Create test data
large_list = list(range(1_000_000))
large_set = set(range(1_000_000))

# What we're looking for (worst case — at the end or missing)
target = 999_999

# List search — slow!
start = time.time()
_ = target in large_list
print(f"List: {time.time() - start:.6f} seconds")

# Set search — instant!
start = time.time()
_ = target in large_set
print(f"Set: {time.time() - start:.6f} seconds")

# Typical output:
# List: 0.015000 seconds
# Set: 0.000001 seconds
```

!!! tip "When to Convert to Set"

    If you're checking membership multiple times against the same collection,
    convert to a set first:

    ```python
    valid_codes = ["A1", "B2", "C3", "D4", ...]  # Original data
    valid_set = set(valid_codes)  # One-time conversion

    # Now all lookups are O(1)
    for code in user_inputs:
        if code in valid_set:
            process(code)
    ```

## The `any()` and `all()` Functions

These built-in functions supercharge membership testing when you need to check
multiple conditions.

### `any()` — At Least One True

Returns `True` if *any* element is truthy (or if any condition is met):

``` python {title="any() Examples" linenums="1"}
# Basic usage
print(any([False, False, True]))   # True
print(any([False, False, False]))  # False
print(any([]))                     # False (empty = no True values)

# With generator expression — more common!
numbers = [1, 3, 5, 7, 8, 9]
has_even = any(n % 2 == 0 for n in numbers)
print(has_even)  # True (8 is even)

# Check if any item exists in a collection
search_terms = ["error", "warning", "critical"]
log_message = "Warning: disk space low"

if any(term in log_message.lower() for term in search_terms):
    print("Alert triggered!")
```

### `all()` — Every One True

Returns `True` only if *all* elements are truthy:

``` python {title="all() Examples" linenums="1"}
# Basic usage
print(all([True, True, True]))   # True
print(all([True, False, True]))  # False
print(all([]))                   # True (vacuous truth!)

# Check if all values pass a condition
ages = [25, 30, 18, 42]
all_adults = all(age >= 18 for age in ages)
print(all_adults)  # True

# Validate all required fields
user = {"name": "Alice", "email": "alice@example.com", "age": 30}
required = ["name", "email"]
is_valid = all(field in user for field in required)
print(is_valid)  # True
```

### Short-Circuit Evaluation

Both `any()` and `all()` short-circuit — they stop as soon as they know the answer:

``` python {title="Short-Circuit Behavior" linenums="1"}
def check(n):
    print(f"Checking {n}")
    return n > 5

# any() stops at first True
print(any(check(n) for n in [1, 2, 6, 3, 4]))
# Checking 1
# Checking 2
# Checking 6  ← stops here!
# True

# all() stops at first False
print(all(check(n) for n in [6, 7, 3, 8, 9]))
# Checking 6
# Checking 7
# Checking 3  ← stops here!
# False
```

### Common Patterns

``` python {title="Practical any()/all() Patterns" linenums="1"}
# Check if file has any of these extensions
filename = "report.pdf"
valid_extensions = [".pdf", ".doc", ".txt"]
is_valid = any(filename.endswith(ext) for ext in valid_extensions)

# Check if all passwords meet requirements
passwords = ["Abc123!", "SecurePass1", "MyP@ss99"]
all_valid = all(
    len(p) >= 8 and any(c.isdigit() for c in p)
    for p in passwords
)

# Check if any item in cart is out of stock
cart = [{"item": "widget", "stock": 5}, {"item": "gadget", "stock": 0}]
has_out_of_stock = any(item["stock"] == 0 for item in cart)
```

## Combining Membership Tests

``` python {title="Complex Membership Logic" linenums="1"}
# Check multiple memberships
required_skills = {"python", "sql", "git"}
nice_to_have = {"docker", "kubernetes", "aws"}

candidate_skills = {"python", "sql", "git", "docker", "react"}

# Has all required?
is_qualified = required_skills.issubset(candidate_skills)
print(is_qualified)  # True

# Has any nice-to-have?
has_bonus = bool(nice_to_have & candidate_skills)
print(has_bonus)  # True (has docker)

# Count matches
bonus_count = len(nice_to_have & candidate_skills)
print(f"Bonus skills: {bonus_count}")  # Bonus skills: 1
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **`in` operator** | Works on lists, tuples, sets, dicts, strings |
| **`not in`** | Negation of membership test |
| **Dict membership** | Tests keys by default; use `.values()` for values |
| **String `in`** | Tests for substring, not character |
| **Performance** | Sets and dicts are O(1); lists/tuples are O(n) |
| **`any()`** | True if at least one element is truthy |
| **`all()`** | True only if every element is truthy |
| **Generator expressions** | Use with any()/all() for efficiency |
| **Short-circuit** | any()/all() stop early when answer is known |