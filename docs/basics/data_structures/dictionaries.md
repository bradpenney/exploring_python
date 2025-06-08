# Dictionaries

## Theory

Dictionaries are one of the most important data structures in Python — and they’re *everywhere*.
Even when you don’t see them directly, they’re often working behind the scenes, quietly holding
things together.

For instance, while a string like `"hello"` isn’t itself a dictionary, many Python objects
(including strings) use internal dictionaries to store attributes and metadata. And when you
assign `a = "my_name"`, you're creating a name (`a`) that points to a string object — which, like
most Python objects, has a dictionary of attributes under the hood.

The real magic of dictionaries is **association**. By linking keys to values (`key: value`), you
can create fast and flexible lookups — like a built-in search engine for your data. Want to find
a user’s email by their username? Dictionary. Want to count how many times something appears?
Dictionary.

If you’ve used other programming languages, you might have heard these referred to as
*associative arrays*, *hash maps*, or just *maps*. It’s the same core idea: match a key to a value.
Think of it like an old-school phone book — you know the name, and the dictionary gives you the
number.

Dictionaries are a much less compute-intensive way to associate two values than say, keeping those
values in two lists (where the order is guaranteed).  In fact, the lookup speed of a dictionary is
not affected by its size!

??? tip

    Every key in a dictionary must be *unique* and *hashable*.  In practical terms, this means you
    can't use a *mutable* object as keys - so you can't use a `list` or a `dict` as as a key in a
    dictionary. This will throw a `TypeError` exception. Mutable objects **can** be assigned as
    values.  For example, trying to assign the list `engine_parts` with
    `dream_car['engine_parts'] = 563`throws an error:

        Traceback (most recent call last):
        File "/home/brad/Documents/exploring_python/basics/data_structures/dictionaries.py", line 17, in <module>
            dream_car[engine_parts] = 563
            ~~~~~~~~~~^^^^^^^^^^^^^^
        TypeError: unhashable type: 'list'


The data type of a dictionary in Python is `dict`, and they're iterable, even though they're not
a sequence type like a `list` or `set`.  Instead, values are retrieved by *key*, not by index
value like a `list`.  Dictionaries do not have a guaranteed order.

## Creating a Dictionary

Dictionaries can be declared with:

``` python {title="Creating a Dictionary" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}
```

To retrieve a value, use square brackets `[]` and supply a key (not an index like a list):

``` python
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']}")
```

Would return:

``` bash
Dream car: 1971 Ford Pinto
```

## Inserting or Changing a Value

You can insert or update a key/value pair using the same square bracket syntax with an assignment:

```python {title="Inserting and Updating Key/Value Pairs" linenums="1"}
dream_car['make'] = "Ferrari"
dream_car['model'] = "365 GTS/4 Daytona"
dream_car['colour'] = "Rosso Chiaro"
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']} of the colour {dream_car['colour']}")
```
This would output:

``` bash
Dream car: 1971 Ferrari 365 GTS/4 Daytona of the colour Rosso Chiaro
```

## Deleting a Key/Value Pair

Removing an entry is as easy as using the `del` keyword:

``` python {title="Deleting a Key/Value Pair" linenums="1"}
del dream_car['colour']
```

??? warning

    Attempting to read or delete a key that doesn’t exist will raise a `KeyError` exception:

    ``` bash
    Traceback (most recent call last):
    File "exploring_python/basics/data_structures/dictionaries.py", line 19, in <module>
        {dream_car['model']} with the {dream_car['engine']} engine.")
                                       ~~~~~~~~~^^^^^^^^^^
    KeyError: 'engine'
    ```

    If you’re unsure whether a key exists, you can check with `'key' in dictionary` or use
    `.get()` instead.
