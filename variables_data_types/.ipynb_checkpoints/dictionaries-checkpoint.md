---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.7
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Dictionaries

Dictionaries are slightly more complex data types, they work with *key-value* pairings.  They're more complex than [Lists](./lists.md) but do not contain the functionality that will be encountered with [Classes](../functions_and_classes/classes.md).

To declare a simple dictionary in Python, use curly braces and use a colon to separate the key from the value:

```{code-cell} ipython3
# A dictionary containing mountain elevations
mountain_elevations = {"mount jo": 3213.9, "gros mourne": 4392.1}
print(mountain_elevations)
```

Obviously we don't always want to print out the entire dictionary.  It is easy to access the value in the *key-value* using similar techniques to accessing an element in a list:

```{code-cell} ipython3
# A dictionary containing mountain elevations
mountain_elevations = {"mount jo": 3213.9, "gros mourne": 4392.1}
print("The elevation of Mount Jo is " + str(mountain_elevations['mount jo']) + " feet.")
```

## Changing Key-Value Pairs in a Dictionary

To add a *key-value* pair to a dictionary, simply declare a new key and then assign it a value:

```{code-cell} ipython3
# Existing list
mountain_elevations = {"mount jo": 3213.9, "gros mourne": 4392.1}
# Add a new value
mountain_elevations['whiteface'] = 4867.3
print(mountain_elevations)
```

To modify a *key-value* pair, the process is similar to adding, but instead simply change the value:

```{code-cell} ipython3
# Existing list
mountain_elevations = {"mount jo": 3213.9, "gros mourne": 4392.1, "whiteface":4867.3}
# Modify a  value
mountain_elevations['gros mourne'] = 4387.1
print(mountain_elevations)
```

There is also a way to remove *key-value* pairs:

```{code-cell} ipython3
# Existing list
mountain_elevations = {"mount jo": 3213.9, "gros mourne": 4392.1, "whiteface":4867.3}
# Delete a key-value pair
del mountain_elevations['gros mourne']
print(mountain_elevations)
```

## Nesting Dictionaries

### Lists Containing Dictionaries
It is possible to nest dictionaries within both lists and dictionaries.  For example, if we created a list of enemies in a video game, they could be grouped in a list of enemies:

```{code-cell} ipython3
infantry = {'name':'infantry', 'weapon':'a sword', 'hitpoints':50, 'damageInflicted':5, 'killPoints':30}
archer = {'name':'archer', 'weapon':'arrows', 'hitpoints':20, 'damageInflicted':10, 'killPoints':20}
catapult = {'name':'catapult', 'weapon':'flying rocks', 'hitpoints':10, 'killPoints':50}
enemies = [infantry, archer, catapult]

for enemy in enemies:
  print("When facing the " + enemy['name'].title() + 
     ", this enemy will try to kill you with " + enemy['weapon'].lower() +
     "! However, once you defeat the " + enemy['name'] + ", you will gain " + str(enemy['killPoints']) + " points.")
```

It is also possible to perform the same type of operation without formally naming each dictionary.  The following example would produce exactly the same output:

```{code-cell} ipython3
enemies = [
     {'name':'infantry', 'weapon':'a sword', 'hitpoints':50, 'damageInflicted':5, 'killPoints':30},
     {'name':'archer', 'weapon':'arrows', 'hitpoints':20, 'damageInflicted':10, 'killPoints':20},
     {'name':'catapult', 'weapon':'flying rocks', 'hitpoints':10, 'killPoints':50} 
]

for enemy in enemies:
  print("When facing the " + enemy['name'].title() + 
     ", this enemy will try to kill you with " + enemy['weapon'].lower() +
     "! However, once you defeat the " + enemy['name'] + ", you will gain " + str(enemy['killPoints']) + " points.")
```

## Dictionaries Containing Lists

Dictionaries can also contain lists as their *values* (not as *keys*).  For example:

```{code-cell} ipython3
myPizza = {
  'crust':'stuffed',
  'toppings':['pepperoni', 'bacon', 'green pepper']
}

print("Your pizza will be a " + myPizza['crust'].title() + "-crust with the following toppings:")
for topping in myPizza['toppings']:
  print("\t-> " + topping.title())
```

\*Credit for above example: *Python Crash Course* by Eric Matthes, page 112.

+++

[![Socratica: Python Dictionaries](https://img.youtube.com/vi/XCcpzWs-CI4/maxresdefault.jpg)](https://youtu.be/XCcpzWs-CI4)
