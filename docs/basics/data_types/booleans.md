# Booleans

A `boolean` is akin to a digital switch, representing a binary state that can be "on" or "off". 💡
Booleans, a fundamental data type in Python, provide a simple yet powerful way to express
conditions and make decisions in your code. They are the cornerstone of control statements
like [`if/else`](../control_structures/if_statements.md) statements and
[`while` loops](../control_structures/while_loops.md), allowing you to create dynamic,
responsive programs.

Booleans can take on one of two values: `True` or `False`. These values act as signals to guide
your program's logic and flow. Whether you're validating user input, iterating through data,
or responding to external conditions, booleans are your code's decision-makers.

!!! note "Case Matters"

    In Python, `True` and `False` must be capitalized. Writing `true` or `FALSE` will give you
    a `NameError`. Python is particular about this. 🎩

Let's delve into the world of booleans in Python with some practical examples:

``` python {title="Declaring Booleans in Python" linenums="1"}
python_is_awesome = True
learning_python_is_hard = False
```

In this snippet, we’ve created two `boolean` variables, `python_is_awesome` and
`learning_python_is_hard`, which can be thought of as assertions about the state of
affairs in our code.

Booleans come to life when they are used in conjunction with control statements.
For instance:

``` python {title="Booleans Control Decision-Making" linenums="1"}
if python_is_awesome:
    print("Python is Awesome!")
```

Returns:

``` text
Python is Awesome!
```

Here, the `if` statement evaluates whether `python_is_awesome` is `True`. If it is, the
associated code block executes, and you’ll see the message "Python is Awesome!" printed on the
screen. This demonstrates how booleans influence the flow of your program based on conditions.

Booleans are also indispensable when it comes to loops. Consider the following:

``` python {title="Booleans Control Loops" linenums="1"}
kevin_is_a_secret_genius = True

while kevin_is_a_secret_genius:
    print("There is no way Kevin is a secret genius")
    kevin_is_a_secret_genius = False
```

Which would return:
``` text
There is no way Kevin is a secret genius
```

In this example, the `while` loop continues to run as long as `kevin_is_a_secret_genius`
is `True`. The moment it tries to execute while it is `False`, the loop terminates. This
illustrates how booleans can control the repetition of tasks in your code, allowing you
to automate processes efficiently.

## Comparison Operators

Most booleans aren't declared directly — they're the *result* of comparisons. Python provides
a full set of comparison operators that evaluate to `True` or `False`:

``` python {title="Comparison Operators" linenums="1"}
x = 10
y = 5

print(x == y)   # False — equal to
print(x != y)   # True  — not equal to
print(x > y)    # True  — greater than
print(x < y)    # False — less than
print(x >= y)   # True  — greater than or equal to
print(x <= y)   # False — less than or equal to
```

These operators work with numbers, strings (alphabetical order), and other comparable types:

``` python {title="Comparing Strings" linenums="1"}
print("apple" < "banana")   # True — 'a' comes before 'b'
print("apple" < "Apple")    # False — lowercase letters come after uppercase in ASCII
print("10" < "9")           # True — string comparison, not numeric! '1' < '9'
```

!!! warning "String vs Number Comparison"

    Comparing strings that look like numbers can be surprising. `"10" < "9"` is `True` because
    string comparison is character-by-character, and `'1'` comes before `'9'`. If you need
    numeric comparison, convert to `int` or `float` first.

### Chained Comparisons

Python lets you chain comparisons in a way that reads naturally:

``` python {title="Chained Comparisons" linenums="1"}
age = 25

# Instead of: age >= 18 and age <= 65
print(18 <= age <= 65)  # True — reads like math!

temperature = 72
print(60 < temperature < 80)  # True — comfortable range
```

This is one of Python's small pleasures. 🐍

## Logical Operators

To combine multiple conditions, Python provides three logical operators: `and`, `or`, and `not`.

### The `and` Operator

Both conditions must be `True` for the result to be `True`:

``` python {title="The and Operator" linenums="1"}
age = 25
has_license = True

can_drive = age >= 16 and has_license
print(can_drive)  # True — both conditions are met

can_rent_car = age >= 25 and has_license
print(can_rent_car)  # True
```

| A | B | A and B |
|:--|:--|:--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### The `or` Operator

At least one condition must be `True` for the result to be `True`:

``` python {title="The or Operator" linenums="1"}
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True — at least one is True
```

| A | B | A or B |
|:--|:--|:-------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### The `not` Operator

Flips `True` to `False` and vice versa:

``` python {title="The not Operator" linenums="1"}
is_raining = False

if not is_raining:
    print("Let's go for a walk!")  # This prints

# Double negation
print(not not True)  # True — two negatives make a positive
```

### Combining Operators

You can combine these operators to build complex conditions:

``` python {title="Complex Conditions" linenums="1"}
age = 25
is_student = True
has_coupon = False

# Gets discount if: student, OR has coupon, OR is senior (65+)
gets_discount = is_student or has_coupon or age >= 65
print(gets_discount)  # True

# Can enter if: adult AND (member OR has ticket)
is_adult = age >= 18
is_member = False
has_ticket = True

can_enter = is_adult and (is_member or has_ticket)
print(can_enter)  # True
```

!!! tip "Use Parentheses for Clarity"

    While Python has operator precedence rules (`not` before `and` before `or`), explicit
    parentheses make your intent clear and prevent bugs. Future you will thank present you. 🙏

## Truthiness: What Python Considers True or False

Here's where it gets interesting. In Python, *every* value has a boolean interpretation —
not just `True` and `False`. This is called "truthiness."

### Falsy Values

These values are considered `False` when used in a boolean context:

``` python {title="Falsy Values" linenums="1"}
# All of these are "falsy"
print(bool(False))     # False — obviously
print(bool(None))      # False — the absence of a value
print(bool(0))         # False — zero
print(bool(0.0))       # False — zero as float
print(bool(""))        # False — empty string
print(bool([]))        # False — empty list
print(bool({}))        # False — empty dictionary
print(bool(set()))     # False — empty set
print(bool(()))        # False — empty tuple
```

### Truthy Values

Everything else is considered `True`:

``` python {title="Truthy Values" linenums="1"}
# All of these are "truthy"
print(bool(True))      # True — obviously
print(bool(1))         # True — non-zero number
print(bool(-1))        # True — negative numbers too!
print(bool(3.14))      # True — non-zero float
print(bool("hello"))   # True — non-empty string
print(bool(" "))       # True — string with just a space (not empty!)
print(bool([1, 2]))    # True — non-empty list
print(bool({"a": 1}))  # True — non-empty dictionary
```

### Why Truthiness Matters

Truthiness allows for elegant, Pythonic code:

``` python {title="Pythonic Truthiness" linenums="1"}
# Instead of:
if len(my_list) > 0:
    print("List has items")

# Write:
if my_list:
    print("List has items")

# Instead of:
if name != "":
    print(f"Hello, {name}")

# Write:
if name:
    print(f"Hello, {name}")

# Checking for None
result = some_function()
if result is not None:
    process(result)

# Or simply (if None and other falsy values should be skipped):
if result:
    process(result)
```

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

Python is lazy in the best way — it stops evaluating a boolean expression as soon as it
knows the answer. This is called "short-circuit evaluation."

### How `and` Short-Circuits

With `and`, if the first value is falsy, Python doesn't bother checking the second:

``` python {title="and Short-Circuiting" linenums="1"}
def expensive_check():
    print("Running expensive check...")
    return True

# This prints nothing — expensive_check() never runs
result = False and expensive_check()
print(result)  # False
```

### How `or` Short-Circuits

With `or`, if the first value is truthy, Python doesn't bother checking the second:

``` python {title="or Short-Circuiting" linenums="1"}
def expensive_check():
    print("Running expensive check...")
    return False

# This prints nothing — expensive_check() never runs
result = True or expensive_check()
print(result)  # True
```

### Practical Uses

Short-circuiting enables some elegant patterns:

``` python {title="Short-Circuit Patterns" linenums="1"}
# Safe attribute access
user = None
# This would crash: user.name
# But this is safe:
name = user and user.name  # Returns None, doesn't crash

# Default values
username = input_name or "Anonymous"  # Use "Anonymous" if input is empty

# Guard clauses
def process_items(items):
    if not items:  # Short-circuits the rest if items is empty/None
        return []
    # ... rest of function
```

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

``` python {title="Using bool()" linenums="1"}
print(bool(42))        # True
print(bool(""))        # False
print(bool([1, 2, 3])) # True

# Useful for debugging truthiness
mystery_value = some_function()
print(f"Value: {mystery_value}, Truthy: {bool(mystery_value)}")
```

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

## Video Summary

<div class="video-wrapper">
  <iframe src="https://www.youtube.com/embed/MahbVDnYSpU" title="Python Booleans" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>
