

# `while` Loops

+++

Another option is a  `while` loop. The code within a `while` will run as long as the condition is `True`:

```{code-cell} ipython3
count = 0
# while count is less than 10
while count < 10:
    print(f"Counter Value: {count}.")
    count += 2
```

The loop above will evaluate the value of `count`.  While it is less than 10, it will print the value of count in the print statement, then increment the value by 2.  At that point, it will restart the loop and re-evaluate the value of `count`.
