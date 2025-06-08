# Strings

Strings are a fundamental data type used to represent text. Whether it’s a single
character or a paragraph, any text enclosed within either single quotes (`' '`) or double quotes
(`" "`) is considered a `string` in Python. Strings serve as the building blocks for text
manipulation, and Python equips us with a rich set of built-in methods, or manipulators, to
operate on strings. You can perform operations like changing letter cases, slicing (and more)
to manipulate and extract valuable information from text data.

Creating a `string` is straightforward. You assign any alphanumeric value inside single or double
quotes to a variable name using the assignment operator (`=`):

``` python {title="Declaring Basic Strings" linenums="1"}
name = "Brad"
location = 'Halifax'
occupation = 'Kubernetes Guy'
```

??? tip

    Strings can be enclosed in either single quotes ('') or double quotes (""), allowing you
    flexibility in your code. Moreover, if a string needs to contain both types of quotes, you
    can use the backslash (`\`) as an escape character to ensure Python interprets the characters
    correctly.

## Concatenating Strings

Strings can be combined with simple plus (`+`) signs:

``` python {title="Basic Concatenation" linenums="1"}
first_name = "Albert"
last_name = "Einstien"
print("There was a famous scientist named " + first_name + " " + last_name + ".")
```

Would output:

``` bash
There was a famous scientist named Albert Einstien.
```

### F-Strings

Introduced in version 3.6 (3.13.3 is current as of Summer 2025), “F-Strings” are a much-improved
way to build strings in Python. Simply precede a string with f before the opening quotation. Then,
any variable can be surrounded by curly braces {}, removing the need to cast variables of various
types. For example:

``` python {title="F-Strings" linenums="1"}
name = "Jim"
age = 32
print(f"My name is {name} and I am {age} years old!")
```

Would produce:

``` bash
My name is Jim and I am 32 years old!
```

## String Methods

Strings can accept methods which alter the contents of the string. Some examples of string methods
that are built into Python include:

``` python {title="Sample String Methods" linenums="1"}
book_title = "mastery by Robert greene"
print(book_title.upper())
print(book_title.lower())
print(book_title.title())
print(book_title.capitalize())
```

Returns:

``` bash
MASTERY BY ROBERT GREENE
mastery by robert greene
Mastery by Robert Greene
Mastery by robert greene
```

### Adding & Removing Whitespace

Special characters can be added to strings that add whitespace. These include:

- `\t` which adds a tab (4 spaces)
- `\n` which adds a newline

``` python {title="Adding Tabs and New Lines to Output" linenums="1"}
print("Hello, I'm \t \t Brad!")
print("and you are learning \n \t Python")
```

Returns:

``` bash
Hello, I'm 	 	 Brad!
and you are learning
 	 Python
```

Whitespace can also be stripped out using string methods. These include `strip()` (both sides),
`rstrip()` (right side), and `lstrip()` (left side).

``` python {title="Stripping Whitespace in Strings" linenums="1"}
name = "      Albert Einstein       "
print("Hello I am " + name + ".") # whitespace remains
print("Hello I am " + name.strip() + ".") # whitespace stripped
print("Hello I am " + name.rstrip() + ".") # whitespace on righ stripped
print("Hello I am " + name.lstrip() + ".") # whitespace on left stripped
```

Would result with:

``` bash
Hello I am       Albert Einstein       .
Hello I am Albert Einstein.
Hello I am       Albert Einstein.
Hello I am Albert Einstein       .
```

??? tip

    Strings can also be *sliced* - see [Slicing Sequences](../data_structures/slicing_sequences.md)
    for more details.