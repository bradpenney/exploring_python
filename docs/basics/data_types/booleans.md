# Booleans

A `boolean` is akin to a digital switch, representing a binary state that can be "on" or "off".
Booleans, a fundamental data type in Python, provides a simple yet powerful way to express
conditions and make decisions in your code. They are the cornerstone of control statements
like [`if/else`](../control_structures/if_statements.md) statements and
[`while` loops](../control_structures/while_loops.md), allowing you to create dynamic,
responsive programs.

Booleans can take on one of two values: `True` or `False`. These values act as signals to guide
your program's logic and flow. Whether you’'re validating user input, iterating through data,
or responding to external conditions, booleans are your code’s decision-makers.

Let’s delve into the world of booleans in Python with some practical examples:

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
