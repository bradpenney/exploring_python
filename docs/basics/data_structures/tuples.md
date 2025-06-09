# Tuples

Tuples, similar to [lists](lists.md), are a sequenced collection that provides a means to collect
and organize data. However, their immutability sets tuples apart – once created, the elements
within a tuple cannot be modified. In this guide, we’ll delve into what tuples are, explore why
they are used, and demonstrate some practical use cases for these unchangeable data structures.

## Understanding Tuples

A `tuple` is a collection of elements, just like a list, but it differs crucially: *it cannot be
changed or altered once declared*. This immutability makes tuples an ideal choice for ensuring
that the data remains constant throughout your program’s execution. Consider tuples as containers
for values that should remain fixed, such as the results obtained from a database SELECT statement
in SQL. These results might be crucial to your Python program, but you want to guarantee their
integrity and prevent unintentional modifications.

## Creating Tuples

Creating a tuple in Python is relatively straightforward. Instead of using square brackets, as you
would with a list, you **use parentheses to define a tuple**. Here’s how you can create tuples to store
server names and ages:

``` python {title="Basic Tuples" linenums="1"}
servers = ('web01', 'web02', 'app01', 'db01')
ages = (12, 19, 32, 41)
```

Once you’ve created these tuples, you can access their elements using indexing, just like a list.
For example, to retrieve the first element from the ages tuple, you can use:

``` python {title="Retrieving Elements in a Tuple" linenums="1"}
print(ages[0])
```

Would result in:

``` text
12
```

## Use Cases for Tuples

Now, let’s explore some practical use cases for tuples.

- **Store Constant Values**: Lsuch as mathematical constants or configuration settings,
  ensuring that they remain unchanged throughout the program’s execution.
- **Unpacking Contstants - Returning Multiple Values**: Functions in Python can return multiple
  values as a tuple. This allows you to efficiently pack and unpack data when calling and
  receiving function results.

``` python {title="Tuples Use Case: Unpacking Constants" linenums="1"}
def get_user_info(user_id):
    # retrieve user data
    return ('John', 'Doe', 30)

first_name, last_name, age = get_user_info(123)
```

- **Database Results**: As mentioned earlier, tuples are perfect for holding database query results.
  They maintain the integrity of fetched data while allowing you to work with it effectively.
- **Coordinate Pairs**: Tuples can represent coordinates or pairs of values, which is handy in
  applications involving geometry or mapping.

``` python {title="Tuples Use Case: Coordinate Pairs" linenums="1"}
lat = 43.642567
long = -79.387054
cn_tower = (lat, long) # immutable
print(f"The CN Tower stands at {cn_tower[0]} latitude, and {cn_tower[1]} longitude.")
```

Would return:

``` text
The CN Tower stands at 43.642567 latitude, and -79.387054 longitude.
```

