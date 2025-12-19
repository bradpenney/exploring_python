# Integers

Count users in a database. Calculate pixels on a screen. Track inventory quantities. Process financial transactions. Loop exactly 100 times. Index into the 42nd element of a list.

Every one of these tasks requires whole numbers—integers. No fractions, no decimals, just precise counting and calculation. Integers are Python's workhorse numeric type, appearing in nearly every program you write.

## What is an Integer?

Integers (`int` type) represent whole numbers—positive, negative, or zero:

```python title="Creating Integers" linenums="1"
count = 42                # (1)!
temperature = -15         # (2)!
balance = 0
large_number = 1_000_000  # (3)!
```

1. Positive integers—the most common case
2. Negative integers work identically
3. Underscores improve readability for large numbers (Python 3.6+)—`1_000_000` is the same as `1000000`

Unlike many programming languages where integers have size limits (32-bit, 64-bit), Python integers can be arbitrarily large—limited only by available memory.

## Why Integers Matter

Integers solve fundamental programming problems:

- **Counting**: Users, iterations, items in a collection
- **Indexing**: Accessing elements in sequences ([lists](../../data_structures/lists.md), [strings](strings.md))
- **File I/O**: Byte offsets, line numbers, file sizes
- **Game development**: Scores, health points, coordinates
- **Web applications**: Pagination (page 5 of 100), user IDs
- **Data processing**: Row counts, batch sizes

Every time you use [`range()`](../../control_structures/for_loops.md#the-range-function), index a list, or count occurrences, you're working with integers. They're the foundation of [computational thinking](https://cs.bradpenney.io/fundamentals/computational_thinking/)—the discrete, step-by-step logic that computers excel at.

## Arithmetic Operations

Calculate total price from quantity and unit cost. Determine grid dimensions. Compute elapsed time from timestamps. Scale image coordinates. Integers power these calculations.

### Basic Operators

```python title="Basic Arithmetic" linenums="1"
a = 10
b = 3

print(a + b)   # (1)!
print(a - b)   # (2)!
print(a * b)   # (3)!
print(a ** b)  # (4)!
```

1. Addition: `13`—combining quantities
2. Subtraction: `7`—finding differences, remainders
3. Multiplication: `30`—scaling values, calculating areas
4. Exponentiation: `1000` (10³)—growth rates, compound calculations

### Division: Three Types for Different Needs

Division is where integers reveal their nuances. Python provides three division operators because different problems require different behaviors:

```python title="Division Types" linenums="1"
a = 17
b = 5

print(a / b)   # (1)!
print(a // b)  # (2)!
print(a % b)   # (3)!
```

1. True division: `3.4`—always returns a float, even if the result is a whole number
2. Floor division: `3`—rounds down to the nearest integer (useful for pagination, chunking)
3. Modulo: `2`—returns the remainder after division (essential for cycling, even/odd checks)

**Why three operators?** Different problems need different behaviors:

| Operator | Name | When to Use | Example Use Case |
|:---------|:-----|:------------|:-----------------|
| `/` | True division | Need decimal precision | Calculating averages, percentages |
| `//` | Floor division | Need integer result, round down | Pagination (items per page), splitting into chunks |
| `%` | Modulo | Need remainder | Checking even/odd, cycling through lists, time calculations |

!!! warning "True Division Always Returns a Float"

    Even if the division is "clean," `/` returns a float:

    ```python
    print(10 / 2)   # 5.0, not 5
    print(type(10 / 2))  # <class 'float'>
    ```

    If you need an integer result, use `//` or wrap in `int()`.

### Floor Division with Negative Numbers

Floor division always rounds toward negative infinity—not toward zero. This catches programmers familiar with other languages:

```python title="Floor Division with Negatives" linenums="1"
print(17 // 5)    # (1)!
print(-17 // 5)   # (2)!
print(17 // -5)   # (3)!
```

1. Returns `3`—rounds down from 3.4 as expected
2. Returns `-4`—rounds down from -3.4 (toward negative infinity, not toward zero!)
3. Returns `-4`—same behavior with negative divisor

This is mathematically consistent but surprises those expecting truncation toward zero.

### The Modulo Operator in Real Use

Check if a number is even or odd. Cycle through array indices. Convert 24-hour to 12-hour time. Implement round-robin task assignment. Modulo powers all these patterns:

```python title="Practical Modulo Uses" linenums="1"
# Check if a number is even or odd
number = 42
if number % 2 == 0:  # (1)!
    print("Even")
else:
    print("Odd")

# Wrap around (like a clock)
hour = 14
print(hour % 12)  # (2)!

# Check divisibility
if 100 % 25 == 0:  # (3)!
    print("100 is divisible by 25")

# Cycle through a list
colors = ["red", "green", "blue"]
for i in range(10):  # (4)!
    print(colors[i % len(colors)])  # (5)!
```

1. Even/odd check—[if statement](../../control_structures/if_statements.md) tests if remainder is 0 when divided by 2
2. Returns `2`—converts 14:00 (2 PM) to 12-hour format
3. Divisibility test—remainder of 0 means evenly divisible
4. [For loop](../../control_structures/for_loops.md) with range—common pattern for iteration
5. Cycles through colors: `i % 3` wraps indices 0,1,2,0,1,2... regardless of how large `i` gets

## Operator Precedence

Calculate a discount with tax. Compute compound interest. Convert units with multiple steps. Complex formulas fail when operators execute in the wrong order. Understanding precedence prevents subtle bugs in mathematical expressions:

```python title="Order of Operations" linenums="1"
result = 2 + 3 * 4      # (1)!
result = (2 + 3) * 4    # (2)!
result = 2 ** 3 ** 2    # (3)!
result = 10 - 3 - 2     # (4)!
```

1. Returns `14`, not 20—multiplication happens before addition
2. Returns `20`—parentheses override precedence
3. Returns `512`—exponentiation is right-to-left: 3² = 9, then 2⁹ = 512
4. Returns `5`—subtraction is left-to-right: (10 - 3) - 2 = 7 - 2 = 5

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

Find the largest score in a game. Calculate total sales from a list. Get the distance between two points regardless of direction. These common operations appear in nearly every program—Python provides built-in functions so you don't reinvent them:

```python title="Handy Integer Functions" linenums="1"
# Absolute value
print(abs(-42))      # (1)!
print(abs(42))

# Power (alternative to **)
print(pow(2, 10))    # (2)!
print(pow(2, 10, 100))  # (3)!

# Min and max
print(min(5, 3, 8, 1))  # (4)!
print(max(5, 3, 8, 1))

# Sum of an iterable
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # (5)!

# divmod — returns both quotient and remainder
quotient, remainder = divmod(17, 5)  # (6)!
print(f"17 ÷ 5 = {quotient} remainder {remainder}")
```

1. Returns `42`—`abs()` converts negative to positive (useful for distances, differences)
2. Returns `1024`—`pow(x, y)` is equivalent to `x ** y`
3. Returns `24`—three-argument form: `(2¹⁰) % 100` (efficient for cryptography, large numbers)
4. Returns `1`—finds minimum value (works with any number of arguments or an iterable)
5. Returns `15`—adds all values in a list
6. Returns both quotient (3) and remainder (2) in one operation—more efficient than using `//` and `%` separately

## Number Systems

Parse network packets. Set file permissions on Unix. Define colors for web design. Work with memory addresses. Process bit flags. Different number bases aren't academic—they're practical tools for systems programming, web development, and data processing.

### Why Number Bases Matter

- **Binary (base 2)**: Bit manipulation, flags, permissions, low-level protocols
- **Hexadecimal (base 16)**: Colors (`#FF5733`), memory addresses, MAC addresses, hashing
- **Octal (base 8)**: Unix file permissions (`chmod 755`)

Python lets you write integers in any of these bases:

```python title="Different Number Bases" linenums="1"
decimal = 255        # (1)!
binary = 0b11111111  # (2)!
octal = 0o377        # (3)!
hexadecimal = 0xFF   # (4)!

# They're all the same number!
print(decimal == binary == octal == hexadecimal)  # (5)!
print(decimal, binary, octal, hexadecimal)
```

1. Base 10 (decimal)—the default, what we use daily
2. Base 2 (binary)—prefix `0b`—useful for bit operations
3. Base 8 (octal)—prefix `0o`—used in Unix permissions
4. Base 16 (hexadecimal)—prefix `0x`—common in web colors, memory addresses
5. Returns `True`—all represent 255, just in different notations

### Converting Between Bases

```python title="Base Conversion" linenums="1"
number = 255

# Convert to string representation in different bases
print(bin(number))   # (1)!
print(oct(number))   # (2)!
print(hex(number))   # (3)!

# Convert string back to int (specify the base)
print(int('11111111', 2))   # (4)!
print(int('377', 8))
print(int('FF', 16))
print(int('ff', 16))        # (5)!
```

1. Returns `'0b11111111'`—binary string representation
2. Returns `'0o377'`—octal string representation
3. Returns `'0xff'`—hexadecimal string representation
4. Parse binary string to integer by specifying base 2 as second argument
5. Hexadecimal parsing is case-insensitive—`'FF'` and `'ff'` both work

??? example "Real-World Number Base Examples"

    **Web development—RGB colors**:
    ```python
    # RGB color as hex
    red = 0xFF
    green = 0x57
    blue = 0x33
    print(f"#{red:02X}{green:02X}{blue:02X}")  # #FF5733
    ```

    **Systems programming—Unix permissions**:
    ```python
    # chmod 755 in Python
    rwx_owner = 0o700   # Read, write, execute for owner
    rx_group = 0o050    # Read, execute for group
    rx_other = 0o005    # Read, execute for others
    permissions = rwx_owner | rx_group | rx_other
    print(oct(permissions))  # 0o755
    ```

## Python's Unlimited Integer Size

Calculate factorial of 100. Process credit card numbers. Work with cryptographic keys. Handle astronomical calculations. Generate large prime numbers. In other languages, these tasks hit integer overflow—values wrap around or crash. Python just works:

```python title="Arbitrarily Large Integers" linenums="1"
# This is perfectly valid Python
huge = 10 ** 100  # (1)!
print(huge)

# Calculate factorial of 100
import math
print(math.factorial(100))  # (2)!
```

1. A googol (10¹⁰⁰)—100 digits long! Python handles this without overflow
2. Returns a 158-digit number—no special "big integer" library needed

!!! note "No Integer Overflow"

    Languages like C or Java use fixed-size integers (32-bit, 64-bit) that overflow when values get too large. Python automatically switches to arbitrary-precision arithmetic—you'll never see integer overflow, just potentially slower calculations with very large numbers.

## Converting To and From Integers

Parse user input from a form. Read numeric data from CSV files. Round measurements down to whole units. Display counts in messages. Data arrives in various types—[strings](strings.md) from files, [floats](floats.md) from calculations, [booleans](booleans.md) from logic. Converting between types is constant in real programs:

```python title="Type Conversion" linenums="1"
# String to integer
age = int("25")  # (1)!
print(age + 1)

# Float to integer (truncates toward zero!)
print(int(3.9))    # (2)!
print(int(-3.9))

# Boolean to integer
print(int(True))   # (3)!
print(int(False))

# Integer to string
count = 42
message = f"The answer is {count}"  # (4)!
print(message)

# Check if something is an integer
print(isinstance(42, int))     # (5)!
print(isinstance(42.0, int))
```

1. Parse [string](strings.md) to integer—essential for processing user input, file data
2. Returns `3` (not 4!)—`int()` truncates toward zero, doesn't round (see [floats](floats.md) for precision)
3. Returns `1`—[booleans](booleans.md) convert to 0 and 1 (useful in calculations)
4. [F-strings](strings.md#building-strings-with-f-strings) handle conversion automatically—cleaner than `str(count)` concatenation
5. Returns `True`—`isinstance()` checks type (note: `42.0` is [float](floats.md), not int)

!!! warning "int() Truncates, Not Rounds"

    `int()` always truncates toward zero—different from `round()` or floor division:

    ```python
    print(int(3.9))    # 3 (truncated)
    print(round(3.9))  # 4 (rounded)
    print(int(-3.9))   # -3 (truncated toward zero)
    print(-3.9 // 1)   # -4.0 (floor division toward negative infinity)
    ```

## Practice Problems

??? question "Practice Problem 1: Division Types"

    What's the difference between `17 / 5`, `17 // 5`, and `17 % 5`?

    ??? tip "Answer"

        ```python
        print(17 / 5)   # 3.4 - true division (float)
        print(17 // 5)  # 3 - floor division (rounds down)
        print(17 % 5)   # 2 - modulo (remainder)
        ```

        - `/` gives the exact quotient as a float
        - `//` gives the quotient rounded down to an integer
        - `%` gives the remainder after division

??? question "Practice Problem 2: Modulo for Even/Odd"

    Write code to determine if a number stored in variable `n` is even or odd using the modulo operator.

    ??? tip "Answer"

        ```python
        n = 42
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
        ```

        Any even number divided by 2 has remainder 0. Odd numbers have remainder 1.

??? question "Practice Problem 3: Number Bases"

    What decimal number do these represent: `0b1010`, `0o12`, `0xA`?

    ??? tip "Answer"

        All three represent the decimal number `10`:

        ```python
        print(0b1010)  # 10 (binary: 1×8 + 0×4 + 1×2 + 0×1)
        print(0o12)    # 10 (octal: 1×8 + 2×1)
        print(0xA)     # 10 (hex: A = 10)
        ```

        Python automatically converts all number literals to decimal for display.

??? question "Practice Problem 4: Floor Division Trap"

    What does `print(-17 // 5)` output, and why might it be surprising?

    ??? tip "Answer"

        It outputs `-4`, not `-3`.

        ```python
        print(-17 / 5)   # -3.4
        print(-17 // 5)  # -4 (rounds DOWN toward negative infinity)
        print(int(-17 / 5))  # -3 (truncates toward zero)
        ```

        Floor division (`//`) always rounds toward negative infinity, so -3.4 rounds down to -4. This differs from truncation toward zero, which would give -3.

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

## Further Reading

- [**Python Integer Documentation**](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) - Official reference for integer operations
- [**PEP 237 – Unifying Long Integers and Integers**](https://peps.python.org/pep-0237/) - How Python removed integer overflow
- [**Bitwise Operations**](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types) - Advanced integer operations for low-level programming
- [**Python's Data Model**](https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy) - Deep dive into how integers work internally
- [**Computational Thinking**](https://cs.bradpenney.io/fundamentals/computational_thinking/) - Problem-solving patterns using discrete mathematics
- [**What is Computer Science?**](https://cs.bradpenney.io/fundamentals/what_is_computer_science/) - Understanding how computers process discrete values

---

Integers are the foundation of computational logic. From counting loop iterations to indexing arrays, from checking divisibility to converting between number systems, integers power the discrete mathematics that computers excel at.

Python's integer implementation removes the complexity found in other languages—no overflow errors, no separate "long" types, automatic precision scaling. This lets you focus on solving problems rather than managing numeric representation.

Master integers, and you master the building blocks of algorithmic thinking.
