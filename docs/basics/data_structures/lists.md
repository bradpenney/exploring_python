# Lists

Lists are among Python's most valuable and frequently used data types, and they are the heart
of countless programs. 📋 So, what exactly is a `list`, and why are they so indispensable?

In essence, a `list` is a dynamic and mutable sequence of values. Think of it as a versatile
bag storing various items—numbers, words, and even a medley of data types—all within a single
container. This flexibility makes lists an invaluable asset for any Python programmer.

??? tip

    Closely related to lists are [tuples](tuples.md), which are *immutable*, but can be
    managed with similar syntax.

Let’s explore the concept further with a real-world analogy. Imagine you have a collection of
names, distances, and mixed data types like this:

``` python {title="Example Python Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
distance_in_kms = [32, 97, 51, 403, 21, 53, 81]
mixed_types = ["Jim", 23, 3.14, True, "Berzerk"]
```

In this example, `users` contains a `list` of names of `string` types, `distance_in_kms` stores
a `list` of distances in `int` type, and `mixed_types` seemingly defies convention by accommodating
a diverse set of data types. Lists are compelling because they allow you to organize and manipulate
such data effortlessly.

## Accessing List Items

List items can be accessed via their index system like this:

``` python {title="Accessing List Items via Indexc" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
print(f"What is your favourite moment when {users[0]} pulls a prank on {users[1]}?")
```

Returns:

``` text
What is your favourite moment when Jim pulls a prank on Dwight?
```

Lists can even be accessed through negative indexing like this:

``` python {title="Negative Indexing of Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
print(f"What was one thing that {users[-1]} did you found extra funny?")
```

Outputs:

``` text
What was one thing that Michael did you found extra funny?
```

## Adding and Removing Items from Lists

What makes lists genuinely exceptional is their *mutability*. Unlike some data types in Python,
lists can change and adapt as your program runs. Flexible, like a good morning stretch. 🧘 Adding, removing, or modifying elements within
a list makes it a dynamic tool for handling evolving data. This adaptability is particularly
useful when managing data collections that may grow or shrink in size.

``` python {title="Appending Items to Lists" linenums="1"}
users = ["Jim", "Dwight", "Michael"]
users.append("Pam")
print(f"We've added {users[-1]} to the list!")
```

Results in:
``` text
We've added Pam to the list!
```