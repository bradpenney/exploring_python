# Functions

A function is a reusable block of code that performs a single task and can be used repeatedly in
programs.

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
