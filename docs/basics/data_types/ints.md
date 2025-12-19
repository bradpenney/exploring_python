# Integers

Integers, data type `int`, are interpreted as numbers, enabling you to perform standard
mathematical operations efficiently. Integers represent whole numbers, crucial for various
mathematical and computational tasks. No decimal nonsense here — just clean, whole numbers. 🔢

Declaring integers in Python is a breeze, following the same straightforward syntax used for all
variables. You assign a value to a variable name using the assignment operator (`=`). For instance,
you can declare integers like this:

``` python {title="Declaring Integer Variables" linenums="1"}
rank = 10
eggs = 12
people = 3
negative_temp = -15  # Negative integers work too
big_number = 1_000_000  # Underscores for readability (Python 3.6+)
```

!!! tip "Readable Large Numbers"

    Python lets you use underscores in numbers for readability. `1_000_000` is the same as
    `1000000`, but much easier to read. Your eyes will thank you. 👀

??? tip "Combining Integers with Strings"

    Exercise caution when combining an `int` with a `string`. To ensure correct output, you must
    *cast* the `int` as a `string` within the context of the `print()` statement. For example,
    when working with the variable `my_age = 12`, a standard concatenated print statement would
    need to *cast* the variable like this: `print("My age is " + str(my_age))`. This casting
    operation ensures that the `int` value of `my_age` is correctly interpreted as part of the
    `string`. Python can also handle this automatically through the use of "F-strings" (the
    preferred approach).

## Arithmetic Operations

The primary use of an `int` in Python is mathematical operations. Whether you're calculating the
area of geometric shapes, managing quantities, or working on numerical algorithms, integers are
essential.

### Basic Operators

``` python {title="Basic Arithmetic" linenums="1"}
a = 10
b = 3

print(a + b)   # 13  — Addition
print(a - b)   # 7   — Subtraction
print(a * b)   # 30  — Multiplication
print(a ** b)  # 1000 — Exponentiation (10³)
```

### Division: The Three Flavors 🍦

This is where integers get interesting. Python has *three* different division operators:

``` python {title="Division Types" linenums="1"}
a = 17
b = 5

print(a / b)   # 3.4  — True division (always returns a float!)
print(a // b)  # 3    — Floor division (rounds down to nearest integer)
print(a % b)   # 2    — Modulo (remainder after division)
```

Let's break these down:

| Operator | Name | What It Does | Result Type |
|:---------|:-----|:-------------|:------------|
| `/` | True division | Divides and keeps decimals | Always `float` |
| `//` | Floor division | Divides and rounds *down* | `int` if both operands are `int` |
| `%` | Modulo | Returns the remainder | `int` if both operands are `int` |

!!! warning "True Division Always Returns a Float"

    Even if the division is "clean," `/` returns a float:

    ```python
    print(10 / 2)   # 5.0, not 5
    print(type(10 / 2))  # <class 'float'>
    ```

    If you need an integer result, use `//` or wrap in `int()`.

### Floor Division with Negative Numbers

Here's a gotcha that trips people up — floor division rounds toward *negative infinity*, not
toward zero:

``` python {title="Floor Division Gotcha" linenums="1"}
print(17 // 5)    # 3   — rounds down from 3.4
print(-17 // 5)   # -4  — rounds down from -3.4 (toward negative infinity!)
print(17 // -5)   # -4  — same deal
```

This is mathematically consistent but can be surprising if you expect truncation toward zero.

### The Modulo Operator in Action

The modulo operator (`%`) is more useful than it might seem:

``` python {title="Practical Modulo Uses" linenums="1"}
# Check if a number is even or odd
number = 42
if number % 2 == 0:
    print("Even")  # This prints
else:
    print("Odd")

# Wrap around (like a clock)
hour = 14
print(hour % 12)  # 2 — 24-hour to 12-hour conversion

# Check divisibility
if 100 % 25 == 0:
    print("100 is divisible by 25")  # This prints

# Cycle through a list
colors = ["red", "green", "blue"]
for i in range(10):
    print(colors[i % len(colors)])  # Cycles: red, green, blue, red, green...
```

## Operator Precedence

Python follows standard mathematical order of operations (PEMDAS/BODMAS):

``` python {title="Order of Operations" linenums="1"}
result = 2 + 3 * 4      # 14, not 20 (multiplication first)
result = (2 + 3) * 4    # 20 (parentheses override)
result = 2 ** 3 ** 2    # 512 (exponentiation is right-to-left: 3² = 9, then 2⁹)
result = 10 - 3 - 2     # 5 (subtraction is left-to-right: 7 - 2)
```

| Priority | Operators | Description |
|:---------|:----------|:------------|
| 1 (highest) | `**` | Exponentiation |
| 2 | `+x`, `-x` | Unary plus/minus |
| 3 | `*`, `/`, `//`, `%` | Multiplication, division, modulo |
| 4 (lowest) | `+`, `-` | Addition, subtraction |

!!! tip "When in Doubt, Use Parentheses"

    Even if you know the precedence rules, parentheses make your intent clear:

    ```python
    # Confusing
    result = a + b * c / d - e ** f

    # Clear
    result = a + ((b * c) / d) - (e ** f)
    ```

## Useful Integer Functions

Python provides several built-in functions for working with integers:

``` python {title="Handy Integer Functions" linenums="1"}
# Absolute value
print(abs(-42))      # 42
print(abs(42))       # 42

# Power (alternative to **)
print(pow(2, 10))    # 1024
print(pow(2, 10, 100))  # 24 — pow with modulo: (2¹⁰) % 100

# Min and max
print(min(5, 3, 8, 1))  # 1
print(max(5, 3, 8, 1))  # 8

# Sum of an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

# divmod — returns both quotient and remainder
quotient, remainder = divmod(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")  # 17 ÷ 5 = 3 remainder 2
```

## Number Systems

Python can work with numbers in different bases. This is handy when dealing with
low-level programming, networking, or just impressing your friends. 🤓

### Binary, Octal, and Hexadecimal Literals

``` python {title="Different Number Bases" linenums="1"}
decimal = 255        # Base 10 (normal)
binary = 0b11111111  # Base 2 (prefix: 0b)
octal = 0o377        # Base 8 (prefix: 0o)
hexadecimal = 0xFF   # Base 16 (prefix: 0x)

# They're all the same number!
print(decimal == binary == octal == hexadecimal)  # True
print(decimal, binary, octal, hexadecimal)  # 255 255 255 255
```

### Converting Between Bases

``` python {title="Base Conversion" linenums="1"}
number = 255

# Convert to string representation in different bases
print(bin(number))   # '0b11111111'
print(oct(number))   # '0o377'
print(hex(number))   # '0xff'

# Convert string back to int (specify the base)
print(int('11111111', 2))   # 255 — from binary
print(int('377', 8))        # 255 — from octal
print(int('FF', 16))        # 255 — from hex
print(int('ff', 16))        # 255 — hex is case-insensitive
```

??? example "When Would You Use This?"

    - **Binary**: Bit manipulation, flags, permissions
    - **Hexadecimal**: Colors (`#FF5733`), memory addresses, MAC addresses
    - **Octal**: Unix file permissions (`chmod 755`)

    ```python
    # RGB color as hex
    red = 0xFF
    green = 0x57
    blue = 0x33
    print(f"#{red:02X}{green:02X}{blue:02X}")  # #FF5733

    # Unix permissions
    rwx_owner = 0o700   # Read, write, execute for owner
    rx_group = 0o050    # Read, execute for group
    rx_other = 0o005    # Read, execute for others
    permissions = rwx_owner | rx_group | rx_other
    print(oct(permissions))  # 0o755
    ```

## Python's Unlimited Integer Size

Unlike many programming languages, Python integers have no maximum size. They can be as
large as your memory allows:

``` python {title="Big Numbers" linenums="1"}
# This is perfectly valid Python
huge = 10 ** 100  # A googol
print(huge)
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# Calculate factorial of 100
import math
print(math.factorial(100))  # A 158-digit number!
```

!!! note "No Integer Overflow"

    In languages like C or Java, integers have fixed sizes (32-bit, 64-bit) and can overflow.
    Python handles this automatically by switching to arbitrary-precision arithmetic. You'll
    never see an integer overflow in Python — just potentially slow calculations with very
    large numbers.

## Converting To and From Integers

``` python {title="Type Conversion" linenums="1"}
# String to integer
age = int("25")
print(age + 1)  # 26

# Float to integer (truncates toward zero!)
print(int(3.9))    # 3
print(int(-3.9))   # -3 (not -4!)

# Boolean to integer
print(int(True))   # 1
print(int(False))  # 0

# Integer to string
count = 42
message = "The answer is " + str(count)
print(message)  # The answer is 42

# Check if something is an integer
print(isinstance(42, int))     # True
print(isinstance(42.0, int))   # False
```

!!! warning "int() Truncates, Not Rounds"

    `int()` always truncates toward zero, which is different from `round()` or floor division:

    ```python
    print(int(3.9))    # 3 (truncated)
    print(round(3.9))  # 4 (rounded)
    print(int(-3.9))   # -3 (truncated toward zero)
    print(-3.9 // 1)   # -4.0 (floor division toward negative infinity)
    ```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Division types** | `/` (float), `//` (floor), `%` (modulo) |
| **True division** | Always returns a float, even for `10 / 2` |
| **Floor division** | Rounds toward negative infinity, not zero |
| **Modulo** | Great for even/odd, cycling, divisibility |
| **Precedence** | `**` → `* / // %` → `+ -` (use parentheses!) |
| **Number bases** | `0b` (binary), `0o` (octal), `0x` (hex) |
| **No overflow** | Python integers can be arbitrarily large |
| **int() truncates** | Toward zero, not rounding |
