
# `logging` Module

[Offical Documentation for the Logging Module](https://docs.python.org/3/library/logging.html?highlight=logging#module-logging)

The `logging` module is one of the most valuable core modules built into the Python programming language.  Like other Python core modules, to use it, simply add this line to the top of your program:

```{code-cell} ipython3
import logging
```

## Levels of Logging

There are five levels of logging available by default using the `logging` module.  In order of severity, these are:

#. **Debug** - called with :p:`logging.debug("Debugging message")`
#. **Info** - called with :p:`logging.info("Informational message")` 
#. **Warning** - called with :p:`logging.warning("Warning message")`
#. **Error** - called with :p:`logging.error("Error message")`
#. **Critical** - called with :p:`logging.critical("Critical message")`

### Basic Usage

After importing the module, it will require some basic setup.  The most basic setup would be:

```{code-cell} ipython3
logging.basicConfig(level=logging.ERROR, filename="errors.log", filemode="a")
```

It is also possible to designate the format of the log string as follows:

```{code-cell} ipython3
logging.basicConfig(
    level=logging.ERROR, 
    filename="errors.log", 
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

The attributes that can be formatted and called in a LogRecord can be found [here](https://docs.python.org/3/library/logging.html#logrecord-attributes).

### Embedding Variables in Logs

It is very easy to write a custom string to a log using the `logging` module.  Using a standard `fstring`, the value is written to the log.  For example (continuing from the above examples):

```{code-cell} ipython3
myName = "Brad"
logging.error(f"Oh noes!  {myName} created an error!")
```

### Embedding Tracebacks in Logs

In Python, specific errors can be caught using a `try/except` block.  The `logging` module has a special function built in to append caught errors to the log.  For example:

```{code-cell} ipython3
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("ZeroDivisionError")
```

### Resources


[![Tech with Tim - Python Logging](https://img.youtube.com/vi/urrfJgHwIJA/maxresdefault.jpg)](https://youtu.be/urrfJgHwIJA)


[![Socratica - Logging Module](https://img.youtube.com/vi/g8nQ90Hk328/maxresdefault.jpg)](https://youtu.be/g8nQ90Hk328)
