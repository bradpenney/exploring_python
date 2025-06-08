# Integers

Integers, data type `int`, are interpreted as numbers, enabling you to perform standard
mathematical operations efficiently. Integers represent whole numbers, crucial for various
mathematical and computational tasks.

Declaring integers in Python is a breeze, following the same straightforward syntax used for all
variables. You assign a value to a variable name using the assignment operator (`=`). For instance,
you can declare integers like this:

``` python {title="Declaring Integer Variables" linenums="1"}
rank = 10
eggs = 12
people = 3
```

??? tip

    Exercise caution when combining an `int` with a `string`. To ensure correct output, you must
    *cast* the `int` as a `string` within the context of the `print()` statement. For example,
    when working with the variable `my_age = 12`, a standard concatenated print statement would
    need to *cast* the variable like this: `print("My age is " + str(my_age))`. This casting
    operation ensures that the `int` value of `my_age` is correctly interpreted as part of the
    `string`. Python can also handle this automatically through the use of "F-strings".

The primary use of an `int` in Python is mathematical operations. Whether you’re calculating the
area of geometric shapes, managing quantities, or working on numerical algorithms, using an `int`
is almost always necessary. You can efficiently perform arithmetic operations like addition,
subtraction, multiplication, division, and even exponentiation. Here is a basic example:

``` python {title="Python Math" linenums="1"}
length = 10
width = 5
height = 3
base = 10
side = 6
rectangle_area = length * width # a value of 30 would now be assigned to the variable area
triangle_area = (0.5 * base * height) # one half base multiplied by height
square_area = side**2 # exponents
print("The area of a the rectangle is " + str(rectangle_area))
print(f"The area of the triangle is {triangle_area}") # using F-strings
print(f"The area of the square is {square_area}")
```

Results in:

``` bash
The area of a the rectangle is 50
The area of the triangle is 15.0
The area of the square is 36
```

??? tip "See Also"

    Sometimes, the output of two integers results in a floating point number (a number with
    decimal points).  Python handles these as a `float`.  See [floats](floats.md) for more
    details.
