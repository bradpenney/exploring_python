# `if` Statements

Decision-making is a fundamental concept in programming, and the `if-elif-else` statement in Python
is a powerful tool for precisely that purpose. 🤔 Should I stay or should I go? Should I have
another coffee or switch to decaf? (The answer is always more coffee.) These statements allow you
to create dynamic, branching logic within your programs. With them, you can instruct your code to
take different actions based on specific conditions, making your programs more intelligent and
responsive.

## What & Why?

An `if-elif-else` statement is a control structure in Python that enables your program to make
choices. It starts with an `if` statement that checks a particular condition. If that condition
is `True`, a specific block of code is executed. However, if the condition is not met, the program
can continue to evaluate other conditions using `elif` (short for “else if”) statements. These
`elif` clauses allow for multiple conditions to be checked sequentially. Finally, if none of the
preceding conditions are `True`, the else code block is executed.

??? tip "See Also"

    `if/else` statements evaluate to `True` or `False` - which are `boolean` values.  See
    [Booleans](../data_types/booleans.md) for more details.

The primary purpose of `if-elif-else` statements is to introduce decision-making capabilities
into your code. They allow your program to adapt and respond to varying situations. There are
three examples below of how you might use `if-elif-else` statements to implement logic:

### Example 1: Game Over Conditions

``` python {title="If-Else Statement Use Case: Game Over Conditions" linenums="1"}
# Determine if a player’s score has reached a winning threshold.
# If yes, declare a winner; otherwise, continue the game.

player_1_score = 47

if (player_1_score >= 100):
    print("YOU WIN!")
else:
    print(f"You need {100 - player_1_score} more points to win!")
```
Would return:
``` text
You need 53 more points to win!
```

### Example 2: User Authentication

``` python {title="If-Else Statement Use Case: User Authentication" linenums="1"}
# Check if a user’s credentials are correct.
# If they are, grant access; otherwise, deny access.

user_input_username = "john_doe"
user_input_password = "secure_password"

correct_username = "john_doe"
correct_password = "secure_password"

if user_input_username == correct_username and \ # (1)
    user_input_password == correct_password:
     print("Access granted!")
else:
     print("Access denied. Please check your username and password.")
```

1. The preceeding backslash is a *line continuation*.   Both of these conditions are evaluated
   in the `if` statement.

Would result in:
``` text
Access granted!
```

### Example 3: Grade Evaluation
``` python {title="If-Else Statement Use Case: Grade Evaluation" linenums="1"}
# Determine a student's letter grade based on their numeric grade.

student_score = 85

if student_score >= 90:
    print("A")
elif student_score >= 80:
    print("B")
elif student_score >= 70:
    print("C")
elif student_score >= 60:
    print("D")
else:
    print("F")
```

Would output:

``` text
B
```

In these examples, `if-elif-else` statements allow the program to take different actions depending
on specific conditions. They provide the flexibility to handle a wide range of scenarios and are
essential for building responsive and intelligent software. 🧠

## Nested Conditionals

Sometimes one decision leads to another. You can nest `if` statements inside each other to handle
more complex logic:

``` python {title="Nested If Statements" linenums="1"}
age = 25
has_license = True
has_insurance = True

if age >= 16:
    if has_license:
        if has_insurance:
            print("You can drive! 🚗")
        else:
            print("You need insurance first.")
    else:
        print("You need a license first.")
else:
    print("You're too young to drive.")
```

While nesting works, too many levels can make code hard to follow. Consider flattening with
`and`/`or` operators or using early returns in functions:

``` python {title="Flattening Nested Conditionals" linenums="1"}
# More readable alternative using 'and'
if age >= 16 and has_license and has_insurance:
    print("You can drive! 🚗")
elif age < 16:
    print("You're too young to drive.")
elif not has_license:
    print("You need a license first.")
else:
    print("You need insurance first.")
```

!!! tip "The Rule of Thumb"

    If you find yourself nesting more than 2-3 levels deep, it's usually a sign to refactor.
    Your future self will thank you. 🙏

## The Ternary Operator (Conditional Expression)

For simple either/or assignments, Python offers a compact one-liner syntax:

``` python {title="Ternary Operator" linenums="1"}
# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Same thing as a ternary expression
status = "adult" if age >= 18 else "minor"
print(status)  # adult
```

The syntax is: `value_if_true if condition else value_if_false`

``` python {title="Ternary Examples" linenums="1"}
# Setting defaults
name = user_input if user_input else "Anonymous"

# Quick formatting
score = 85
grade = "Pass" if score >= 60 else "Fail"

# Nested ternary (use sparingly!)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

!!! warning "Nested Ternaries"

    While you *can* chain ternary expressions, they quickly become unreadable. If you need
    multiple conditions, stick with `if-elif-else`. Readability counts. 📖

## Match Statements (Python 3.10+)

Python 3.10 introduced `match` statements — a powerful pattern matching feature that's like
`if-elif` on steroids. Think of it as a sophisticated switch statement:

``` python {title="Basic Match Statement" linenums="1"}
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # The underscore is a wildcard (matches anything)
            return "Unknown status"

print(http_status(200))  # OK
print(http_status(418))  # Unknown status
```

### Matching Multiple Values

``` python {title="Matching Multiple Values" linenums="1"}
def classify_day(day):
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend! 🎉"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday 💼"
        case _:
            return "Not a valid day"

print(classify_day("Saturday"))  # Weekend! 🎉
```

### Matching with Guards

Add `if` conditions to patterns for more precise matching:

``` python {title="Match with Guards" linenums="1"}
def categorize_number(n):
    match n:
        case n if n < 0:
            return "Negative"
        case 0:
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

### Matching Sequences and Structures

This is where `match` really shines — destructuring data structures:

``` python {title="Matching Sequences" linenums="1"}
def process_command(command):
    match command.split():
        case ["quit"]:
            return "Goodbye!"
        case ["hello", name]:
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

``` python {title="Matching Dictionaries" linenums="1"}
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
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

!!! note "When to Use Match"

    `match` excels at:

    - Handling multiple specific values (like HTTP status codes or commands)
    - Destructuring complex data structures (lists, dicts, tuples)
    - Making state machines and command parsers readable

    For simple boolean conditions, `if-elif-else` is still your friend.

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **if-elif-else** | The workhorse of decision-making |
| **Nested conditionals** | Useful but flatten when possible |
| **Ternary operator** | `value_if_true if condition else value_if_false` |
| **match (3.10+)** | Pattern matching with destructuring |
| **Wildcard `_`** | Matches anything in match statements |
| **Guards** | Add `if` conditions to match cases |
