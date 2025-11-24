# Tuples

Tuples, similar to [lists](lists.md), are a sequenced collection that provides a means to collect
and organize data. However, their immutability sets tuples apart – once created, the elements
within a tuple cannot be modified. Set in stone. 🪨 In this guide, we’ll delve into what tuples are, explore why
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

## Tuple Methods

Tuples have only two methods (since they're immutable, they don't need many):

``` python {title="Tuple Methods" linenums="1"}
numbers = (1, 2, 3, 2, 4, 2, 5)

# Count occurrences
print(numbers.count(2))  # 3

# Find index of first occurrence
print(numbers.index(4))  # 4
# numbers.index(99)  # ValueError if not found!
```

## Tuple Unpacking

Unpacking is one of the most powerful features of tuples. It lets you assign multiple
variables at once:

``` python {title="Basic Unpacking" linenums="1"}
# Basic unpacking
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")  # x=10, y=20

# Unpacking in loops
coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

# Swap variables without a temp!
a, b = 1, 2
a, b = b, a  # Magic! ✨
print(f"a={a}, b={b}")  # a=2, b=1
```

### Extended Unpacking with *

Python 3 introduced the `*` operator for catching "the rest":

``` python {title="Extended Unpacking" linenums="1"}
# Grab first and rest
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5] — note: becomes a list!

# Grab first, last, and middle
first, *middle, last = (1, 2, 3, 4, 5)
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Ignore parts you don't need
name, _, _, email = ("Alice", "Developer", "NYC", "alice@example.com")
print(f"{name}: {email}")
```

### Unpacking in Function Calls

``` python {title="Unpacking in Function Calls" linenums="1"}
def greet(first_name, last_name, age):
    print(f"Hello, {first_name} {last_name}! You are {age}.")

person = ("Alice", "Smith", 30)
greet(*person)  # Unpacks tuple as positional arguments
# Hello, Alice Smith! You are 30.
```

## Named Tuples

Regular tuples access elements by index, which can be unclear. Named tuples give you
the best of both worlds — tuple efficiency with named access like a class:

``` python {title="Named Tuples" linenums="1"}
from collections import namedtuple

# Define a named tuple type
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', 'name age city')  # String also works

# Create instances
p = Point(10, 20)
alice = Person('Alice', 30, 'NYC')

# Access by name (much clearer!)
print(p.x, p.y)           # 10 20
print(alice.name)         # Alice
print(alice.age)          # 30

# Still works like a regular tuple
print(p[0], p[1])         # 10 20
x, y = p                  # Unpacking works
print(len(alice))         # 3
```

### Named Tuple Methods

``` python {title="Named Tuple Features" linenums="1"}
from collections import namedtuple

Person = namedtuple('Person', 'name age city')
alice = Person('Alice', 30, 'NYC')

# Convert to dictionary
print(alice._asdict())
# {'name': 'Alice', 'age': 30, 'city': 'NYC'}

# Create a modified copy (remember, tuples are immutable!)
bob = alice._replace(name='Bob', age=25)
print(bob)  # Person(name='Bob', age=25, city='NYC')

# Get field names
print(Person._fields)  # ('name', 'age', 'city')

# Create from an iterable
data = ['Charlie', 35, 'LA']
charlie = Person._make(data)
print(charlie)  # Person(name='Charlie', age=35, city='LA')
```

### typing.NamedTuple (Modern Alternative)

Python 3.6+ offers a class-based syntax with type hints:

``` python {title="typing.NamedTuple" linenums="1"}
from typing import NamedTuple

class Point(NamedTuple):
    x: float
    y: float
    label: str = "origin"  # Default value!

p1 = Point(10.0, 20.0)
p2 = Point(5.0, 5.0, "center")

print(p1)        # Point(x=10.0, y=20.0, label='origin')
print(p1.label)  # origin
print(p2.label)  # center
```

!!! tip "When to Use Named Tuples"

    Named tuples are perfect for:

    - Simple data containers (coordinates, RGB colors, records)
    - Return values from functions with multiple fields
    - Replacing small classes that just hold data
    - Making code more self-documenting

## Tuples vs Lists: When to Use Each

Choosing between tuples and lists is like choosing between a good espresso and a cheap pizza —
one is refined and purposeful, the other is... flexible but sometimes regrettable.

| Use Tuples When... | Use Lists When... |
|:-------------------|:------------------|
| Data shouldn't change | Data needs to be modified |
| Representing fixed collections (coordinates, RGB) | Managing dynamic collections |
| Dictionary keys (tuples are hashable!) | Order matters but items change |
| Function return values with multiple items | Stacks, queues, or buffers |
| Slightly better performance matters | You need append/remove/sort |

``` python {title="Tuples as Dictionary Keys" linenums="1"}
# Tuples can be dict keys (they're hashable)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

print(locations[(40.7128, -74.0060)])  # New York

# Lists CANNOT be dict keys
# {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Creating** | `(1, 2, 3)` or `tuple()`, single item needs comma: `(1,)` |
| **Immutable** | Cannot add, remove, or change elements |
| **Methods** | Only `count()` and `index()` |
| **Unpacking** | `x, y = point` — assign multiple variables at once |
| **Extended unpacking** | `first, *rest = items` — catch remaining items |
| **Named tuples** | `namedtuple('Point', ['x', 'y'])` — access by name |
| **Hashable** | Can be used as dict keys (lists cannot) |
| **Performance** | Slightly faster and less memory than lists |
