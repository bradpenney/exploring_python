# While Loops

Unlike `for` loops, `while` loops are non-deterministic – the program (and programmer!) doesn't
always know how many times the loop will repeat before it finally calls it quits. Instead, it
depends on a particular condition – usually waiting for a boolean to flip from `True` to
`False`. 🕵️‍♂️

??? danger

     If the condition never becomes `False`, an _infinite_ loop can be created. If you encounter
     an infinite loop, usually `Ctrl+C` will kill the program (for basic scripting).
     _(Don't worry, it happens to everyone! Even the pros forget to escape sometimes. 🏃‍♂️💨)_

The basic form of a `while` loop is:

```python
while expr:
    <code block>
```

The expression is evaluated at the start of each loop, and if it is `True`, the loop will run.
It's like a party that keeps going as long as the music is playing! 🎶

For example:

```python
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

```python
value = 10

while value > 0:
    print(f"Current value: {value}")
    value -= 1  # Decrease the value by 1 each iteration
print("Loop has ended. All done! 🏁")
```

??? challenge

     Try writing your own `while` loop that is different from the examples above!
     Bonus points for creativity – maybe count sheep, print emojis, or make a countdown to pizza time! 🍕⏳