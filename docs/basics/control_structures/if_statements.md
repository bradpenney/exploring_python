# `if` Statements

Grant admin access only if credentials match. Charge shipping fees based on order total and destination. Display different error messages depending on what went wrong. Calculate letter grades from numeric scores. Route HTTP requests to different handlers based on the URL path.

Every one of these requires your program to choose between different paths of execution. That's what `if` statements enable: conditional logic that makes programs adaptive, responsive, and intelligent. They're the foundation of [control flow](https://cs.bradpenney.io/fundamentals/computational_thinking/#algorithmic-thinking)—the ability to make decisions based on conditions.

## What is an If Statement?

An `if` statement evaluates a [boolean](../data_types/booleans.md) condition and executes a block of code only when that condition is `True`:

```python title="Basic If Statement" linenums="1"
age = 25
if age >= 18:  # (1)!
    print("You can vote!")
```

1. The condition `age >= 18` evaluates to `True` or `False`—if `True`, the indented block executes

You can extend this with `elif` (else if) to check multiple conditions in sequence, and `else` to handle cases where none of the conditions matched:

```python title="If-Elif-Else Structure" linenums="1"
score = 85

if score >= 90:  # (1)!
    print("A")
elif score >= 80:  # (2)!
    print("B")
elif score >= 70:
    print("C")
else:  # (3)!
    print("F")
```

1. Checks the first condition—if `True`, prints "A" and skips the rest
2. Only evaluated if the previous `if` was `False`—checks conditions in order
3. The fallback—executes only if all previous conditions were `False`

## Why If Statements Matter

If statements transform static code into adaptive programs:

- **Access control**: Check permissions before allowing operations—authentication, authorization, admin features
- **Input validation**: Verify data meets requirements before processing—email format, password strength, age restrictions
- **Error handling**: Different responses based on what went wrong—404 vs 500 errors, network failures vs invalid input
- **Business logic**: Calculate pricing, apply discounts, determine shipping costs based on complex rules
- **State management**: Different behavior based on current state—game over vs playing, logged in vs logged out
- **Data filtering**: Include or exclude items based on criteria—search results, active users, valid transactions

Without conditional logic, every program would execute the same way every time. If statements enable programs to respond to their environment.

## Common Patterns

### Simple If-Else: Binary Decisions

Check a score threshold. Validate user age. Test if a file exists—any yes/no decision:

```python title="Game Win Condition" linenums="1"
player_score = 47
winning_score = 100

if player_score >= winning_score:  # (1)!
    print("YOU WIN!")
else:
    print(f"You need {winning_score - player_score} more points to win!")  # (2)!
```

1. Simple comparison—`True` if player has reached or exceeded the threshold
2. F-string calculates the remaining points needed—output: "You need 53 more points to win!"

### Combining Conditions: AND/OR Logic

Authenticate users. Check multiple requirements. Validate complex eligibility—combine [boolean](../data_types/booleans.md) operators:

```python title="User Authentication" linenums="1"
user_input_username = "john_doe"
user_input_password = "secure_password"

correct_username = "john_doe"
correct_password = "secure_password"

if user_input_username == correct_username and \
   user_input_password == correct_password:  # (1)!
    print("Access granted!")
else:
    print("Access denied. Please check your username and password.")
```

1. Both conditions must be `True`—the backslash (`\`) continues the line for readability. You could also write this on one line or use parentheses.

### Multiple Conditions: If-Elif-Else Chains

Grade assignment. Tax brackets. Shipping zones. Priority levels—sequential condition checking:

```python title="Grade Calculation" linenums="1"
student_score = 85

if student_score >= 90:  # (1)!
    grade = "A"
elif student_score >= 80:  # (2)!
    grade = "B"
elif student_score >= 70:
    grade = "C"
elif student_score >= 60:
    grade = "D"
else:  # (3)!
    grade = "F"

print(f"Grade: {grade}")  # Grade: B
```

1. Python checks conditions from top to bottom—first match wins
2. Only checked if the `if` (and any preceding `elif`) failed—order matters!
3. The catch-all—executes if no previous condition matched

## Nested Conditionals

Check driver eligibility (age, license, insurance). Process payments (valid card, sufficient funds, fraud check). Validate forms (all fields present, correct format, unique email). Sometimes one decision leads to another:

```python title="Nested If Statements" linenums="1"
age = 25
has_license = True
has_insurance = True

if age >= 16:  # (1)!
    if has_license:
        if has_insurance:
            print("You can drive!")
        else:
            print("You need insurance first.")
    else:
        print("You need a license first.")
else:
    print("You're too young to drive.")
```

1. Three levels of nesting—each decision depends on the previous one being `True`

While nesting works, too many levels make code hard to follow. Flatten with [boolean operators](../data_types/booleans.md) or use [guard clauses in functions](../control_structures/functions.md):

```python title="Flattened Conditionals" linenums="1"
# More readable alternative using 'and'
if age >= 16 and has_license and has_insurance:  # (1)!
    print("You can drive!")
elif age < 16:
    print("You're too young to drive.")
elif not has_license:
    print("You need a license first.")
else:
    print("You need insurance first.")
```

1. Single condition combining all requirements—easier to read and test

!!! warning "Avoid Deep Nesting"

    Nesting more than 2-3 levels deep usually signals a need to refactor. Extract [functions](../control_structures/functions.md), combine conditions with `and`/`or`, or use early returns.

## The Ternary Operator (Conditional Expression)

Set default values. Format output based on a condition. Assign variables conditionally in one line—the ternary operator handles simple either/or logic concisely:

```python title="Ternary Operator Basics" linenums="1"
# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Same logic as a ternary expression
status = "adult" if age >= 18 else "minor"  # (1)!
print(status)  # adult
```

1. Syntax: `value_if_true if condition else value_if_false`—condition is evaluated, then one of the two values is returned

```python title="Practical Ternary Examples" linenums="1"
# Setting defaults
name = user_input if user_input else "Anonymous"  # (1)!

# Quick formatting
score = 85
grade = "Pass" if score >= 60 else "Fail"  # (2)!

# Nested ternary (use sparingly!)
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"  # (3)!
```

1. If `user_input` is truthy, use it; otherwise default to "Anonymous"—leverages [truthiness](../data_types/booleans.md#truthiness-what-python-considers-true-or-false)
2. Binary decision—pass/fail based on threshold
3. Multiple conditions chained—works but quickly becomes hard to read

!!! warning "When to Avoid Ternaries"

    Ternary expressions are elegant for simple either/or logic. Chaining them (nested ternaries) sacrifices readability. If you need multiple conditions, use `if-elif-else` instead. [PEP 8](https://peps.python.org/pep-0008/) emphasizes: "Readability counts."

## Match Statements (Python 3.10+)

Parse HTTP status codes. Route commands. Handle event types. Process structured data. Python 3.10 introduced `match` statements—pattern matching that goes far beyond simple equality checks:

```python title="Basic Match Statement" linenums="1"
def http_status(status):
    match status:  # (1)!
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # (2)!
            return "Unknown status"

print(http_status(200))  # OK
print(http_status(418))  # Unknown status
```

1. The `match` statement evaluates `status` once, then checks it against each `case` pattern
2. The underscore (`_`) is a wildcard—matches anything not caught by previous cases (like `else` in if-elif-else)

### Matching Multiple Values

Weekend vs weekday logic. Categorizing user roles. Grouping similar cases—the pipe operator (`|`) matches any of several values:

```python title="Matching Multiple Values" linenums="1"
def classify_day(day):
    match day.lower():
        case "saturday" | "sunday":  # (1)!
            return "Weekend!"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Not a valid day"

print(classify_day("Saturday"))  # Weekend!
```

1. The pipe (`|`) operator means "or"—matches if the value equals any of the options listed

### Matching with Guards

Categorize numbers by properties. Filter data based on conditions. Add complex validation—guards combine pattern matching with conditional logic:

```python title="Match with Guards" linenums="1"
def categorize_number(n):
    match n:
        case n if n < 0:  # (1)!
            return "Negative"
        case 0:  # (2)!
            return "Zero"
        case n if n % 2 == 0:
            return "Positive even"
        case _:
            return "Positive odd"

print(categorize_number(-5))   # Negative
print(categorize_number(0))    # Zero
print(categorize_number(4))    # Positive even
print(categorize_number(7))    # Positive odd
```

1. The `if` after the pattern is a guard—pattern matches any value, but only proceeds if `n < 0`
2. Exact value match—no guard needed for simple equality

### Matching Sequences and Structures

Parse command strings. Process API responses. Route structured data. Destructure [tuples](../../data_structures/tuples.md) and [lists](../../data_structures/lists.md)—`match` excels at pattern matching complex data:

```python title="Matching List Patterns" linenums="1"
def process_command(command):
    match command.split():  # (1)!
        case ["quit"]:
            return "Goodbye!"
        case ["hello", name]:  # (2)!
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Result: {int(x) + int(y)}"
        case ["move", direction, steps]:
            return f"Moving {direction} by {steps} steps"
        case _:
            return "Unknown command"

print(process_command("quit"))           # Goodbye!
print(process_command("hello World"))    # Hello, World!
print(process_command("add 5 3"))        # Result: 8
```

1. Splits the string into a list, then matches against list patterns
2. Matches a 2-element list where first element is "hello"—second element is captured in variable `name`

```python title="Matching Dictionary Patterns" linenums="1"
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:  # (1)!
            return f"Click at ({x}, {y})"
        case {"type": "keypress", "key": key}:
            return f"Key pressed: {key}"
        case {"type": "scroll", "direction": d}:
            return f"Scrolling {d}"
        case _:
            return "Unknown event"

print(handle_event({"type": "click", "x": 100, "y": 200}))  # Click at (100, 200)
print(handle_event({"type": "keypress", "key": "Enter"}))   # Key pressed: Enter
```

1. Matches [dictionaries](../../data_structures/dictionaries.md) with specific keys—values are captured into variables

??? tip "When to Use Match vs If-Elif"

    `match` excels at:

    - Handling multiple specific values (HTTP status codes, command types, state values)
    - Destructuring complex data structures (lists, dicts, tuples from APIs or parsed data)
    - Making state machines and command parsers more readable
    - Pattern matching with guards for complex filtering

    Use `if-elif-else` for:

    - Simple boolean conditions and range checks
    - Code that needs to run on Python <3.10
    - When you don't need destructuring or pattern matching

## Practice Problems

??? question "Practice Problem 1: Basic If-Else"

    What will this code print?

    ```python
    temperature = 25
    if temperature > 30:
        print("Hot")
    elif temperature > 20:
        print("Warm")
    else:
        print("Cold")
    ```

    ??? tip "Answer"

        It prints `"Warm"`.

        The first condition (`temperature > 30`) is `False` (25 is not greater than 30). Python then checks the `elif` condition (`temperature > 20`), which is `True` (25 > 20), so it prints "Warm" and skips the `else` block.

??? question "Practice Problem 2: Ternary Operator"

    Rewrite this if-else block as a ternary expression:

    ```python
    x = 15
    if x % 2 == 0:
        result = "even"
    else:
        result = "odd"
    ```

    ??? tip "Answer"

        ```python
        x = 15
        result = "even" if x % 2 == 0 else "odd"
        ```

        The ternary syntax is: `value_if_true if condition else value_if_false`. Since `x % 2 == 0` is the condition, "even" is returned if true, "odd" if false.

??? question "Practice Problem 3: Nested vs Flattened"

    Why is the second version better than the first?

    ```python
    # Version 1
    if age >= 18:
        if has_id:
            if not is_banned:
                print("Entry allowed")

    # Version 2
    if age >= 18 and has_id and not is_banned:
        print("Entry allowed")
    ```

    ??? tip "Answer"

        Version 2 is better because:

        - **Readability**: Single line condition is easier to understand than 3 levels of nesting
        - **Maintainability**: Easier to modify or add conditions
        - **Pythonic**: Combining conditions with `and`/`or` is idiomatic Python

        Version 1 forces you to track indentation levels to understand the logic. Version 2 makes all requirements explicit in one place.

??? question "Practice Problem 4: Match Statements"

    What does this match statement do differently than an if-elif chain?

    ```python
    match command.split():
        case ["move", direction, steps]:
            move(direction, int(steps))
        case ["quit"]:
            exit()
    ```

    ??? tip "Answer"

        The match statement **destructures** the list and captures values into variables.

        - `["move", direction, steps]` matches a 3-element list where the first element is "move", then captures the second and third elements into `direction` and `steps` variables
        - An if-elif chain would need manual indexing: `if parts[0] == "move": direction = parts[1]; steps = parts[2]`

        This destructuring makes parsing structured data much cleaner than traditional conditionals.

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **if-elif-else** | The workhorse of decision-making |
| **Nested conditionals** | Useful but flatten when possible |
| **Ternary operator** | `value_if_true if condition else value_if_false` |
| **match (3.10+)** | Pattern matching with destructuring |
| **Wildcard `_`** | Matches anything in match statements |
| **Guards** | Add `if` conditions to match cases |

## Further Reading

- [**Python If Statements Documentation**](https://docs.python.org/3/tutorial/controlflow.html#if-statements) - Official tutorial on conditional statements
- [**PEP 622 – Structural Pattern Matching**](https://peps.python.org/pep-0622/) - The proposal that introduced match statements in Python 3.10
- [**PEP 634 – Structural Pattern Matching: Specification**](https://peps.python.org/pep-0634/) - Complete specification for match syntax
- [**PEP 8 – Style Guide**](https://peps.python.org/pep-0008/#programming-recommendations) - Best practices for writing conditionals
- [**Computational Thinking**](https://cs.bradpenney.io/fundamentals/computational_thinking/#algorithmic-thinking) - Understanding control flow and decision-making in algorithms

---

Conditionals are the decision-making heart of every program. Without them, code executes linearly, the same way every time—deterministic but inflexible. `if` statements introduce adaptability, enabling programs to respond to data, user input, and changing conditions.

Master the fundamentals: `if-elif-else` for sequential conditions, ternary operators for simple assignments, nested conditionals flattened with boolean logic. Then level up with Python 3.10's `match` statements—pattern matching that destructures data structures elegantly. Each approach has its place: use the simplest tool that clearly expresses your intent. Readability counts.
