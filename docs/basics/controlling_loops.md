# Controlling Loops

Loops in Python are great for repetition — but sometimes, you need to take control.
Maybe you want to **skip ahead**, **stop early**, or **do something special at the end**.
That’s where the loop control keywords `continue`, `break`, and `else` come in.

This guide explores how these keywords work and shows you how to use them effectively —
with a few playful examples along the way.


## Continuing a Loop
Sometimes, we want to skip over part of a loop's work for a particular iteration without stopping
the whole thing.  That’s where `continue` comes in — it tells the loop:
*“Skip the rest of this turn, move on to the next!”*

``` python
colours = ["red", "green", "blue", "orange"]

for colour in colours:
    if colour == "orange":
        print("Ugh, orange again? Let's pretend we didn't see that.")
        continue
    print(f"Ooooh, I totally dig the colour {colour}!")

```

Would result in:
``` bash
Ooooh, I totally dig the colour red!
Ooooh, I totally dig the colour green!
Ooooh, I totally dig the colour blue!
Ugh, orange again? Let's pretend we didn't see that.
```

??? tip

    Often, continue can be replaced by simply using an if statement to wrap the block of code.
    For example: if colour != "orange": print(...) would achieve the same result.
    That said, continue can be helpful for readability — just use it mindfully.

## Breaking a Loop
Sometimes, we want to stop a loop entirely when something important happens.
This is known as *abnormal termination*, and the `break` statement is your go-to tool.

In the example below, we simulate a bank account that refuses to go into the red:

``` python
balance = 100
withdrawals = [10, 23, 12, 16, 43, 19, 4, 5]

for withdrawal in withdrawals:
    print(f"📤 Request to withdraw ${withdrawal}...")

    if (balance - withdrawal) < 0:
        print("🚨 Uh-oh! You're broke. No more money magic today.")
        break

    balance -= withdrawal
    print(f"✅ Success! You withdrew ${withdrawal}. Remaining balance: ${balance}")
```

Would result in:

``` bash
📤 Request to withdraw $10...
✅ Success! You withdrew $10. Remaining balance: $90
📤 Request to withdraw $23...
✅ Success! You withdrew $23. Remaining balance: $67
📤 Request to withdraw $12...
✅ Success! You withdrew $12. Remaining balance: $55
📤 Request to withdraw $16...
✅ Success! You withdrew $16. Remaining balance: $39
📤 Request to withdraw $43...
🚨 Uh-oh! You're broke. No more money magic today.
```

Like the `continue` statement, `break` should also be used with caution.  In the example above
the same funtionality could have been achieved with a `while` loop.  Use with discretion!

### Using Else with For Loops
One of Python’s lesser-known features is the ability to attach an `else` block to a loop.
This block will run *only if the loop completes naturally* — that is, not interrupted by a
`break`.

Here’s a playful example that builds on our earlier scenario:

``` python
balance = 200
withdrawals = [10, 23, 12, 16, 43, 19, 4, 5]

print("💸 Time for a little shopping adventure!")

for withdrawal in withdrawals:
    print(f"🛒 You spot something for ${withdrawal}...")

    if (balance - withdrawal) < 0:
        print("😱 Your wallet gasps in horror — not enough cash!")
        print("💀 The spree ends here, friend.")
        break

    balance -= withdrawal
    print(f"🎉 Purchase successful! You’ve got ${balance} left in your treasure chest.")
else:
    print("🎊 You made it through your spree without going broke!")
```

Would result in:

``` bash
💸 Time for a little shopping adventure!
🛒 You spot something for $10...
🎉 Purchase successful! You’ve got $190 left in your treasure chest.
🛒 You spot something for $23...
🎉 Purchase successful! You’ve got $167 left in your treasure chest.
🛒 You spot something for $12...
🎉 Purchase successful! You’ve got $155 left in your treasure chest.
🛒 You spot something for $16...
🎉 Purchase successful! You’ve got $139 left in your treasure chest.
🛒 You spot something for $43...
🎉 Purchase successful! You’ve got $96 left in your treasure chest.
🛒 You spot something for $19...
🎉 Purchase successful! You’ve got $77 left in your treasure chest.
🛒 You spot something for $4...
🎉 Purchase successful! You’ve got $73 left in your treasure chest.
🛒 You spot something for $5...
🎉 Purchase successful! You’ve got $68 left in your treasure chest.
🎊 You made it through your spree without going broke!
```

Using else in loops isn’t especially common, but when used well, it can express logic cleanly —
particularly in search loops, or when you want to take special action only if no early exit
occurred.