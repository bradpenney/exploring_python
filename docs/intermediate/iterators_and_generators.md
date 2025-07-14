# Iterators and Generators

Iterators and generators are important memory-saving tools in Python. They
make it possible to work with sequences of data (of any size) without loading
everything into memory at once. Instead, each member of the iterable is
processed individually, which is particularly useful when dealing with large
datasets or streams of data.

## What is an Iterable?

An iterable is any Python object that can return its members one at a time,
allowing it to be iterated over using a loop (see
[For Loops](../basics/control_structures/for_loops.md) and
[While Loops](../basics/control_structures/while_loops.md)). Common examples
of iterables include [lists](../basics/data_structures/lists.md),
[tuples](../basics/data_structures/tuples.md),
[strings](../basics/data_types/strings.md), and
[dictionaries](../basics/data_structures/dictionaries.md).

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

An iterator is an object that implements the iterator protocol, which consists
of two methods:

- `__iter__()`: Returns the iterator object itself.
- `__next__()`: Returns the next value from the iterator. If there are no more
    items, it raises a `StopIteration` exception.
