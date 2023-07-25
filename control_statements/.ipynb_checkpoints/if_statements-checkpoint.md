
# `if` Statements


Ubiquitous in nearly all programming languages, the `if` statement is the foundational way programs make decsions.  A condition is evaluated, and then a particular action is taken depending on the outcome of the evaluation.  A Python `if` statement will look like this:

```python
name = "Michael"

if name == "Michael": # the name variable is "Michael"
    print(f"Hello {name}!")
```

## `if/else` Statements

It is most common that if a condition is not met, a different action will be taken.  This paradigm is known as a `if/else` statement.  In Python, these look like this:

```python
name = "Jim"

if name == "Michael":  # the name variable is "Michael"
    print(f"Hello {name}!")
else:  # the name variable is anything other than "Michael"
    print(f"Hey there {name}!")
```

## `if/elif/else` Statements

Often there are more than two possible outcomes that can be evaluated and different actions can be taken depending on the results of the evaluation.  In Python, we use `if/elif/else` statements:

```python
name = "Dwight"

if name == "Michael":  # the name variable is "Michael"
    print(f"Hello {name}!")
elif name == "Jim": # the name variable is "Jim"
    print(f"Hey there {name}!")
else:  # the name variable is anything other than "Michael" or "Jim"
    print(f"Greetings {name}!")
```
