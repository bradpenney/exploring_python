# Dictionaries

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

    Every key in a dictionary must be unique and _hashable_.  In practical terms, this means you
    can't use a mutable object as keys - so you can't use a `list` as a key in a dictionary.  It
    is ok to use a `list` as a value.
