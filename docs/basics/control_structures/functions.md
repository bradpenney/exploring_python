# Functions

A function is a reusable block of code that performs a single task and can be used repeatedly in
programs. In Python, a basic function can be declared as follows:

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

Functions are useful for repeated actions. A famous principle of software development is “Don’t
Repeat Yourself” (aka DRY code). As an example, writing the same message to multiple users could
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
