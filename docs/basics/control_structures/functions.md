# Functions

A function is a reusable block of code that performs a single task and can be used repeatedly in
programs. Think of functions like your morning coffee routine ☕ — you don't reinvent it every day,
you just *call* it and let it do its thing.

## What is a Function?

In Python, a basic function can be declared as follows:

``` python {title="Declaring a Basic Function" linenums="1"}
def add_numbers(a:int, b:int) -> int:
    return a+b
```

In the above example, the following items should be noted:

- The `def` keyword declares the start of a function
- The name of this function is `add_numbers`
- The function accepts two arguments, `a` and `b`.
    - Each argument can be labelled to show the expected data type (i.e. `a:int` shows that the
      `a` argument is expecting an `int`).
    - The `-> int` declares that the function will `return` an integer (see below).
- Similar to other Python constructs, the declaration line ends with a colon (`:`).
- In standard circumstances, a Python function will return a value

## Functions Are Repeatable

Functions are useful for repeated actions. A famous principle of software development is "Don't
Repeat Yourself" (aka DRY code). Copy-pasting is for amateurs. 😉 As an example, writing the same message to multiple users could
be performed as follows:

``` python {title="Inefficient Repeated Code" linenums="1"}
user1 = "Carl"
user2 = "Jim"
user3 = "Fred"

print("Greetings " + user1 + ", welcome to this program.")
print("Greetings " + user2 + ", welcome to this program.")
print("Greetings " + user3 + ", welcome to this program.")
```

The same lines are being repeated over and over. This could be re-written as a function:

``` python {title="Declaring a Function to Avoid Repeated Code" linenums="1"}
def greet(user:str) -> str:
    return "Greetings " + user + ", welcome to this program."

user1 = "Carl"
user2 = "Jim"
user3 = "Fred"

print(greet(user1))
print(greet(user2))
print(greet(user3))
```

Both examples will have the same output, but using the function will require less effort from the
programmer and will be much more robust and maintainable.

## Looping Over a Function

There are often scenarios where we must execute a function multiple times with different inputs.
This repetitive task can be efficiently accomplished using a
 [`for` loop](../control_structures/for_loops.md).

Consider a situation where you have a function that performs a specific task or computation, and
you need to apply this function to a collection of values or items. Instead of manually calling
the function for each input, which can be tedious and error-prone, you can harness the for loop’s
capabilities to automate this process. Looping over a function allows you to:

- **Reuse Code**: You can encapsulate a specific functionality within a function and then
  effortlessly apply it to multiple data points without duplicating code.
- **Efficiency**: Automating repetitive tasks enhances code efficiency, making it easier
  to maintain and less prone to errors.
- **Scalability**: As your data set grows, using loops to apply a function becomes indispensable,
  ensuring your code remains adaptable to various input sizes.

Let’s illustrate this concept with an example using a temperature conversion function,
`celsius_to_kelvin()`, which converts Celsius temperatures to Kelvin:

``` python {title="Looping Over a Function" linenums="1"}
def celsius_to_kelvin(cels):
    return cels + 273.15

for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))
```

Would result in:

```text
282.25
281.95
3.0
```

During the loop, `celsius_to_kelvin()` is executed with the values 9.1, 8.8, and -270.15,
respectively, demonstrating the power of automating repetitive tasks through function
iteration.

## Default Parameter Values

Parameters can have default values, making them optional when calling the function:

``` python {title="Default Parameters" linenums="1"}
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))                    # Hello, Alice!
print(greet("Bob", "Hi"))                # Hi, Bob!
print(greet("Charlie", "Hey", "..."))    # Hey, Charlie...
```

!!! warning "Mutable Default Arguments"

    Never use mutable objects (lists, dicts) as default values — they're shared across calls!

    ```python
    # DON'T do this:
    def add_item(item, items=[]):  # Bug! The list persists
        items.append(item)
        return items

    # DO this instead:
    def add_item(item, items=None):
        if items is None:
            items = []
        items.append(item)
        return items
    ```

### Keyword Arguments

You can specify arguments by name, allowing you to skip defaults or reorder:

``` python {title="Keyword Arguments" linenums="1"}
def create_user(username, email, is_admin=False, is_active=True):
    return {
        "username": username,
        "email": email,
        "is_admin": is_admin,
        "is_active": is_active
    }

# Skip is_admin, just set is_active
user = create_user("alice", "alice@example.com", is_active=False)
print(user)
```

## *args: Variable Positional Arguments

Sometimes you don't know how many arguments will be passed. The `*args` syntax collects
extra positional arguments into a tuple:

``` python {title="*args" linenums="1"}
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100
print(sum_all())                # 0
```

The name `args` is convention — you could use `*values` or `*items`. The `*` is what matters.

``` python {title="Combining Regular and *args" linenums="1"}
def introduce(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

introduce("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

## **kwargs: Variable Keyword Arguments

Similarly, `**kwargs` collects extra keyword arguments into a dictionary:

``` python {title="**kwargs" linenums="1"}
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# name: Alice
# age: 30
# city: New York
```

### The Full Parameter Order

When combining all parameter types, they must appear in this order:

``` python {title="Complete Parameter Order" linenums="1"}
def complex_function(
    required,           # 1. Regular positional arguments
    default="value",    # 2. Arguments with defaults
    *args,              # 3. *args (variable positional)
    keyword_only=True,  # 4. Keyword-only arguments (after *args)
    **kwargs            # 5. **kwargs (variable keyword) — always last
):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Keyword only: {keyword_only}")
    print(f"Kwargs: {kwargs}")

complex_function("hello", "world", 1, 2, 3, keyword_only=False, extra="data")
```

!!! tip "In Practice"

    You rarely need all five. The most common combinations are:

    - `def f(a, b, c=None)` — regular with optional
    - `def f(*args)` — variable number of same-type items
    - `def f(**kwargs)` — configuration-style functions
    - `def f(*args, **kwargs)` — wrapper functions that pass everything through

## Returning Multiple Values

Python functions can return multiple values using tuple packing:

``` python {title="Multiple Return Values" linenums="1"}
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Unpack the returned tuple
minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or keep as tuple
result = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(result)  # (1, 9)
```

``` python {title="Returning Named Data" linenums="1"}
def analyze_text(text):
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "unique_words": len(set(words))
    }

stats = analyze_text("the quick brown fox jumps over the lazy dog")
print(stats)
# {'word_count': 9, 'char_count': 43, 'unique_words': 8}
```

## Docstrings

Docstrings are special strings that document what a function does. They appear right after
the function definition:

``` python {title="Basic Docstring" linenums="1"}
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
```

For more complex functions, use a multi-line docstring:

``` python {title="Detailed Docstring" linenums="1"}
def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        The BMI value as a float.

    Raises:
        ValueError: If height is zero or negative.

    Example:
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)
```

!!! note "Accessing Docstrings"

    You can access a function's docstring with `function_name.__doc__` or `help(function_name)`.

## Lambda Functions

Lambda functions are anonymous, single-expression functions. They're useful for short
operations, especially when passing functions as arguments:

``` python {title="Lambda Syntax" linenums="1"}
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25
```

### Where Lambdas Shine

Lambdas are most useful with functions like `sorted()`, `map()`, `filter()`:

``` python {title="Lambdas in Action" linenums="1"}
# Sorting by a custom key
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade (ascending)
by_grade = sorted(students, key=lambda s: s["grade"])
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by name length (descending)
by_name_length = sorted(students, key=lambda s: len(s["name"]), reverse=True)
print([s["name"] for s in by_name_length])  # ['Charlie', 'Alice', 'Bob']
```

``` python {title="map() and filter() with Lambdas" linenums="1"}
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter for even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# But comprehensions are often cleaner!
squared = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
```

!!! warning "Lambda Limitations"

    Lambdas are limited to a single expression — no statements, no assignments, no multiple lines.
    If you need more complexity, use a regular `def` function. Readability counts! 📖

## Variable Scope

Variables in Python have different *scopes* — regions where they're accessible.

### Local Scope

Variables defined inside a function are local to that function:

``` python {title="Local Scope" linenums="1"}
def my_function():
    message = "I'm local!"  # Only exists inside this function
    print(message)

my_function()  # I'm local!
# print(message)  # NameError: 'message' is not defined
```

### Global Scope

Variables defined at the module level are global:

``` python {title="Global Scope" linenums="1"}
greeting = "Hello"  # Global variable

def say_hello(name):
    print(f"{greeting}, {name}!")  # Can READ global variables

say_hello("World")  # Hello, World!
```

### Modifying Global Variables

To *modify* a global variable inside a function, use the `global` keyword:

``` python {title="The global Keyword" linenums="1"}
counter = 0

def increment():
    global counter  # Declare we want the global one
    counter += 1

increment()
increment()
print(counter)  # 2
```

!!! warning "Use Sparingly"

    Modifying global variables can make code hard to reason about. Prefer returning values
    and passing parameters. If you find yourself using `global` a lot, consider refactoring. 🔧

### The `nonlocal` Keyword

For nested functions, `nonlocal` lets you modify variables from an enclosing (but not global) scope:

``` python {title="nonlocal for Nested Functions" linenums="1"}
def outer():
    count = 0

    def inner():
        nonlocal count  # Modify the enclosing scope's 'count'
        count += 1
        print(f"Count: {count}")

    inner()  # Count: 1
    inner()  # Count: 2
    inner()  # Count: 3

outer()
```

### Scope Lookup Order (LEGB Rule)

Python looks up names in this order:

1. **L**ocal — inside the current function
2. **E**nclosing — in enclosing functions (for nested functions)
3. **G**lobal — at the module level
4. **B**uilt-in — Python's built-in names (`print`, `len`, etc.)

``` python {title="LEGB in Action" linenums="1"}
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local

    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

## Type Hints

Python 3.5+ supports type hints (annotations) that document expected types:

``` python {title="Type Hints" linenums="1"}
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:
    return {item: len(item) for item in items}
```

Type hints are optional and don't affect runtime behavior — Python won't raise an error
if you pass the wrong type. They're primarily for:

- Documentation
- IDE autocompletion
- Static type checkers like `mypy`

``` python {title="Optional and Union Types" linenums="1"}
from typing import Optional, Union

def find_user(user_id: int) -> Optional[dict]:
    """Return user dict or None if not found."""
    # ...
    return None

def process(value: Union[int, str]) -> str:
    """Accept either int or str."""
    return str(value)

# Python 3.10+ syntax:
def process_new(value: int | str) -> str:
    return str(value)
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Default parameters** | `def f(x, y=10)` — defaults come after required |
| **Keyword arguments** | `f(y=5, x=3)` — specify by name |
| **\*args** | Collect extra positional args into a tuple |
| **\*\*kwargs** | Collect extra keyword args into a dict |
| **Multiple returns** | `return a, b` — returns a tuple |
| **Docstrings** | `"""Documentation"""` right after `def` |
| **Lambda** | `lambda x: x * 2` — anonymous single-expression function |
| **Local scope** | Variables inside function aren't visible outside |
| **global** | Declare intent to modify a global variable |
| **nonlocal** | Modify variable from enclosing function scope |
| **Type hints** | `def f(x: int) -> str:` — for documentation and tools |
