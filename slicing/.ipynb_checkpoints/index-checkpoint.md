<!-- #region -->


# Slicing Python Variables

Lists, strings, and tuples have a positive index system:

``` python
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
       0      1      2      3      4      5      6
```
And they have a negative index system as well:

``` python
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
      -7     -6     -5     -4     -3     -2     -1
```
In a list, the 2nd, 3rd, and 4th items can be accessed with:

<!-- #endregion -->

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
```

First three items of a list:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
```

Last three items of a list:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
```

Everything but the last:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
```

Everything but the last two:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
```

A dictionary value can be accessed using its corresponding dictionary key:

```python
phone_numbers = {"Fred Flintstone":"+37682929928","Barney Rubble":"+423998200919"}
phone_numbers["Barney Rubble"]
```

Credit: *Python Mega Course* by Ardit Sulce on Udemy
