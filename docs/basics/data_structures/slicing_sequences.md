# Slicing Sequences

Slicing is a powerful technique that allows you to extract specific portions of data from
Python sequences such as [lists](lists.md), strings, and [tuples](tuples.md). It provides
you with the ability to finely control what data you need, whether it’s from the beginning,
end, or anywhere in between. This slicing capability is governed by both positive and negative
index systems, making it a versatile tool for data manipulation.

Consider the following index systems for a list:

``` python {title="Indexing Sequences" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Positive index system
#   0      1      2      3      4      5      6
# Negative index system
#  -7     -6     -5     -4     -3     -2     -1
print(days[-2])
print(days[2])
```

Results in:

``` bash
Saturday
Wednesday
```

Easily access specific portions of a list using slicing. For example, to access the 2nd, 3rd,
and 4th items of a list named days, you can use the following code:

``` python {title="Slicing Lists" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sliced_days = days[1:4]
print(sliced_days)
```

Would output:

``` bash
['Tuesday', 'Wednesday', 'Thursday']
```

Retrieve the first three items of a list by simply omitting the starting index:

``` python {title="Retrieving First 3 Items in a List" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
first_three_days = days[:3]
print(first_three_days)
```

Would result in:

``` bash
['Monday', 'Tuesday', 'Wednesday']
```

To get the last three items, you can use negative indexing:

``` python {title="Negative Slicing of Lists" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
last_three_days = days[-3:]
print(last_three_days)
```

Outputs:

``` bash
['Friday', 'Saturday', 'Sunday']
```

For everything except the last item, exclude it by slicing until one element from the end:

``` python {title="Exclude the Last Item in a List" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
everything_but_last = days[:-1]
print(everything_but_last)
```

Results in:

``` bash
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
```

Similarly, you can exclude the last two items:

``` python {title="Exclude the Last 2 Items in a List" linenums="1"}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
everything_but_last_two = days[:-2]
print(everything_but_last_two)
```

Returns:

``` bash
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```

## Slicing Strings and Tuples

Strings and tuples share the same slicing principles as lists. You can effortlessly extract
portions of text from a string or elements from a tuple using slicing. For example, consider
this example:

``` python {title="Slicing Strings" linenums="1"}
text = "Hello, World!"
sliced_text = text[7:12]
print(sliced_text)
```

Would output:

``` bash
World
```
