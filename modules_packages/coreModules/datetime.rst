.. role:: p(code)
   :language: python

:p:`datetime` Module
====================

The :p:`datetime` module supplies classes for manipulating dates and times.  The official documentation can be found `here <https://docs.python.org/3/library/datetime.html>`_.  As with all other core modules, to get started add the standard import line to the top of the program:

.. code-block:: python

   import datetime

Key Functions
-------------

:p:`date()`
~~~~~~~~~~~

Using the :p:`datetime.date()` function, Python creates a :p:`datetime` object that is a date on the Gregorian calendar.  It is used as follows:

.. code-block:: python

   britishNorthAmericaAct = datetime.date(1871, 7, 1)

   print(f"The British North America Act made Canada an independent country on {britishNorthAmericaAct}")

.. TODO: add time(), datetime() and today()

Resources
---------

.. figure:: https://img.youtube.com/vi/RjMbCUpvIgw/maxresdefault.jpg
    :width: 500
    :alt: Socratica - DateTime Module
    :target: https://youtu.be/RjMbCUpvIgw

    Socratica - DateTime Module
