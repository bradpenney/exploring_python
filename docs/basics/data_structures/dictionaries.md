# Dictionaries

Dictionaries are one of the most important data structures in Python — and they're *everywhere*. 📖
Even when you don't see them directly, they're often working behind the scenes, quietly holding
things together.

For instance, while a string like `"hello"` isn’t itself a dictionary, many
Python objects (including strings) use internal dictionaries to store
attributes and metadata. And when you assign `a = "my_name"`, you're creating
a name (`a`) that points to a string object — which, like most Python objects,
has a dictionary of attributes under the hood.

The real magic of dictionaries is **association**. Linking keys to values
(`key: value`) creates fast and flexible lookups. Want to find a user’s email
by their username? Dictionary. Want to count how many times something appears?
Dictionary.

If you’ve used other programming languages, you might have heard these referred
to as *associative arrays*, *hash maps*, or just *maps*. It’s the same core
idea: match a key to a value. Think of it like an old-school phone book — you
know the name, and the dictionary gives you the number.

Dictionaries are a much less compute-intensive way to associate two values than say, keeping those
values in two lists (where the order is guaranteed). In fact, the lookup speed of a dictionary is
not affected by its size! ⚡ That's some serious performance.

??? tip

    Every key in a dictionary must be *unique* and *hashable*.  In practical
    terms, this means you can't use a *mutable* object as keys - so you can't
    use a `list` or a `dict` as as a key in a dictionary. This will throw a
    `TypeError` exception. Mutable objects **can** be assigned as values.
    For example, trying to assign the list `engine_parts` with
    `dream_car['engine_parts'] = 563`throws an error:

        Traceback (most recent call last):
        File "/home/brad/Documents/exploring_python/basics/data_structures/dictionaries.py", line 17, in <module>
            dream_car[engine_parts] = 563
            ~~~~~~~~~~^^^^^^^^^^^^^^
        TypeError: unhashable type: 'list'

The data type of a dictionary in Python is `dict`, and they're iterable, even
though they're not a sequence type like a [`list`](lists.md) or `set`. In lists,
you can insert a value at a specific index position in the sequence. With
dictionaries, position is determined by *insertion order*—new items are always
appended to the end. When iterating over a dictionary (see below), iteration
will always happen in insertion order. This isn't an index, but the natural
order of dictionaries.

??? info

    Prior to Python `v3.6`, there was no guaranteed order of dictionaries at all.
    As of `v3.6`, this changed, and dictionaries are guaranteed to iterate over
    the insertion order.

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

To retrieve a value, use square brackets `[]` and supply a key (not an index
like a list):

``` python
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']}")
```

Would return:

``` text
Dream car: 1971 Ford Pinto
```

## Inserting or Changing a Value

You can insert or update a key/value pair using the same square bracket syntax
with an assignment:

```python {title="Inserting and Updating Key/Value Pairs" linenums="1"}
dream_car['make'] = "Ferrari"
dream_car['model'] = "365 GTS/4 Daytona"
dream_car['colour'] = "Rosso Chiaro"
print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']} of the colour {dream_car['colour']}.")
```

This would output:

``` text
Dream car: 1971 Ferrari 365 GTS/4 Daytona of the colour Rosso Chiaro.
```

## Deleting a Key/Value Pair

Removing an entry is as easy as using the `del` keyword:

``` python {title="Deleting a Key/Value Pair" linenums="1"}
del dream_car['colour']
```

## Avoiding `KeyError` with `get()`

Attempting to read or delete a key that doesn’t exist will raise a `KeyError`
exception. For example, attempting to retrieve `dream_car['engine']` would
result in:

``` text
Traceback (most recent call last):
File "exploring_python/basics/data_structures/dictionaries.py", line 19, in <module>
    dream_car['engine']
    ~~~~~~~~~^^^^^^^^^^
KeyError: 'engine'
```

The `dict.get()` method tries to find a key in a dictionary and will not raise
an error if that key doesn't exist. Even better, you can assign a default value
to return if the key is missing (the default is `None`). So, if you search for
a key and it isn't present, the default value will be returned:

``` python {title="Creating a Dictionary" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

print(dream_car.get('engine', 'V8'))
```

Returns:

``` text
V8
```

???+ tip

    Note that the key/value pair `engine: V8` isn't inserted into the
    dictionary. Instead, this one-time value is returned to avoid throwing
    a `KeyError`.

## Clearing a Dictionary

If the data in a dictionary is no longer valuable, but you'd like to keep
the same dictionary object, use the `clear()` method to empty a dictionary
without changing the id.

``` python {title="Clear a Dictionary but Keep the Object" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400
}

print(f"Dream Car Object ID: {id(dream_car)}")
dream_car.clear()
print(f"Dream Car after clear: {dream_car}")
print(f"Dream Car Object ID after clear: {id(dream_car)}")
```

Results in:

``` text
Dream Car Object ID: 140457216790016
Dream Car after clear: {}
Dream Car Object ID after clear: 140457216790016
```

## Merging Dictionaries

Dictionaries often store related data, so merging them is a common task.
To do this, use the `update()` method. When you call `update()`, the
dictionary you pass in will **merge** with the original dictionary:
it will **update** any values with the **same key** and **add** any
key/value pairs that did not exist in the original dictionary.

``` python {title="Merging Dictionaries" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400
}

dream_car_engine = {
    "engine": "V8",
    "horsepower": 440,
    "cylinders": 8
}

dream_car.update(dream_car_engine) # (1)
print(f"Dream Car: {dream_car}")
print(f"Dream Car Engine: {dream_car_engine}")
```

1. The `update()` method is also available, with similar functionality, in
   [`sets`](sets.md#adding-elements)

Would output:

``` text
Dream Car: {'model': 'Pinto', 'make': 'Ford', 'year': 1971, 'mileage': 400, 'engine': 'V8', 'horsepower': 440, 'cylinders': 8}
Dream Car Engine: {'engine': 'V8', 'horsepower': 440, 'cylinders': 8}
```

Note how `dream_car_engine` was not modified by the `update()` function,
only `dream_car`.
