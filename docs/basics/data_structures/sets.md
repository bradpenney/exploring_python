# Sets

In Python, a Sets are a unique data type inspired by mathematical sets.  They are a collection of
elements, like a [`list`](./lists.md) or [`dict`](dictionaries.md), but there is
**no ordering** of the elements, and there can be **no duplicate** elements. With that in mind,
it should be clear that the main use of a `set` is to have unique set of values, ideal when
dealing with data prone to duplication, and then [testing membership](membership_testing.md)
against that `set`.

Like mathematical sets, Python sets support operations such as *union*, *insertion*, *difference*,
and *containment*.

??? tip "Rusty on mathematical sets?  Check out these videos!"

    **General Set Theory**

    <iframe width="70%" height="315" src="https://www.youtube.com/embed/tyDKR4FG3Yw?si=gxYhPLoa6eTw7u02"
    frameborder="0" allowfullscreen></iframe>

    **Union & Intersection of Sets**

    <iframe width="70%" height="315" width="100" src="https://www.youtube.com/embed/xZELQc11ACY?si=_UQYsw0bYjuMiirn"
    frameborder="0" allowfullscreen></iframe>

    **Difference of Sets**

    <iframe width="70%" height="315" src="https://www.youtube.com/embed/HJduHa16Y70?si=WoTyRr4O0RBsSoOL"
    frameborder="0" allowfullscreen></iframe>

    **Set Theory: Containment**

    <iframe width="70%" height="315" src="https://www.youtube.com/embed/wTHojsEmuNU?si=IjocB0fb-sde4W--"
    frameborder="0" allowfullscreen></iframe>

Some programmers think of sets in Python as *keyless [dictionaries](./dictionaries.md)* because
a set must contain unique values, the order is not (yet) guaranteed, the elements are iterable,
and they must be *hashable*.

??? info ""Hashable?"

    A *hashable* object has a consistent hash value throughout its lifetime, and it can be
    compared for equality with other objects.

    A hash value, also known as a message digest or fingerprint, is a unique, fixed-length
    string produced by a hash function based on an input data.

Sets are mutable objects in Python, similar to a[`list`](lists.md), which, somewhat ironcially,
makes sets *non-hashable* (see note above) and therefore a `set` cannot be an element of a
`set`. 😕

??? Frozenset

    Check out the Python Standard Library type
    [FrozenSet](https://docs.python.org/3/library/stdtypes.html#frozenset) if you do require
    nested sets.

## Creating Sets

In Python, a set is declared with curly braces (hence one of the comparison to keyless
dictionaries):

``` python {title="Creating Sets" linenums="1"}
colours = {"red","green","blue", "orange", "red", "blue", "red"}
chess_pieces = set(["king","queen","knight","knight", "bishop","bishop",
                    "rook", "rook", "pawn", "pawn", "pawn", "pawn", "pawn",
                    "pawn", "pawn", "pawn"])
print(f"Colours: {colours}")
print(f"Object type of colours variable: {type(colours)}")
print(f"Chess Pieces: {chess_pieces}")
print(f"Object type of chess_pieces variable: {type(chess_pieces)}")
```

Outputs:

``` text
Colours: {'green', 'blue', 'red', 'orange'}
Object type of colours variable: <class 'set'>
Chess Pieces: {'pawn', 'knight', 'rook', 'king', 'queen', 'bishop'}
Object type of chess_pieces variable: <class 'set'>
```

Notice how even though duplicate values were passed in, all the elements of the `set` are unique
and duplicates are ignored.

??? tip

    To create an empty `set`, use `variable = set()`, as `variable = {}` would create an empty
    `dict` object.

Sets can use most of the familiar control structures in Python iterables such as
[`for` loops](../control_structures/for_loops.md) and [membership testing](./membership_testing.md).
Other familiar functions for sequences also work such as `set.clear()`, `set.copy()`, `len(set)`,
and so on.

## Set-Specific Functionality

Because of their mathematical underpinnings, sets have functionality that other iterables do not.

### Adding/Removing/Discarding Elements

Unlike other iterables, there is no `append()` or `insert()` methods for sets as the order is not
guaranteed.  Instead, sets use `add()`, `remove()`, and `discard(). Note that adding the duplicate
elements to a `set` will be ignored as the unique element already exists.

??? tip "Remove with Caution!"

    Trying to use the `set.remove()` method on an element that doesn't exist in the `set` will
    result in a `KeyError` exception.

### Disjointed

If two sets do not have any elements in common, it is *disjoint*, meaning their *intersection*
is empty. In Python, this can be a useful operation to ensure there is no duplication between two
sets of data.

``` python {title="Testing Disjoint Sets" linenums="1"}
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))
```

Returns:

``` text
True
```
