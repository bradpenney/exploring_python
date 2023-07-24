
# Integers

In Python (as most programming languages), numbers are treated differently than [`strings`](./strings.md).  They are interpreted as numbers, therefore standard mathematical operations can be performed on them.  Integers are whole numbers (as opposed to [`floats`](./floats.md)).  Any two integers can be declared and then used mathematically. 



```{note}
Be careful of division in Python - the quotient of two `ints` could result in a `float` if the numbers cannot be divided evenly.
```

Declaring `ints`, as all other variables in Python, is simple syntax:

.. code-block:: python

    # Declaring basic integer values   
    rank = 10
    eggs = 12
    people = 3

.. warning::
    When using an :p:`int` in combination with :ref:`strings`, it is important to *cast* the :p:`int` as a :p:`string` in order for it to print out correct.  For example, :p:`print("My age is " + str(myAge))` casts the :p:`int` :p:`myAge` as a string within the context of the :p:`print` statement.

+++

The most common usage of :p:`ints` is in for mathematical operations, such as:

.. code-block:: python

    length = 10
    width = 5
    height = 3
    base = 10
    side = 6
    rectangleArea = length * width # the value of 30 would now be assigned to the variable area
    triangleArea = (0.5 * base * height) # one half base multipled by height
    squareArea = side**2 # exponents
    print("The area of a the rectangle is " + str(rectangleArea))
    print("The area of the triangle is " + str(triangleArea))
    print("The area of the square is " + str(squareArea))

Which would result in:

.. code-block::

    The area of a the rectangle is 50
    The area of the triangle is 15.0
    The area of the square is 36
