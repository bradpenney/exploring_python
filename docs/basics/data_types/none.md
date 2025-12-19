# None

Every programming language needs a way to represent "nothing." In Python, that's `None`. 🕳️

`None` is Python's null value — it represents the *absence* of a value, rather than a value
of zero, empty, or false. It's a singleton, meaning there's only ever one `None` object in
memory, and it's used everywhere: function returns, optional parameters, placeholder values,
and more.

``` python {title="The None Type" linenums="1"}
nothing = None
print(nothing)        # None
print(type(nothing))  # <class 'NoneType'>
```

!!! note "None is Not..."

    `None` is not the same as:

    - `0` (that's an integer with a value)
    - `""` (that's an empty string — still a string)
    - `[]` (that's an empty list — still a list)
    - `False` (that's a boolean with a value)

    `None` means "no value at all."

## When You'll Encounter None

### Functions Without a Return Value

If a function doesn't explicitly return something, it returns `None`:

``` python {title="Implicit None Return" linenums="1"}
def greet(name):
    print(f"Hello, {name}!")
    # No return statement

result = greet("Alice")  # Prints "Hello, Alice!"
print(result)            # None
print(result is None)    # True
```

This catches many beginners off guard. If you forget to return a value, your function
silently returns `None`. 🤫

``` python {title="The Forgotten Return" linenums="1"}
def add(a, b):
    total = a + b
    # Oops! Forgot to return total

result = add(2, 3)
print(result)  # None — not 5!
```

### Optional Parameters

`None` is commonly used as a default for optional parameters:

``` python {title="None as Default Parameter" linenums="1"}
def connect(host, port=None):
    if port is None:
        port = 8080  # Use default
    print(f"Connecting to {host}:{port}")

connect("localhost")        # Connecting to localhost:8080
connect("localhost", 3000)  # Connecting to localhost:3000
```

!!! tip "Why Not Just Use the Default Directly?"

    You might wonder why not write `port=8080` directly. Using `None` is useful when:

    - The default depends on other parameters or runtime conditions
    - You need to distinguish between "not provided" and "explicitly set to the default"
    - The default is mutable (like a list) — never use mutable defaults!

    ```python
    # DANGER: Mutable default argument
    def add_item(item, items=[]):  # DON'T DO THIS
        items.append(item)
        return items

    # SAFE: Use None instead
    def add_item(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items
    ```

### Dictionary and Attribute Access

Many methods return `None` when a key or attribute doesn't exist:

``` python {title="None from Missing Keys" linenums="1"}
user = {"name": "Alice", "email": "alice@example.com"}

# .get() returns None for missing keys (instead of raising KeyError)
phone = user.get("phone")
print(phone)  # None

# You can provide a default
phone = user.get("phone", "Not provided")
print(phone)  # "Not provided"
```

### Representing "Not Yet Set"

`None` is useful as a placeholder for values that will be set later:

``` python {title="Placeholder Values" linenums="1"}
class User:
    def __init__(self, username):
        self.username = username
        self.email = None      # Will be set later
        self.verified = None   # Unknown until checked

user = User("bob")
print(user.email)  # None

# Later...
user.email = "bob@example.com"
```

## Checking for None: `is` vs `==`

This is important: **always use `is None`, not `== None`**.

``` python {title="is None vs == None" linenums="1"}
value = None

# CORRECT — use 'is'
if value is None:
    print("Value is None")

# ALSO CORRECT — use 'is not'
if value is not None:
    print("Value has been set")

# AVOID — technically works but not idiomatic
if value == None:
    print("This works but don't do it")
```

### Why `is` Instead of `==`?

1. **`is` checks identity** — is this the exact same object?
2. **`==` checks equality** — do these objects have the same value?

Since there's only one `None` object, `is` is both faster and more explicit about your intent.
It also avoids edge cases where a custom class might override `__eq__`:

``` python {title="The == Gotcha" linenums="1"}
class Sneaky:
    def __eq__(self, other):
        return True  # Claims to equal everything!

sneaky = Sneaky()
print(sneaky == None)   # True — but sneaky isn't None!
print(sneaky is None)   # False — correct answer
```

!!! warning "Linters Will Complain"

    Tools like `flake8` and `pylint` will flag `== None` as a code smell. Use `is None`
    to keep your code clean and your linters happy.

## None and Truthiness

`None` is *falsy* — it evaluates to `False` in a boolean context:

``` python {title="None is Falsy" linenums="1"}
if not None:
    print("None is falsy!")  # This prints

# Same as
if None:
    print("This won't print")
else:
    print("None is falsy!")  # This prints
```

### The Truthiness Trap

Because `None` is falsy, you need to be careful when checking for it:

``` python {title="Distinguishing None from Other Falsy Values" linenums="1"}
def process(value):
    # This treats None, 0, "", and [] the same!
    if not value:
        print("No value provided")
        return

    print(f"Processing: {value}")

process(None)  # "No value provided" — correct
process(0)     # "No value provided" — but 0 IS a value!
process("")    # "No value provided" — but "" might be intentional!
```

If you need to specifically check for `None` while allowing other falsy values:

``` python {title="Explicit None Check" linenums="1"}
def process(value):
    if value is None:
        print("No value provided")
        return

    print(f"Processing: {value}")

process(None)  # "No value provided"
process(0)     # "Processing: 0" — zero is processed!
process("")    # "Processing: " — empty string is processed!
```

## Common Patterns

### Guard Clauses

Return early if a required value is `None`:

``` python {title="Guard Clause Pattern" linenums="1"}
def send_email(user):
    if user is None:
        return  # Can't send to nobody

    if user.email is None:
        print(f"No email for {user.name}")
        return

    # Now we know user and user.email exist
    actually_send_email(user.email)
```

### The `or` Default (With Caution)

You can use `or` to provide a fallback, but be aware of the truthiness trap:

``` python {title="The or Pattern" linenums="1"}
# Works for None
name = None
display_name = name or "Anonymous"
print(display_name)  # "Anonymous"

# But watch out for other falsy values
count = 0
display_count = count or 10
print(display_count)  # 10 — oops! We wanted 0!

# Safer version for when 0/""/[] might be valid
display_count = count if count is not None else 10
print(display_count)  # 0 — correct!
```

### Optional Chaining (Python 3.8+)

The walrus operator can help with None checks:

``` python {title="Walrus Operator with None" linenums="1"}
# Instead of:
result = get_user()
if result is not None:
    process(result)

# You can write:
if (result := get_user()) is not None:
    process(result)
```

## Type Hints with None

When using type hints, `None` has its own type annotation:

``` python {title="Type Hints with None" linenums="1"}
from typing import Optional

# A function that might return None
def find_user(user_id: int) -> Optional[str]:
    """Returns username or None if not found."""
    users = {1: "alice", 2: "bob"}
    return users.get(user_id)

# Parameter that could be None
def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

# Python 3.10+ allows the shorter syntax
def greet(name: str | None = None) -> str:
    ...
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **What it is** | The absence of a value — not zero, not empty, not false |
| **Singleton** | There's only one `None` object in Python |
| **Check with `is`** | Always `is None` or `is not None`, never `== None` |
| **Falsy** | `None` evaluates to `False` in boolean contexts |
| **Function returns** | Functions without `return` implicitly return `None` |
| **Default parameters** | Use `None` for optional params, especially with mutable types |
| **Type hint** | `Optional[X]` or `X | None` (Python 3.10+) |
