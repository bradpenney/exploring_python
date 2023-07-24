
# Floats

A Float is similar to an `int`, except it includes decimal places (i.e. `pi = 3.14`).

Floats take up more memory (RAM) than integers in the Python program, so should only be used when needed.  If an `int` will work, use it.  However, with modern computers having a significant amount of RAM, this is less of a concern than it was in the past.

Floats are declared in the same way as an `int`:

```{code-cell} ipython3
pi = 3.14
price = 10.99
temperature = 21.05
```

As mentioned, a `float` can be the quotient of two integers.  However, if any mathematical operation is performed and one of the numbers is a `float`, the result will also be a `float`.

```{code-cell} ipython3
number_of_items = 5 # integer
price = 10.99 #float
total_price = number_of_items * price # 54.95 will now be assigned to the "total_price" variable, which is a float
print(total_price)
```

```{code-cell} ipython3

```
