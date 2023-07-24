.. role:: p(code)
   :language: python

.. _functions:

Python Functions
================

A function is reusable block of code that performs a single task and can be used repeatedly in programs.  In Python, a basic function can be declared as follows:

.. code-block:: python

   def addNumbers(a:int, b:int) -> int:
      return a+b

The above example, the following items should be noted:

- The :p:`def` keyword declares the start of a function
- The name of this function is :p:`addNumbers`
- The function accepts two arguments, :p:`a` and :p:`b`.

   - Each argument can be labelled to show the expected data type (i.e. :p:`a:int` shows that the :p:`a` argument is expecting an :p:`int`).
   - The :p:`-> int` declares what the function will :p:`return` (see below).

- Similar to other Python constructs, the declaration line ends with a colon (:p:`:`).
- In standard circumstances, a Python function will :p:`return` a value

Functions are useful for repeated actions.  A famous principle of software development is "Don't Repeat Yourself" (aka DRY code).  As an example, writing the same message to multiple users could be performed as follows:

.. code-block:: python

   user1 = "Carl"
   user2 = "Jim"
   user3 = "Fred"

   print("Greetings " + user1 + ", welcome to this program.")
   print("Greetings " + user2 + ", welcome to this program.")
   print("Greetings " + user3 + ", welcome to this program.")

Clearly, the same lines are being repeated over and over.  This could be re-written as a function:

.. code-block:: python

   def greet(user:str) -> str:
      return "Greetings " + user + ", welcome to this program."

   user1 = "Carl"
   user2 = "Jim"
   user3 = "Fred"

   print(greet(user1))
   print(greet(user2))
   print(greet(user3))

Both of these examples will have the same output, but using the function will require less effort for the programmer and be much more robust and maintainable:

.. code-block:: python

   Greetings Carl, welcome to this program.
   Greetings Jim, welcome to this program.
   Greetings Fred, welcome to this program.