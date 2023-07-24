# Looping Over a Function

A `for` loop can also be used to execute a function multiple times. For example, below we are executing `celsius_to_kelvin` three times since there are three items in the iterating list:

```python
def celsius_to_kelvin(cels):
    return cels + 273.15
    
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))
```

In the first iteration `celsius_to_kelvin(9.1)` was executed, in the second `celsius_to_kelvin(8.8)` and in the third `celsius_to_kelvin(-270.15)`.

Credit: *Python Mega Course* by Ardit Sulce
