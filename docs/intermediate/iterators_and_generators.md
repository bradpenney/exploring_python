# Iterators and Generators

Iterators and generators are important memory-saving tools in Python. They
allow you to work with sequences of data (of any size) without loading
everything into memory at once. Instead, each member of the iterable is
processed individually. This is especially useful when dealing with large
datasets or streams of data.

## What is an Iterable?

An iterable is any Python object that can return its members one at a time,
allowing it to be iterated over using a loop (see
[For Loops](../basics/control_structures/for_loops.md) and
[While Loops](../basics/control_structures/while_loops.md)). The order in
which iterables are iterated over depends on their type. For example:

- **Sequentially**: [Lists](../basics/data_structures/lists.md),
    [Tuples](../basics/data_structures/tuples.md), and
    [Strings](../basics/data_types/strings.md).
- **Insertion Order**: [Dictionaries](../basics/data_structures/dictionaries.md).
- **Unordered**: [Sets](../basics/data_structures/sets.md).

??? tip

    Not everything in Python is iterable. For example,
    [integers](../basics/data_types/ints.md) and
    [floats](../basics/data_types/floats.md) are not iterable. If you try to
    iterate over them, you'll get a `TypeError` exception.

You can check if an object is iterable by using the `isinstance()` function
with the `collections.abc.Iterable` class.

``` python {title="Checking if Iterable" linenums="1"}
from collections.abc import Iterable
def is_iterable(obj):
    return isinstance(obj, Iterable)

print(is_iterable([1, 2, 3]))
print(is_iterable("Hello"))
print(is_iterable(42)) # (1)
```

1. Integers are not iterable, so this will return `False`.

Would return:

``` text
True
True
False
```

## What is an Iterator?

An iterator is any object that implements the iterator protocol, which consists
of two methods:

- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next value from the iterator. If there are no more
    items, it raises a `StopIteration` exception.
