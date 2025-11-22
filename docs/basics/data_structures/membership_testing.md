# Membership Testing

When working with data structures, one of the most common questions is
*"Does this value exist in this data structure?"* 🔍 Python comes to the rescue here with two
operators: `in` and `not in`.

## Testing Membership in Sequences

Recall that the sequence types in Python are [`list`](lists.md) and [`tuples`](tuples.md). While
they can contain any data type, the order of the elements is guaranteed.

Testing membership using the `in` and `not in` operators combined with an
[`if` statement](../control_structures/if_statements.md) returns a *truthy* value
([`boolean`](../data_types/booleans.md)) to indicate membership:

``` python {title="Testing Membership in a List" linenums="1"}
fav_books = ['mastery', 'the signal and the noise', 'the organized mind']

if 'mastery' in fav_books:
    print("One of your favourites!")
else:
    print("Maybe something new to consider?")
```

Returns:

``` text
One of your favourites!
```

Using `not in` works the opposite:

``` python {title="Negative Testing Membership in a List" linenums="1"}
fav_books = ['mastery', 'the signal and the noise', 'the organized mind']

if 'discipline is destiny' not in fav_books:
    print("Have your read this one? Maybe you should!")
else:
    print("Ye ole` favourites once again!")
```

Would result in:

``` text
Have your read this one? Maybe you should!
```

## Testing Membership in Dictionaries

Dictionaries (the [`dict` data structure](../data_structures/dictionaries.md)) present a little
bit of a special case in testing membership, the caveat being you must remember that by default,
the test runs against the *key* of the dictionary, not the entire *key/value* pair, nor against
the *value* itself.

``` python {title="Testing Membership in Dictionary Keys" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

if 'year' in dream_car:
    print("Good to know the year of your dream car!")
else:
    print("What year is your dream car?")
```

Would output:

``` text
Good to know the year of your dream car!
```

If you'd like to test to see if a specific value is in a dictionary, remmember to use the
`dict.values()` method:

``` python {title="Negative Testing Membership in Dictionary Values" linenums="1"}
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400,
}

if 'Pinto' not in dream_car.values():
    print("Your dream car isn't a Pinto???!??")
else:
    print("Nothing quite as sweet as a lovely Pinto!")
```

Which would return:

``` text
Nothing quite as sweet as a lovely Pinto!
```