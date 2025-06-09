# `if` Statements

Decision-making is a fundamental concept in programming, and the `if-elif-else` statement in Python
is a powerful tool for precisely that purpose. These statements allow you to create dynamic,
branching logic within your programs. With them, you can instruct your code to take different
actions based on specific conditions, making your programs more intelligent and responsive.

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
essential for building responsive and intelligent software.
