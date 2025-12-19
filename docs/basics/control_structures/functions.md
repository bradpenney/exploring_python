# Functions

Validate user email formats. Calculate shipping costs. Send welcome emails. Parse JSON responses. Format database queries. Hash passwords. Convert temperatures. Every one of these tasks gets repeated throughout your codebase—sometimes hundreds of times.

Functions let you write the logic once, name it, and reuse it everywhere. They're the fundamental building block of code organization, enabling you to break complex programs into manageable, testable, reusable pieces. Master functions, and you master [abstraction](https://cs.bradpenney.io/fundamentals/computational_thinking/#abstraction)—one of the core principles of programming.

## What is a Function?

A function is a named, reusable block of code that performs a specific task. You define it once with `def`, then call it as many times as needed:

```python title="Basic Function" linenums="1"
def add_numbers(a: int, b: int) -> int:  # (1)!
    return a + b  # (2)!

result = add_numbers(5, 3)  # (3)!
print(result)  # 8
```

1. Function definition: `def` keyword, name (`add_numbers`), parameters with type hints (`a: int, b: int`), return type annotation (`-> int`), colon
2. The `return` statement sends a value back to the caller—this function returns the sum
3. Function call: use the function name with parentheses and arguments—the function executes and returns `8`

Function anatomy:

- **`def` keyword**: Declares the start of a function definition
- **Function name**: Identifies the function (use descriptive names: `calculate_tax`, not `ct`)
- **Parameters**: Inputs the function accepts (can be zero or more)
- **Type hints** (optional): Document expected types—`a: int` means `a` should be an integer, `-> int` means it returns an integer
- **Colon**: Marks the end of the definition line
- **Indented body**: The code that runs when the function is called
- **`return` statement**: Sends a value back to the caller (optional—functions without `return` implicitly return `None`)

## Why Functions Matter

Functions are how programmers manage complexity. They enable:

- **Code reuse**: Write once, use everywhere—email validation, tax calculation, data formatting all become one-liners
- **Maintainability**: Fix a bug in one place, and every call gets the fix—no hunting through thousands of lines for copy-pasted code
- **Testability**: Test a function in isolation with known inputs and expected outputs—much easier than testing entire programs
- **Abstraction**: Hide complex logic behind simple names—`send_email()` is clearer than 50 lines of SMTP protocol code
- **Organization**: Break 1000-line scripts into 20 well-named functions—each does one thing well
- **Collaboration**: Teams can work on different functions simultaneously—clear interfaces between components

Without functions, every program would be a linear script. Functions transform code from a sequence of instructions into a collection of reusable tools.

## DRY: Don't Repeat Yourself

Send the same welcome message to multiple users. Apply the same validation to multiple form fields. Calculate the same metric for different datasets. Repetition is code smell—functions eliminate it:

```python title="Repetitive Code (Don't Do This)" linenums="1"
user1 = "Carl"
user2 = "Jim"
user3 = "Fred"

print("Greetings " + user1 + ", welcome to this program.")  # (1)!
print("Greetings " + user2 + ", welcome to this program.")
print("Greetings " + user3 + ", welcome to this program.")
```

1. Same string concatenation repeated three times—error-prone and hard to change

```python title="DRY with Functions" linenums="1"
def greet(user: str) -> str:  # (1)!
    return f"Greetings {user}, welcome to this program."

users = ["Carl", "Jim", "Fred"]  # (2)!
for user in users:
    print(greet(user))
```

1. Define the logic once—now changing the greeting message requires editing one line, not three (or hundreds)
2. Combine with a [for loop](for_loops.md) to process any number of users—scales from 3 to 3000

## Functions with Loops

Convert multiple temperatures. Process a batch of files. Validate a [list](../../data_structures/lists.md) of email addresses—apply the same function to different inputs by combining functions with [`for` loops](for_loops.md):

```python title="Applying Functions to Multiple Inputs" linenums="1"
def celsius_to_kelvin(celsius: float) -> float:  # (1)!
    return celsius + 273.15

temperatures_c = [9.1, 8.8, -270.15]
for temp in temperatures_c:  # (2)!
    kelvin = celsius_to_kelvin(temp)
    print(f"{temp}°C = {kelvin}K")
```

1. Define the conversion logic once—this function handles any single temperature
2. Loop over the [list](../../data_structures/lists.md) and apply the function to each element—output: "9.1°C = 282.25K", "8.8°C = 281.95K", "-270.15°C = 3.0K"

This pattern—define function, apply to collection—is fundamental to data processing. You could process 3 temperatures or 3 million with the same code.

## Default Parameter Values

Greeting messages with customizable text. API calls with optional parameters. Configuration functions with sensible defaults—default values make parameters optional:

```python title="Default Parameters" linenums="1"
def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:  # (1)!
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))                    # (2)!
print(greet("Bob", "Hi"))                # (3)!
print(greet("Charlie", "Hey", "..."))    # Hey, Charlie...
```

1. Parameters with `=` have defaults—`greeting` defaults to "Hello", `punctuation` to "!" if not provided
2. Uses both defaults: "Hello, Alice!"
3. Overrides first default but uses second: "Hi, Bob!"

!!! warning "Mutable Default Arguments Trap"

    Never use mutable objects ([lists](../../data_structures/lists.md), [dicts](../../data_structures/dictionaries.md)) as default values—they're shared across all calls and cause subtle bugs!

    ```python title="The Bug" linenums="1"
    # DON'T do this:
    def add_item(item, items=[]):  # (1)!
        items.append(item)
        return items

    print(add_item("apple"))   # ['apple'] — looks fine
    print(add_item("banana"))  # ['apple', 'banana'] — WHAT?!
    ```

    1. The empty list is created once when the function is defined, not each time it's called—all calls share the same list!

    ```python title="The Fix" linenums="1"
    # DO this instead:
    def add_item(item, items=None):  # (1)!
        if items is None:
            items = []  # (2)!
        items.append(item)
        return items

    print(add_item("apple"))   # ['apple']
    print(add_item("banana"))  # ['banana'] — correct!
    ```

    1. Use `None` as the sentinel value for "no list provided"
    2. Create a new list inside the function—each call gets its own list

### Keyword Arguments

Create users with optional flags. Configure functions with many parameters. Make calls self-documenting—keyword arguments let you specify parameters by name:

```python title="Keyword Arguments" linenums="1"
def create_user(username: str, email: str, is_admin: bool = False, is_active: bool = True) -> dict:  # (1)!
    return {
        "username": username,
        "email": email,
        "is_admin": is_admin,
        "is_active": is_active
    }

user = create_user("alice", "alice@example.com", is_active=False)  # (2)!
print(user)  # {'username': 'alice', 'email': 'alice@example.com', 'is_admin': False, 'is_active': False}
```

1. Function has 2 required parameters and 2 optional parameters with defaults
2. Specify `is_active` by name, skip `is_admin` (uses default `False`)—keyword arguments make the call self-documenting

## *args: Variable Positional Arguments

Sum any number of values. Concatenate multiple [strings](../data_types/strings.md). Find the maximum of an unknown quantity of numbers—`*args` accepts any number of positional arguments:

```python title="Variable Positional Arguments" linenums="1"
def sum_all(*numbers):  # (1)!
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100  (2)!
print(sum_all())                # 0   (3)!
```

1. `*numbers` collects all positional arguments into a [tuple](../../data_structures/tuples.md) named `numbers`—you can pass 0, 1, or 100 arguments
2. Four arguments → `numbers` becomes `(10, 20, 30, 40)`
3. Zero arguments → `numbers` becomes `()` (empty tuple)

The name `args` is convention—you could use `*values` or `*items`. The asterisk (`*`) is what triggers the behavior.

```python title="Mixing Required and *args" linenums="1"
def introduce(greeting: str, *names: str) -> None:  # (1)!
    for name in names:
        print(f"{greeting}, {name}!")

introduce("Hello", "Alice", "Bob", "Charlie")  # (2)!
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

1. `greeting` is required, `*names` collects all remaining arguments—must have at least one argument (the greeting)
2. "Hello" fills `greeting`, the rest go into `names` tuple

## **kwargs: Variable Keyword Arguments

Configuration functions. Building [dictionaries](../../data_structures/dictionaries.md) from arguments. Flexible API wrappers—`**kwargs` accepts any number of keyword arguments:

```python title="Variable Keyword Arguments" linenums="1"
def print_info(**kwargs):  # (1)!
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")  # (2)!
# name: Alice
# age: 30
# city: New York
```

1. `**kwargs` collects all keyword arguments into a [dictionary](../../data_structures/dictionaries.md) named `kwargs`
2. Three keyword arguments → `kwargs` becomes `{"name": "Alice", "age": 30, "city": "New York"}`

### The Full Parameter Order

When mixing parameter types, they must appear in this strict order:

```python title="Complete Parameter Order" linenums="1"
def complex_function(
    required,           # (1)!
    default="value",    # (2)!
    *args,              # (3)!
    keyword_only=True,  # (4)!
    **kwargs            # (5)!
):
    print(f"Required: {required}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Keyword only: {keyword_only}")
    print(f"Kwargs: {kwargs}")

complex_function("hello", "world", 1, 2, 3, keyword_only=False, extra="data")
# Required: hello
# Default: world
# Args: (1, 2, 3)
# Keyword only: False
# Kwargs: {'extra': 'data'}
```

1. Regular positional arguments—must come first
2. Parameters with defaults—after required positionals
3. `*args` for variable positional—collects extras into tuple
4. Keyword-only parameters (after `*args`)—can only be set by name
5. `**kwargs` for variable keyword—always last, collects extras into dict

??? tip "Common Patterns in Practice"

    You rarely need all five. The most common combinations:

    - `def f(a, b, c=None)` — required with optional defaults
    - `def f(*args)` — variable number of same-type items (sum, max, concatenate)
    - `def f(**kwargs)` — configuration functions, flexible APIs
    - `def f(*args, **kwargs)` — wrapper functions that forward everything to another function

## Returning Multiple Values

Get min and max in one call. Return status code and message. Calculate multiple statistics—functions can return multiple values via [tuple](../../data_structures/tuples.md) packing:

```python title="Tuple Packing for Multiple Returns" linenums="1"
def get_min_max(numbers: list[int]) -> tuple[int, int]:  # (1)!
    return min(numbers), max(numbers)  # (2)!

# Unpack the returned tuple
minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])  # (3)!
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or keep as tuple
result = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(result)  # (1, 9)
```

1. Type hint shows function returns a tuple of two integers
2. Comma-separated values create a tuple—`return min(numbers), max(numbers)` is equivalent to `return (min(numbers), max(numbers))`
3. Tuple unpacking assigns each returned value to a variable

```python title="Returning Structured Data" linenums="1"
def analyze_text(text: str) -> dict:  # (1)!
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "unique_words": len(set(words))
    }

stats = analyze_text("the quick brown fox jumps over the lazy dog")
print(stats["word_count"])  # 9
print(stats["unique_words"])  # 8
```

1. Returning a [dictionary](../../data_structures/dictionaries.md) provides named access to multiple values—more self-documenting than tuples for complex data

## Docstrings

Document your functions. Explain parameters and return values. Provide usage examples—docstrings are how Python functions document themselves:

```python title="Basic Docstring" linenums="1"
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""  # (1)!
    return length * width

print(calculate_area.__doc__)  # Calculate the area of a rectangle.
help(calculate_area)  # Shows formatted documentation
```

1. Triple-quoted string immediately after function definition—this is the docstring

For complex functions, use multi-line docstrings with sections:

```python title="Detailed Docstring (Google Style)" linenums="1"
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index (BMI).  # (1)!

    Args:  # (2)!
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:  # (3)!
        The BMI value as a float.

    Raises:  # (4)!
        ValueError: If height is zero or negative.

    Example:  # (5)!
        >>> calculate_bmi(70, 1.75)
        22.857142857142858
    """
    if height_m <= 0:
        raise ValueError("Height must be positive")
    return weight_kg / (height_m ** 2)
```

1. Brief summary on first line
2. Args section documents each parameter
3. Returns section describes the return value
4. Raises section lists exceptions the function can raise
5. Example section shows usage with expected output (doctest format)

??? tip "Accessing Docstrings Programmatically"

    Access docstrings with `__doc__` attribute or `help()` function:

    ```python
    print(calculate_bmi.__doc__)  # Prints the docstring
    help(calculate_bmi)  # Displays formatted documentation
    ```

## Lambda Functions

Sort by custom criteria. Transform data inline. Quick callback functions—lambdas are anonymous, single-expression functions for short operations:

```python title="Lambda Syntax" linenums="1"
# Regular function
def square(x: int) -> int:
    return x ** 2

# Equivalent lambda
square_lambda = lambda x: x ** 2  # (1)!

print(square(5))         # 25
print(square_lambda(5))  # 25
```

1. Lambda syntax: `lambda parameters: expression`—no `def`, no `return`, single expression only

### Where Lambdas Shine

Lambdas excel as arguments to functions like `sorted()`, `map()`, `filter()`:

```python title="Sorting with Lambda Keys" linenums="1"
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade (ascending)
by_grade = sorted(students, key=lambda s: s["grade"])  # (1)!
print([s["name"] for s in by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by name length (descending)
by_name_length = sorted(students, key=lambda s: len(s["name"]), reverse=True)
print([s["name"] for s in by_name_length])  # ['Charlie', 'Alice', 'Bob']
```

1. The `key` parameter takes a function that extracts the sort value—lambda provides an inline function without needing `def`

```python title="map() and filter() with Lambdas" linenums="1"
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))  # (1)!
print(squared)  # [1, 4, 9, 16, 25]

# Filter for even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))  # (2)!
print(evens)  # [2, 4]

# But comprehensions are often cleaner!
squared = [x ** 2 for x in numbers]  # (3)!
evens = [x for x in numbers if x % 2 == 0]
```

1. `map()` applies the lambda to each element—transforms [1, 2, 3] → [1, 4, 9]
2. `filter()` keeps only elements where the lambda returns `True`
3. List comprehensions are often more Pythonic than `map()`/`filter()` with lambdas

!!! warning "Lambda Limitations"

    Lambdas are limited to a **single expression**—no statements, no assignments, no multiple lines. If you need `if`/`else` logic beyond a ternary expression, multiple operations, or better debugging, use a regular `def` function. [PEP 8](https://peps.python.org/pep-0008/): "Readability counts."

## Variable Scope

Which variables can this function see? Can I modify that global counter? What happens when nested functions use the same name? Scope rules determine where variables are accessible:

### Local Scope

Variables defined inside a function exist only within that function:

```python title="Local Scope" linenums="1"
def my_function():
    message = "I'm local!"  # (1)!
    print(message)

my_function()  # I'm local!
# print(message)  # (2)!
```

1. `message` only exists inside `my_function`—created when function runs, destroyed when it returns
2. Would raise `NameError: name 'message' is not defined`—`message` doesn't exist outside the function

### Global Scope

Variables defined at module level are accessible everywhere:

```python title="Global Scope" linenums="1"
greeting = "Hello"  # (1)!

def say_hello(name: str) -> None:
    print(f"{greeting}, {name}!")  # (2)!

say_hello("World")  # Hello, World!
```

1. `greeting` is global—defined outside any function
2. Functions can read global variables—`greeting` is accessible here

### Modifying Global Variables

To modify a global variable inside a function, explicitly declare it with `global`:

```python title="The global Keyword" linenums="1"
counter = 0

def increment():
    global counter  # (1)!
    counter += 1

increment()
increment()
print(counter)  # 2
```

1. `global counter` tells Python "I want to modify the global `counter`, not create a new local one"—without this, `counter += 1` would raise `UnboundLocalError`

!!! warning "Global Variables Are Code Smell"

    Modifying global variables makes code hard to test and reason about—functions have hidden dependencies. Prefer returning values and passing parameters. If you're using `global` frequently, refactor to classes or pass state explicitly.

### The `nonlocal` Keyword

For nested functions, `nonlocal` modifies variables from enclosing (non-global) scopes:

```python title="nonlocal for Nested Functions" linenums="1"
def outer():
    count = 0  # (1)!

    def inner():
        nonlocal count  # (2)!
        count += 1
        print(f"Count: {count}")

    inner()  # Count: 1
    inner()  # Count: 2
    inner()  # Count: 3

outer()
```

1. `count` is in the enclosing scope—not global, not local to `inner`
2. `nonlocal count` allows `inner` to modify `outer`'s `count` variable

### Scope Lookup Order (LEGB Rule)

Python searches for names in this order:

1. **L**ocal—inside the current function
2. **E**nclosing—in enclosing functions (for nested functions)
3. **G**lobal—at the module level
4. **B**uilt-in—Python's built-in names (`print`, `len`, etc.)

```python title="LEGB in Action" linenums="1"
x = "global"

def outer():
    x = "enclosing"  # (1)!

    def inner():
        x = "local"  # (2)!
        print(x)  # local

    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

1. Each function can have its own `x` variable—they don't conflict
2. Python finds the innermost (most local) `x` first—prints "local", not "enclosing" or "global"

## Type Hints

Document expected types. Enable IDE autocompletion. Catch type errors before runtime—type hints make Python code more maintainable:

```python title="Type Hints Basics" linenums="1"
def greet(name: str) -> str:  # (1)!
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    return a + b

def process_items(items: list[str]) -> dict[str, int]:  # (2)!
    return {item: len(item) for item in items}
```

1. `name: str` means parameter expects a string, `-> str` means function returns a string
2. Generic types like `list[str]` specify the type of elements—list of strings → dictionary of string keys to integer values

Type hints are **optional** and don't affect runtime—Python won't raise errors for wrong types. They're primarily for:

- **Documentation**: Makes function signatures self-documenting
- **IDE support**: Enables autocompletion and inline error checking
- **Static analysis**: Tools like `mypy` catch type errors before runtime
- **Refactoring**: Easier to understand what changes might break

```python title="Optional and Union Types" linenums="1"
from typing import Optional

def find_user(user_id: int) -> Optional[dict]:  # (1)!
    """Return user dict or None if not found."""
    if user_id == 1:
        return {"name": "Alice"}
    return None

def process(value: int | str) -> str:  # (2)!
    """Accept either int or str."""
    return str(value)
```

1. `Optional[dict]` means "either a dict or None"—shorthand for `dict | None`
2. `int | str` means "either an int or a str" (Python 3.10+ syntax, cleaner than `Union[int, str]`)

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

## Practice Problems

??? question "Practice Problem 1: Default Parameters"

    What will this code print?

    ```python
    def greet(name, prefix="Hello"):
        return f"{prefix}, {name}!"

    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    ```

    ??? tip "Answer"

        ```
        Hello, Alice!
        Hi, Bob!
        ```

        The first call uses the default `prefix` ("Hello"). The second call overrides it with "Hi".

??? question "Practice Problem 2: *args"

    What's the difference between these two functions?

    ```python
    def sum_list(numbers):
        return sum(numbers)

    def sum_args(*numbers):
        return sum(numbers)
    ```

    ??? tip "Answer"

        - `sum_list()` takes a single argument (a list): `sum_list([1, 2, 3])`
        - `sum_args()` takes variable positional arguments: `sum_args(1, 2, 3)`

        Both work internally the same way (summing a sequence), but the calling interface differs. `*args` collects multiple arguments into a tuple.

??? question "Practice Problem 3: Scope"

    What does this code print?

    ```python
    x = 10

    def modify_x():
        x = 20
        print(x)

    modify_x()
    print(x)
    ```

    ??? tip "Answer"

        ```
        20
        10
        ```

        The function creates a **local** variable `x = 20`, which only exists inside the function. The global `x` remains unchanged at `10`. To modify the global, you'd need `global x` inside the function.

??? question "Practice Problem 4: Lambda Functions"

    Rewrite this using a lambda function:

    ```python
    def double(x):
        return x * 2

    numbers = [1, 2, 3, 4]
    doubled = list(map(double, numbers))
    ```

    ??? tip "Answer"

        ```python
        numbers = [1, 2, 3, 4]
        doubled = list(map(lambda x: x * 2, numbers))
        ```

        Or even better with a list comprehension:

        ```python
        doubled = [x * 2 for x in numbers]
        ```

## Further Reading

- [**Python Functions Tutorial**](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) - Official documentation on functions
- [**PEP 8 – Style Guide**](https://peps.python.org/pep-0008/#function-and-variable-names) - Function naming conventions and best practices
- [**PEP 257 – Docstring Conventions**](https://peps.python.org/pep-0257/) - How to write good docstrings
- [**PEP 484 – Type Hints**](https://peps.python.org/pep-0484/) - Introduction to type hints in Python
- [**PEP 3107 – Function Annotations**](https://peps.python.org/pep-3107/) - The proposal that introduced function annotations
- [**Computational Thinking: Abstraction**](https://cs.bradpenney.io/fundamentals/computational_thinking/#abstraction) - Understanding functions as abstraction mechanisms

---

Functions are the building blocks of organized, reusable code. They transform repetitive tasks into single, named operations. They enable testing, collaboration, and maintainability. Every complex program is built from simple functions composed together.

Master the fundamentals: parameters, return values, scope. Understand the advanced features: `*args`, `**kwargs`, decorators, closures. Write clear docstrings, use type hints, follow [PEP 8](https://peps.python.org/pep-0008/) naming conventions. A well-written function does one thing, does it well, and has a name that clearly communicates its purpose.

The difference between a script and a program is organization. Functions are how you organize code.
