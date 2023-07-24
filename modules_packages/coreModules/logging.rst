.. role:: p(code)
   :language: python

:p:`logging` Module
====================

* `Offical Documentation for the Logging module <https://docs.python.org/3/library/logging.html?highlight=logging#module-logging>`_

The :p:`logging` module is one of the most valuable core modules built into the Python programming language.  Like other Python core modules, to use it, simply add this line to the top of your program:

.. code-block:: python

   import logging

Levels of Logging
~~~~~~~~~~~~~~~~~

There are five levels of logging available by default using the :p:`logging` module.  In order of severity, these are:

#. **Debug** - called with :p:`logging.debug("Debugging message")`
#. **Info** - called with :p:`logging.info("Informational message")` 
#. **Warning** - called with :p:`logging.warning("Warning message")`
#. **Error** - called with :p:`logging.error("Error message")`
#. **Critical** - called with :p:`logging.critical("Critical message")`

Basic Usage
~~~~~~~~~~~

After importing the module, it will require some basic setup.  The most basic setup would be:

.. code-block:: python

   logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a")

It is also possible to designate the format of the log string as follows:

.. code-block:: python

   logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a", 
                       format="%(asctime)s - %(levelname)s - %(message)s")

The attributes that can be formatted and called in a LogRecord can be found `here <https://docs.python.org/3/library/logging.html#logrecord-attributes>`_.

Embedding Variables in Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is very easy to write a custom string to a log using the :p:`logging` module.  Using a standard :p:`fstring`, the value is written to the log.  For example (continuing from the above examples):

.. code-block:: python

   myName = "Brad"
   logging.error(f"Oh noes!  {myName} created an error!")

Which would output:

.. code-block:: html

   2022-11-08 19:23:51,490 - ERROR - Oh noes!  Brad created an error!

Embedding Tracebacks in Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In Python, specific errors can be caught using a :p:`try/except` block.  The :p:`logging` module has a special function built in to append caught errors to the log.  For example:

.. code-block:: python

   try:
      1/0
   except ZeroDivisionError:
      logging.exception("ZeroDivisionError")

Which would print the following info to the log (assuming similar setup as earlier examples):

.. code-block:: html

   2022-11-14 10:00:05,348 - ERROR - ZeroDivisionError
   Traceback (most recent call last):
   File "/home/brad/Documents/test.py", line 9, in <module>
      1/0
   ZeroDivisionError: division by zero

Resources
~~~~~~~~~

.. figure:: https://img.youtube.com/vi/urrfJgHwIJA/maxresdefault.jpg
    :width: 500
    :alt: Tech with Tim - Python Logging
    :target: https://youtu.be/urrfJgHwIJA

    Tech with Tim - Python Logging

.. figure:: https://img.youtube.com/vi/g8nQ90Hk328/maxresdefault.jpg
    :width: 500
    :alt: Socratica - Logging Module
    :target: https://youtu.be/g8nQ90Hk328

    Socratica - Logging Module