# Booleans

Validate user passwords. Check if a file exists. Determine whether to show admin features. Test if a number is within range. Filter search results. Control loop execution. Every one of these requires answering yes/no questions in code.

Booleans are Python's data type for truth values—`True` or `False`. They're the foundation of every decision your program makes, powering [`if` statements](../control_structures/if_statements.md), [`while` loops](../control_structures/while_loops.md), data filtering, and conditional logic throughout your code.

## What is a Boolean?

A boolean (`bool` type) represents one of two values: `True` or `False`:

```python title="Creating Booleans" linenums="1"
is_authenticated = True  # (1)!
has_permission = False
is_valid = True
```

1. Booleans must be capitalized—`True` and `False`, not `true`/`false`. Python will raise `NameError` for lowercase versions.

Most booleans aren't assigned directly—they're the result of comparisons, function returns, or logical operations:

```python title="Booleans from Comparisons" linenums="1"
age = 25
is_adult = age >= 18      # (1)!
print(is_adult)           # True

user_count = 0
has_users = user_count > 0  # (2)!
print(has_users)          # False
```

1. Comparison operators (`>=`, `==`, `!=`, etc.) return boolean values
2. Evaluates to `False` because 0 is not greater than 0

## Why Booleans Matter

Booleans enable decision-making in code:

- **Authentication**: Is the user logged in? Do they have permission?
- **Validation**: Is the email valid? Is the form complete? Is the input within range?
- **Control flow**: Should the loop continue? Should this branch execute?
- **Filtering**: Does this item match criteria? Should it appear in results?
- **State management**: Is the connection active? Is data loaded? Is processing complete?

Without booleans, programs couldn't make decisions. Every [`if` statement](../control_structures/if_statements.md), every [`loop`](../control_structures/for_loops.md) condition, every filter—all built on [boolean logic](https://cs.bradpenney.io/fundamentals/computational_thinking/#logical-thinking).

## Comparison Operators

Check if a score passes a threshold. Verify a password matches. Test if an age qualifies for a discount. Comparisons return boolean values that drive program logic:

```python title="Comparison Operators" linenums="1"
x = 10
y = 5

print(x == y)   # (1)!
print(x != y)   # (2)!
print(x > y)    # (3)!
print(x < y)
print(x >= y)
print(x <= y)
```

1. `==` tests equality—returns `False` (10 does not equal 5)
2. `!=` tests inequality—returns `True` (10 is not equal to 5)
3. `>`, `<`, `>=`, `<=` compare magnitude—work with [numbers](ints.md), [strings](strings.md), and other comparable types

These operators work with numbers, [strings](strings.md) (alphabetical order), and other comparable types:

```python title="Comparing Strings" linenums="1"
print("apple" < "banana")   # (1)!
print("apple" < "Apple")    # (2)!
print("10" < "9")           # (3)!
```

1. Returns `True`—'a' comes before 'b' alphabetically
2. Returns `False`—lowercase letters come after uppercase in ASCII/Unicode
3. Returns `True`—string comparison is character-by-character: '1' < '9' in ASCII

!!! warning "String vs Number Comparison"

    Comparing strings that look like numbers can be surprising. `"10" < "9"` is `True` because
    string comparison is character-by-character, and `'1'` comes before `'9'`. If you need
    numeric comparison, convert to [`int`](ints.md) or [`float`](floats.md) first.

### Chained Comparisons

Validate that a value falls within a range. Check if a date is between two bounds. Python lets you chain comparisons naturally:

```python title="Chained Comparisons" linenums="1"
age = 25

# Instead of: age >= 18 and age <= 65
print(18 <= age <= 65)  # (1)!

temperature = 72
print(60 < temperature < 80)  # (2)!
```

1. Returns `True`—reads like mathematical notation: "is age between 18 and 65?"
2. Returns `True`—multiple comparisons in one expression

## Logical Operators

Require both username AND password. Grant access if admin OR moderator. Deny entry if NOT authenticated. Combining conditions is essential for complex logic—Python provides `and`, `or`, and `not`:

### The `and` Operator

Both conditions must be `True` for the result to be `True`:

```python title="The and Operator" linenums="1"
age = 25
has_license = True

can_drive = age >= 16 and has_license  # (1)!
print(can_drive)  # True

can_rent_car = age >= 25 and has_license
print(can_rent_car)  # True
```

1. Both conditions must be true—age must be at least 16 AND license must exist

| A | B | A and B |
|:--|:--|:--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### The `or` Operator

At least one condition must be `True` for the result to be `True`:

```python title="The or Operator" linenums="1"
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday  # (1)!
print(can_sleep_in)  # True
```

1. Only one condition needs to be true—either weekend OR holiday allows sleeping in

| A | B | A or B |
|:--|:--|:-------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### The `not` Operator

Flips `True` to `False` and vice versa:

```python title="The not Operator" linenums="1"
is_raining = False

if not is_raining:  # (1)!
    print("Let's go for a walk!")

# Double negation
print(not not True)  # (2)!
```

1. `not` inverts the boolean—`not False` becomes `True`
2. Returns `True`—two `not` operators cancel out

### Combining Operators

Check complex eligibility. Validate multiple requirements. Build sophisticated filters—combine operators for precise logic:

```python title="Complex Conditions" linenums="1"
age = 25
is_student = True
has_coupon = False

# Gets discount if: student, OR has coupon, OR is senior (65+)
gets_discount = is_student or has_coupon or age >= 65  # (1)!
print(gets_discount)  # True

# Can enter if: adult AND (member OR has ticket)
is_adult = age >= 18
is_member = False
has_ticket = True

can_enter = is_adult and (is_member or has_ticket)  # (2)!
print(can_enter)  # True
```

1. Multiple `or` conditions—any one being true makes the whole expression true
2. Parentheses group conditions—must be adult AND (member OR ticket holder)

!!! tip "Use Parentheses for Clarity"

    While Python has operator precedence rules (`not` before `and` before `or`), explicit
    parentheses make your intent clear and prevent bugs.

## Truthiness: What Python Considers True or False

Check if a list has items without `len()`. Validate that a string isn't empty without comparison. Test for `None` in conditionals. Python's "truthiness" lets every value act as a boolean in context.

### Falsy Values

These values are considered `False` when used in a boolean context:

```python title="Falsy Values" linenums="1"
# All of these are "falsy"
print(bool(False))     # (1)!
print(bool(None))      # (2)!
print(bool(0))         # (3)!
print(bool(0.0))
print(bool(""))        # (4)!
print(bool([]))        # (5)!
print(bool({}))
print(bool(set()))
print(bool(()))
```

1. `False` is obviously falsy
2. `None` (absence of value) is falsy—see [None type](none.md)
3. Zero in any numeric form (`0`, `0.0`) is falsy
4. Empty [string](strings.md) is falsy
5. Empty collections ([lists](../../data_structures/lists.md), [dicts](../../data_structures/dictionaries.md), [sets](../../data_structures/sets.md), [tuples](../../data_structures/tuples.md)) are falsy

### Truthy Values

Everything else is considered `True`:

```python title="Truthy Values" linenums="1"
# All of these are "truthy"
print(bool(True))      # True — obviously
print(bool(1))         # (1)!
print(bool(-1))        # (2)!
print(bool(3.14))
print(bool("hello"))   # (3)!
print(bool(" "))       # (4)!
print(bool([1, 2]))    # (5)!
print(bool({"a": 1}))
```

1. Any non-zero number is truthy
2. Negative numbers are truthy too!
3. Non-empty strings are truthy
4. String with just a space is truthy (not empty!)
5. Non-empty collections are truthy

### Why Truthiness Matters

Truthiness allows for elegant, Pythonic code:

```python title="Pythonic Truthiness" linenums="1"
# Instead of:
if len(my_list) > 0:  # (1)!
    print("List has items")

# Write:
if my_list:  # (2)!
    print("List has items")

# Instead of:
if name != "":
    print(f"Hello, {name}")

# Write:
if name:  # (3)!
    print(f"Hello, {name}")

# Checking for None
result = some_function()
if result is not None:  # (4)!
    process(result)

# Or simply (if None and other falsy values should be skipped):
if result:  # (5)!
    process(result)
```

1. Verbose—explicitly checking length
2. Pythonic—empty list is falsy, non-empty is truthy
3. Pythonic—empty string is falsy
4. Explicit None check—use when distinguishing None from other falsy values (0, "", etc.)
5. Truthiness check—simpler but treats 0, "", [], etc. the same as None

!!! warning "Truthiness vs. Explicit Comparison"

    Be careful! `if x:` and `if x == True:` are different:

    ```python
    x = 1
    print(x == True)   # True — because bool(1) equals True
    print(x is True)   # False — 1 is not the same object as True

    x = 2
    print(x == True)   # False — 2 doesn't equal True
    print(bool(x))     # True — but 2 is still truthy!
    ```

    When checking truthiness, use `if x:`. When checking for the actual boolean value,
    use `if x is True:`.

## Short-Circuit Evaluation

Skip expensive database queries. Avoid accessing attributes on None. Prevent unnecessary API calls. Python's "short-circuit evaluation" stops evaluating as soon as the result is known—boosting performance and safety:

### How `and` Short-Circuits

With `and`, if the first value is falsy, Python doesn't bother checking the second:

```python title="and Short-Circuiting" linenums="1"
def expensive_check():
    print("Running expensive check...")  # (1)!
    return True

# This prints nothing — expensive_check() never runs
result = False and expensive_check()  # (2)!
print(result)  # False
```

1. This function would be expensive to run (database query, API call, etc.)
2. Since `False and anything` is always `False`, Python skips the function call entirely

### How `or` Short-Circuits

With `or`, if the first value is truthy, Python doesn't bother checking the second:

```python title="or Short-Circuiting" linenums="1"
def expensive_check():
    print("Running expensive check...")
    return False

# This prints nothing — expensive_check() never runs
result = True or expensive_check()  # (1)!
print(result)  # True
```

1. Since `True or anything` is always `True`, Python skips the function call

### Practical Uses

Short-circuiting enables some elegant patterns:

```python title="Short-Circuit Patterns" linenums="1"
# Safe attribute access
user = None
# This would crash: user.name
# But this is safe:
name = user and user.name  # (1)!

# Default values
username = input_name or "Anonymous"  # (2)!

# Guard clauses in functions
def process_items(items):  # (3)!
    if not items:  # (4)!
        return []
    # ... rest of function
```

1. Returns `None` without crashing—if `user` is falsy, Python stops evaluating and returns `user` (None)
2. Use "Anonymous" if `input_name` is empty/None—the `or` pattern provides a default value
3. See [functions](../control_structures/functions.md) for more on defining and using functions
4. Short-circuits the rest of the function if items is empty/None—guard clauses prevent errors

!!! tip "The `or` Default Pattern"

    `value or default` is a common Python idiom for providing default values:

    ```python
    name = user_input or "Guest"
    port = config.get("port") or 8080
    ```

    But be careful — this replaces *any* falsy value, including `0` or `""` which might be
    intentional. For more control, use `value if value is not None else default`.

## The `bool()` Function

You can explicitly convert any value to a boolean using `bool()`:

```python title="Using bool()" linenums="1"
print(bool(42))        # (1)!
print(bool(""))        # (2)!
print(bool([1, 2, 3])) # (3)!

# Useful for debugging truthiness
mystery_value = some_function()
print(f"Value: {mystery_value}, Truthy: {bool(mystery_value)}")  # (4)!
```

1. Returns `True`—any non-zero number is truthy
2. Returns `False`—empty string is falsy
3. Returns `True`—non-empty list is truthy
4. Helpful debugging pattern to see both the value and its boolean interpretation

## Practice Problems

??? question "Practice Problem 1: Comparison Operators"

    What does `5 < 10 < 15` evaluate to?

    ??? tip "Answer"

        It returns `True`. This is a chained comparison that checks if `5 < 10` AND `10 < 15`. Both conditions are true, so the entire expression is `True`. This is equivalent to `5 < 10 and 10 < 15`, but more readable.

??? question "Practice Problem 2: Truthiness"

    Which of these values are truthy in Python: `0`, `[]`, `" "` (space), `False`, `1`, `None`?

    ??? tip "Answer"

        Only `" "` (string with a space) and `1` are truthy.

        - `0` is falsy (zero is always falsy)
        - `[]` is falsy (empty list)
        - `" "` is **truthy** (non-empty string—even just whitespace counts!)
        - `False` is falsy (obviously)
        - `1` is **truthy** (non-zero number)
        - `None` is falsy (absence of value)

??? question "Practice Problem 3: Short-Circuit Evaluation"

    What will this code print?

    ```python
    result = [] or [1, 2, 3]
    print(result)
    ```

    ??? tip "Answer"

        It prints `[1, 2, 3]`.

        The `or` operator returns the first truthy value. Since `[]` (empty list) is falsy, Python evaluates the second operand `[1, 2, 3]`, which is truthy, and returns it. This is the "default value" pattern: `value or default`.

??? question "Practice Problem 4: Logical Operators"

    What's the difference between `==` and `is` when comparing to `True`?

    ??? tip "Answer"

        - `==` checks for **equality** (value comparison)
        - `is` checks for **identity** (same object in memory)

        ```python
        x = 1
        print(x == True)   # True — 1 equals True in value
        print(x is True)   # False — 1 is not the same object as True

        y = True
        print(y == True)   # True — obviously equal
        print(y is True)   # True — same object
        ```

        For boolean checks, use `if x:` (truthiness) rather than `if x == True:` or `if x is True:` unless you specifically need to distinguish `True` from other truthy values.

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Values** | Only `True` and `False` (capitalized!) |
| **Comparison operators** | `==`, `!=`, `<`, `>`, `<=`, `>=` return booleans |
| **Logical operators** | `and`, `or`, `not` — can be combined |
| **Falsy values** | `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `()` |
| **Truthy values** | Everything else |
| **Short-circuit** | `and`/`or` stop early when result is known |
| **Pythonic style** | Use `if items:` not `if len(items) > 0:` |

## Further Reading

- [**Python Boolean Operations Documentation**](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) - Official reference for `and`, `or`, `not`
- [**Truth Value Testing**](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) - Complete list of falsy values and truthiness rules
- [**PEP 8 – Style Guide for Python Code**](https://peps.python.org/pep-0008/#programming-recommendations) - Boolean comparison best practices
- [**Computational Thinking**](https://cs.bradpenney.io/fundamentals/computational_thinking/) - Understanding logical reasoning in programming
- [**Python Operators**](https://docs.python.org/3/library/operator.html) - Standard operators including comparison and boolean operators

## Video Summary

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/MahbVDnYSpU" title="Python Booleans" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

---

Booleans are deceptively simple—just `True` and `False`—yet they're the foundation of every decision your program makes. Master comparison operators, logical combinations, and truthiness, and you control the flow of execution. Understand short-circuit evaluation, and you write safer, more efficient code.

Every [`if` statement](../control_structures/if_statements.md), every [loop](../control_structures/for_loops.md) condition, every filter operation relies on boolean logic. The elegance of Python's truthiness (checking `if items:` instead of `if len(items) > 0:`) reflects the [language's philosophy](https://cs.bradpenney.io/fundamentals/what_is_computer_science/#programming-paradigms): explicit is better than implicit, but simple is better than complex. Booleans embody both principles—simple in concept, powerful in practice.
