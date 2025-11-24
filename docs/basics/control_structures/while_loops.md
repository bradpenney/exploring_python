# While Loops

Unlike `for` loops, `while` loops are non-deterministic – the program (and programmer!) doesn't
always know how many times the loop will repeat before it finally calls it quits. Instead, it
depends on a particular condition – usually waiting for a [`boolean`](../data_types/booleans.md)
to flip from `True` to `False`. 🕵️‍♂️

??? danger

     If the condition never becomes `False`, an _infinite_ loop can be created. If you encounter
     an infinite loop, usually `Ctrl+C` will kill the program (for basic scripting).
     _(Don't worry, it happens to everyone! Even the pros forget to escape sometimes. 🏃‍♂️💨)_

The basic form of a `while` loop is:

``` python {title="Basic While Loop" linenums="1"}
while expr:
    <code block>
```

The expression is evaluated at the start of each loop, and if it is `True`, the loop will run.
It's like a party that keeps going as long as the music is playing! 🎶

For example:

``` python {title='Loop Until "Exit"' linenums="1"}
keep_looping = True
while keep_looping:
    user_input = input("Enter 'exit' to stop the loop: ")
    if user_input.lower() == 'exit':
        print("Exiting the loop. Goodbye! 👋")
        keep_looping = False
    else:
        print(f"You entered: {user_input} 🤖")
```

Until the user enters "exit", this loop will keep echoing the user input infinitely.
Careful not to get stuck in an infinite loop.

??? tip

     It is possible that a `while` loop will never run if, when it is reached, the condition
     it checks is already `False`. 🚫

Another common pattern is to check equality and increment/decrement the value on each iteration:

``` python {title="Loop Until Value is Zero" linenums="1"}
value = 10

while value > 0:
    print(f"Current value: {value}")
    value -= 1  # Decrease the value by 1 each iteration
print("Loop has ended. All done! 🏁")
```

## The `while True` Pattern

One of the most common patterns is `while True` with an explicit `break` to exit. This is
perfect when you don't know up front how many iterations you'll need:

``` python {title="While True with Break" linenums="1"}
while True:
    user_input = input("Enter a number (or 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Goodbye! 👋")
        break

    try:
        number = int(user_input)
        print(f"You entered: {number}")
    except ValueError:
        print("That's not a valid number. Try again!")
```

This reads as: "Keep looping forever, until we explicitly break out." It's cleaner than
managing a separate boolean flag in many cases.

## Input Validation Loop

A classic use case — keep asking until the user gives valid input. Like a barista who won't
let you leave without confirming your order. ☕

``` python {title="Input Validation" linenums="1"}
while True:
    age_str = input("Enter your age: ")

    if not age_str.isdigit():
        print("❌ Please enter a valid number.")
        continue

    age = int(age_str)

    if age < 0 or age > 150:
        print("❌ That doesn't seem like a realistic age...")
        continue

    # If we get here, input is valid!
    break

print(f"✅ Got it! You are {age} years old.")
```

!!! tip "Validation Pattern"

    The pattern is: loop forever, `continue` on bad input (to retry), `break` on good input.
    Simple and effective. 🎯

## Sentinel Value Pattern

Sometimes you loop until you encounter a special "sentinel" value that signals the end:

``` python {title="Sentinel Value" linenums="1"}
print("Enter numbers to sum (enter 0 to finish):")
total = 0

while True:
    num = int(input("Number: "))
    if num == 0:  # Sentinel value
        break
    total += num

print(f"Sum: {total}")
```

Common sentinel values include `0`, `-1`, empty string `""`, or `None`.

## Processing Until Exhausted

While loops excel when you're consuming from a source until it's empty:

``` python {title="Processing a Stack" linenums="1"}
tasks = ["Write code", "Review PR", "Deploy", "Test"]

while tasks:  # Truthy check — empty list is False
    current_task = tasks.pop()
    print(f"Working on: {current_task}")
    print(f"  (Tasks remaining: {len(tasks)})")

print("All done! 🎉")
```

Returns:

``` text
Working on: Test
  (Tasks remaining: 3)
Working on: Deploy
  (Tasks remaining: 2)
Working on: Review PR
  (Tasks remaining: 1)
Working on: Write code
  (Tasks remaining: 0)
All done! 🎉
```

## Retry with Limits

Don't let your program try forever — add a maximum attempt count:

``` python {title="Retry with Maximum Attempts" linenums="1"}
import random

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    attempts += 1
    password = input(f"Enter password (attempt {attempts}/{max_attempts}): ")

    if password == "secret123":
        print("✅ Access granted!")
        break
    else:
        print("❌ Wrong password.")
else:
    # This runs if we exit normally (no break) — meaning all attempts failed
    print("🔒 Account locked. Too many failed attempts.")
```

!!! note "The else Clause"

    Just like `for` loops, `while` loops can have an `else` clause. It runs only if the loop
    completes normally (without a `break`). See [Controlling Loops](controlling_loops.md)
    for more.

## Waiting for a Condition

While loops are great for polling or waiting:

``` python {title="Waiting for a Condition" linenums="1"}
import time

# Simulating waiting for a resource
retries = 0
max_retries = 5
resource_ready = False

while not resource_ready and retries < max_retries:
    print(f"Checking resource... (attempt {retries + 1})")
    # In real code, you'd check an actual condition here
    retries += 1
    time.sleep(0.5)  # Wait half a second

    if retries >= 3:  # Simulate resource becoming ready
        resource_ready = True

if resource_ready:
    print("Resource is ready! ✅")
else:
    print("Resource never became ready 😞")
```

## Intentional Infinite Loops

Some programs *should* run forever — like servers, game loops, or monitoring scripts:

``` python {title="Game Loop (Conceptual)" linenums="1"}
# A simplified game loop structure
running = True

while running:
    # 1. Handle input
    # events = get_events()

    # 2. Update game state
    # update_game(events)

    # 3. Render
    # draw_screen()

    # 4. Check for quit
    # if quit_requested:
    #     running = False
    pass  # In a real game, this would be the loop content
```

``` python {title="Simple Server Loop (Conceptual)" linenums="1"}
# Conceptual — real servers use frameworks
while True:
    # connection = wait_for_connection()
    # request = read_request(connection)
    # response = process_request(request)
    # send_response(connection, response)
    pass
```

!!! warning "Breaking Out of Infinite Loops"

    During development, if you accidentally create an infinite loop:

    - In a terminal: Press `Ctrl+C` to send a keyboard interrupt
    - In an IDE: Use the stop/kill button
    - As a last resort: Force quit the process

    This happens to everyone. It's practically a rite of passage. 🎓

## for vs while: When to Use Each

| Use `for` when... | Use `while` when... |
|:------------------|:--------------------|
| Iterating over a known sequence | Number of iterations is unknown |
| Processing each item in a collection | Waiting for a condition to change |
| Counting a specific number of times | Input validation loops |
| Using `enumerate()` or `zip()` | Implementing retry logic |
| The loop should end naturally | You need `while True` with `break` |

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Basic while** | `while condition:` — loops while condition is True |
| **while True** | Common pattern with explicit `break` |
| **Input validation** | Loop with `continue` (retry) and `break` (success) |
| **Sentinel values** | Special value that signals end of input |
| **Retry with limits** | Add a counter to prevent infinite attempts |
| **else clause** | Runs if loop completes without `break` |
| **Infinite by design** | Some programs (servers, games) intentionally run forever |
