# Sets

In Python, Sets are a unique data type inspired by mathematical sets. 🎲 They are a collection of
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

## Managing Set Elements

Because of their mathematical underpinnings, sets have functionality that other iterables do not.

### Adding Elements

Unlike other iterables, there is no `append()` or `insert()` methods for sets as the order is not
guaranteed.  Instead, sets use `add()`, and `update()`:

``` python {title="Adding Elements to Sets" linenums="1"}
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.add(4)
print(f"Set 1 after adding 4: {s1}")
s1.update(s2) # (1)
print(f"Set 1 after adding Set 2: {s1}")
```

1. Adding two sets is referred to as the *union* of sets.  In this case, the union of `s1`
and `s2` is assigned to `s1`.  See
[Merging Dictionaries](../data_structures/dictionaries.md#merging-dictionaries) for usage of
`update()` method.

Would output:

``` text
Set 1 after adding 4: {1, 2, 3, 4}
Set 1 after adding Set 2: {1, 2, 3, 4, 5}
```

It is important to understand that adding the duplicate elements to a `set` will be ignored
as the unique element already exists.

### Removing Elements

Python offers two methods to remove elements from a set, `remove()`, and `discard()`.

``` python {title="Discarding Elements" linenums="1"}
manager_nodes = {"host1", "host7", "host12"}
print(f"Manager Nodes: {manager_nodes}")
manager_nodes.discard("host7")
manager_nodes.discard("host13")  # (1)
print(f"Manager Nodes after discarding: {manager_nodes}")
```

1. This will not raise an error if "host13" is not present.  See tip below.

Would output:

``` text
Manager Nodes: {'host1', 'host7', 'host12'}
Manager Nodes after discarding: {'host1', 'host12'}
```

??? tip "Remove with Caution!"

    Trying to use the `set.remove()` method on an element that doesn't exist in the `set` will
    result in a `KeyError` exception.  This may be useful in some situations, it is good to be
    aware of both options.

## Comparing Sets

### Subsets and Supersets

It is possible to compare sets, returning a [`boolean`](../data_types/booleans.md) value. When
all the elements of one set are contained in a second set, the first set is called a *subset*
of the second, and the second is called a *superset* of the first. Testing for subsets and
supersets is common. Below is a table showing comparison operators for raw sets:


| Statement          | True/False? | Explanation                                    |
|:------------------:|:-----------:|:----------------------------------------------:|
| `{2,3} < {2,3,4}`  | ✅          | The first set is a subset of the second.       |
| `{2,3} < {2,3}`    | ❌          | The first set is not greater than the second.  |
| `{2,3} <= {2,3,4}` | ✅          | The second set is a superset of the first.     |
| `{2,3} >= {2,3,4}` | ❌          | The first set is not a superset of the second. |

Rather than having to depend on comparison operators, Python includes useful methods which evaluate
set relationships - `issubset()` and `issuperset()`:

``` python {title="Testing Subsets and Supersets" linenums="1"}
manager_nodes = {"host1", "host7", "host12"}
cluster_nodes = {"host1", "host2", "host3", "host4", "host5", "host6", \
                 "host7", "host8", "host9", "host10", "host11", "host12"}
print(f"Manager Nodes: {manager_nodes}")
print(f"Cluster Nodes: {cluster_nodes}")
print(f"Manager Nodes are present in Cluster Nodes: {manager_nodes.issubset(cluster_nodes)}")
print(f"Cluster Nodes contain all Manager Nodes: {cluster_nodes.issuperset(manager_nodes)}")
```

Yields:

``` text
Manager Nodes: {'host7', 'host1', 'host12'}
Cluster Nodes: {'host3', 'host12', 'host5', 'host1', 'host2', 'host10', 'host7', 'host6', 'host8', 'host4', 'host9', 'host11'}
Manager Nodes are present in Cluster Nodes: True
Cluster Nodes contain all Manager Nodes: True
```

### Unions and Intersections

The *union* of two sets is all the elements of both sets. The *intersection* of two sets is only
the elements that appear in both sets. It is possible to use logical operators to perform unions
and intersections (union is `set1 | set2`, while intersection is `set1 & set2`), but Python
provides useful methods for these operations. Below is a (somewhat contrived) example:

``` python {title="Set Unions and Intersections" linenums="1"}
mechanic_tools = {"wrench", "screwdriver", "hammer", "pliers", "jack"}
carpenter_tools = {"saw", "hammer", "chisel", "screwdriver", "level"}
print(f"Intersection: {mechanic_tools.intersection(carpenter_tools)}") # (1)
print(f"Union: {mechanic_tools.union(carpenter_tools)}")
```

1. Maybe mechanics and carpenters can get along after all! 😄

Returns:

``` text
Intersection: {'screwdriver', 'hammer'}
Union: {'saw', 'level', 'screwdriver', 'chisel', 'jack', 'hammer', 'pliers', 'wrench'}
```

### Difference of Sets

The difference of sets is all the elements in one set that do not exist in another. This can be
calculated using arithmetic operators - `set1 - set2` would yield all the elements in `set1` that
are not in `set2`.  Python also offers handy methods which are more explicit than the arithmetic
operators (for most programmers).  To continue our contrive example from above:

``` python {title="Difference of Sets" linenums="1"}
mechanic_tools = {"wrench", "screwdriver", "hammer", "pliers", "jack"}
carpenter_tools = {"saw", "hammer", "chisel", "screwdriver", "level"}
print(f"Mechanic-only Tools: {mechanic_tools.difference(carpenter_tools)}")
print(f"Carpenter-only Tools: {carpenter_tools.difference(mechanic_tools)}")
```

Returns:

``` text
Mechanic-only Tools: {'jack', 'pliers', 'wrench'}
Carpenter-only Tools: {'saw', 'level', 'chisel'
```

### Disjoint

If two sets do not have any elements in common, it is *disjoint*, meaning their *union*
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
