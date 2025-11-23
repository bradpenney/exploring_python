# Floats

While integers (whole numbers) are well-suited for many tasks, there are situations where precision
beyond whole numbers is required. Enter the `float`. 🎯 A `float`, short for "floating-point number," is a numeric data
type in Python that represents real numbers, including those with decimal points. Unlike integers
(represented in Python as an [`int`](ints.md)), which deal only with whole numbers, a `float` can
handle values that have fractional components. For example, the mathematical constant `pi`, often
approximated as 3.14, is a classic example of a `float` in Python. Consider the following examples:

``` python {title="Floating Point Numbers" linenums="1"}
pi = 3.14
price = 10.99
temperature = 21.05
```

Floats are essential because they enable you to work with a wide range of data, especially in
scientific, engineering, and financial applications. Whether dealing with temperature measurements,
currency values, or mathematical constants, floats provide the flexibility to handle real-world
data with fractional components.

!!! warning "Precision Alert"

    Floats are *approximations*, not exact values. This is crucial to understand before you go
    any further. See [The Precision Problem](#the-precision-problem-why-01--02--03) below — it
    will save you hours of debugging headaches.

## When to Use Floats

It’s important to note that a `float` offers precision, but come at a cost — they occupy more
memory (RAM) than integers. Therefore, it’s advisable to use floats only when necessary. If
your calculations involve whole numbers, it’s more efficient to use integers. However, modern
computers typically have ample RAM, making the memory overhead of floats less of a concern than
in the past.

``` python {title="Sample Use Cases for Floats" linenums="1"}
temperature = 21.05  # A float for temperature
number_of_items = 5  # An integer for quantity
```

## Use Cases for Floats

Floats find their applications in a wide array of scenarios. Here are a few everyday use cases
where floats shine:

- **Financial Calculations**: Floats are ideal for handling financial data, such as calculating
  interest rates, stock prices, or the exact cost of that fancy espresso machine you've been eyeing. ☕
- **Scientific Research**: Scientists use floats to represent experimental data, physical
  measurements, and mathematical constants like pi, e, or the gravitational constant.
- **Engineering**: Engineers use floats for precise calculations in structural analysis,
  fluid dynamics, and electrical circuit design.
- **Geospatial Data**: When working with geographic coordinates or GPS data, floats are essential
  for accurately representing latitude and longitude.
- **Temperature and Weather**: Floats store temperature values, making them suitable for weather forecasting and climate modelling.

## Using Floats

In Python, performing arithmetic operations with floats is straightforward. If any mathematical
operation involves a float, the result will also be a float. For example, multiplying an integer
by a float yields a float result:

``` python {title="Arithmetic with Floats" linenums="1"}
number_of_items = 5       # Integer
price = 10.99             # Float
total_price = number_of_items * price  # Result is a float
print(total_price)
```

Results in:

``` text
54.95
```

## The Precision Problem: Why 0.1 + 0.2 ≠ 0.3

Here's the moment that breaks every new programmer's brain. Try this in Python:

``` python {title="The Classic Gotcha" linenums="1"}
result = 0.1 + 0.2
print(result)
print(result == 0.3)
```

Returns:

``` text
0.30000000000000004
False
```

Wait, what? 🤯

This isn't a Python bug — it's how *all* computers store decimal numbers. Floats are stored in
binary (base-2), and just like 1/3 can't be exactly represented in decimal (0.333...), many
simple decimals can't be exactly represented in binary. The number 0.1 in binary is actually
an infinitely repeating fraction, so the computer stores the closest approximation it can fit.

### Why This Matters

This isn't just a curiosity — it can cause real bugs:

``` python {title="A Bug Waiting to Happen" linenums="1"}
# Imagine this is checking if a bank balance is zero
balance = 0.1 + 0.1 + 0.1 - 0.3

if balance == 0:
    print("Account empty")
else:
    print(f"Balance remaining: {balance}")  # This runs!
```

Returns:

``` text
Balance remaining: 5.551115123125783e-17
```

Your "zero" balance is actually 0.00000000000000005551... Not exactly what you'd want in a
banking application. 💸

### How to Handle Float Comparisons

**Option 1: Use `round()` for display and simple comparisons**

``` python {title="Using round()" linenums="1"}
result = 0.1 + 0.2
print(round(result, 2))  # 0.3
print(round(result, 2) == 0.3)  # True
```

**Option 2: Use `math.isclose()` for robust comparisons**

``` python {title="Using math.isclose()" linenums="1"}
import math

result = 0.1 + 0.2
print(math.isclose(result, 0.3))  # True

# You can adjust the tolerance if needed
print(math.isclose(result, 0.3, rel_tol=1e-9))  # True
```

**Option 3: Use `Decimal` for financial calculations**

When precision actually matters (money, scientific measurements), use the `decimal` module:

``` python {title="Using Decimal for Exact Math" linenums="1"}
from decimal import Decimal

# Create Decimals from strings, not floats!
price = Decimal("19.99")
tax_rate = Decimal("0.15")
total = price * (1 + tax_rate)
print(total)  # 22.9885 — exact!
```

!!! tip "Rule of Thumb"

    - **Display to users**: Use `round()`
    - **Comparing floats**: Use `math.isclose()`
    - **Financial/precise calculations**: Use `Decimal`
    - **Scientific computing**: Use NumPy (it handles precision more gracefully)

## Scientific Notation

For very large or very small numbers, Python supports scientific notation using `e`:

``` python {title="Scientific Notation" linenums="1"}
speed_of_light = 3e8       # 300,000,000 meters per second
planck_constant = 6.626e-34  # A very small number

print(speed_of_light)      # 300000000.0
print(planck_constant)     # 6.626e-34
```

The `e` means "times 10 to the power of" — so `3e8` is 3 × 10⁸. This is much easier to read
(and type) than `300000000.0`. Your fingers will thank you. ⌨️

## Useful Float Functions

Python provides several built-in functions for working with floats:

``` python {title="Handy Float Functions" linenums="1"}
import math

# Rounding
print(round(3.14159, 2))    # 3.14 — round to 2 decimal places
print(round(2.5))           # 2 — Python uses "banker's rounding" (to nearest even)
print(round(3.5))           # 4

# Absolute value
print(abs(-42.5))           # 42.5

# Floor and ceiling
print(math.floor(3.7))      # 3 — round down
print(math.ceil(3.2))       # 4 — round up

# Truncate (remove decimal part)
print(math.trunc(3.9))      # 3
print(math.trunc(-3.9))     # -3 (toward zero, not down)
```

??? note "Banker's Rounding"

    Python's `round()` uses "round half to even" (banker's rounding). This means 2.5 rounds to 2,
    but 3.5 rounds to 4. This reduces bias when rounding lots of numbers. If you need traditional
    "round half up" behavior, you'll need to implement it yourself or use `Decimal`.

## Converting To and From Floats

``` python {title="Type Conversion" linenums="1"}
# String to float
price = float("19.99")
print(price)  # 19.99

# Integer to float
whole_number = float(42)
print(whole_number)  # 42.0

# Float to integer (truncates!)
print(int(3.9))   # 3 — decimal part is discarded
print(int(-3.9))  # -3

# Check if something is a float
print(isinstance(3.14, float))  # True
print(isinstance(3, float))     # False
```

!!! warning "String Conversion"

    `float()` will raise a `ValueError` if the string isn't a valid number:

    ```python
    float("hello")  # ValueError: could not convert string to float: 'hello'
    ```

## Special Float Values

Python floats can represent some special mathematical concepts:

``` python {title="Special Values" linenums="1"}
import math

# Infinity
positive_inf = float('inf')
negative_inf = float('-inf')
print(positive_inf > 1000000000)  # True — infinity is bigger than any number
print(1 / positive_inf)           # 0.0

# Not a Number (NaN)
not_a_number = float('nan')
print(not_a_number == not_a_number)  # False! NaN is not equal to anything, even itself
print(math.isnan(not_a_number))      # True — use this to check for NaN
```

These come up when doing math that would otherwise cause errors, like dividing by zero in
some contexts or taking the square root of a negative number.

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Precision** | Floats are approximations — `0.1 + 0.2 != 0.3` |
| **Comparisons** | Use `math.isclose()`, not `==` |
| **Money** | Use `Decimal`, not `float` |
| **Scientific notation** | `3e8` = 3 × 10⁸ |
| **Rounding** | Python uses banker's rounding (round half to even) |
| **Special values** | `float('inf')`, `float('-inf')`, `float('nan')` exist |
