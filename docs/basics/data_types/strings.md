# Strings

Strings are a fundamental data type used to represent text. 📝 Whether it's a single
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
empty_string = ""  # A string with nothing in it
```

??? tip "Single vs Double Quotes"

    Strings can be enclosed in either single quotes (`''`) or double quotes (`""`), allowing you
    flexibility in your code. The main benefit? Use one to contain the other:

    ```python
    message = "It's a beautiful day!"       # Single quote inside double quotes
    quote = 'He said "Hello" to me'         # Double quotes inside single quotes
    escaped = "He said \"Hello\" to me"     # Or use backslash to escape
    ```

## Concatenating Strings

Strings can be combined with simple plus (`+`) signs:

``` python {title="Basic Concatenation" linenums="1"}
first_name = "Albert"
last_name = "Einstien"
print("There was a famous scientist named " + first_name + " " + last_name + ".")
```

Would output:

``` text
There was a famous scientist named Albert Einstien.
```

### F-Strings

Introduced in version 3.6 (3.13.3 is current as of Summer 2025), "F-Strings" are a much-improved
way to build strings in Python. Once you try them, you'll never go back. ✨ Simply precede a string with f before the opening quotation. Then,
any variable can be surrounded by curly braces {}, removing the need to cast variables of various
types. For example:

``` python {title="F-Strings" linenums="1"}
name = "Jim"
age = 32
print(f"My name is {name} and I am {age} years old!")
```

Would produce:

``` text
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

``` text
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

``` text
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

``` text
Hello I am       Albert Einstein       .
Hello I am Albert Einstein.
Hello I am       Albert Einstein.
Hello I am Albert Einstein       .
```

??? tip "Slicing"

    Strings can also be *sliced* - see [Slicing Sequences](../data_structures/slicing_sequences.md)
    for more details.

## String Length and Indexing

### Getting the Length

The `len()` function tells you how many characters are in a string:

``` python {title="String Length" linenums="1"}
message = "Hello, World!"
print(len(message))  # 13

empty = ""
print(len(empty))    # 0

# Useful for validation
username = "bob"
if len(username) < 3:
    print("Username too short!")
```

### Accessing Individual Characters

Strings are *sequences* of characters, and you can access each character by its position
(index). Python uses zero-based indexing — the first character is at index 0:

``` python {title="String Indexing" linenums="1"}
word = "Python"
#       012345  ← indices

print(word[0])   # 'P' — first character
print(word[1])   # 'y' — second character
print(word[5])   # 'n' — sixth character (last one)
```

### Negative Indexing

Python also supports negative indices, which count from the end. This is incredibly useful
when you want the last character without knowing the string's length:

``` python {title="Negative Indexing" linenums="1"}
word = "Python"
#      -6-5-4-3-2-1  ← negative indices

print(word[-1])   # 'n' — last character
print(word[-2])   # 'o' — second to last
print(word[-6])   # 'P' — first character (same as word[0])
```

!!! warning "Index Out of Range"

    Accessing an index that doesn't exist raises an `IndexError`:

    ```python
    word = "Python"
    print(word[10])   # IndexError: string index out of range
    print(word[-10])  # IndexError: string index out of range
    ```

    Always check `len()` if you're unsure, or use exception handling.

## Searching Within Strings

### The `in` Operator

The simplest way to check if a substring exists:

``` python {title="Checking for Substrings" linenums="1"}
sentence = "The quick brown fox jumps over the lazy dog"

print("fox" in sentence)      # True
print("cat" in sentence)      # False
print("Fox" in sentence)      # False — case-sensitive!

# Great for conditionals
if "error" in log_message.lower():
    print("Something went wrong!")
```

### find() and index()

To get the *position* of a substring:

``` python {title="Finding Substring Positions" linenums="1"}
text = "Hello, World!"

# find() returns -1 if not found
print(text.find("World"))     # 7
print(text.find("Python"))    # -1

# index() raises ValueError if not found
print(text.index("World"))    # 7
# print(text.index("Python"))  # ValueError!

# Find starting from a specific position
text = "banana"
print(text.find("a"))         # 1 — first 'a'
print(text.find("a", 2))      # 3 — first 'a' after index 2
```

!!! tip "find() vs index()"

    Use `find()` when the substring might not exist (returns `-1`).
    Use `index()` when it *should* exist and absence is an error.

### count()

Count how many times a substring appears:

``` python {title="Counting Substrings" linenums="1"}
text = "banana"
print(text.count("a"))    # 3
print(text.count("na"))   # 2
print(text.count("x"))    # 0

# Practical example
sentence = "the cat sat on the mat"
print(sentence.count("the"))  # 2
```

## Replacing and Modifying

### replace()

Substitute parts of a string:

``` python {title="Replacing Substrings" linenums="1"}
message = "Hello, World!"
new_message = message.replace("World", "Python")
print(new_message)  # "Hello, Python!"

# Replace all occurrences
text = "one fish, two fish, red fish, blue fish"
print(text.replace("fish", "cat"))
# "one cat, two cat, red cat, blue cat"

# Limit replacements
print(text.replace("fish", "cat", 2))
# "one cat, two cat, red fish, blue fish"
```

!!! note "Strings Are Immutable"

    Strings cannot be modified in place. Methods like `replace()` return a *new* string;
    the original is unchanged:

    ```python
    original = "Hello"
    original.upper()       # Returns "HELLO" but doesn't change original
    print(original)        # Still "Hello"

    # To "change" a string, reassign it
    original = original.upper()
    print(original)        # Now "HELLO"
    ```

### Other Useful Modifications

``` python {title="More String Modifications" linenums="1"}
text = "  hello world  "

# Centering and padding
print(text.strip().center(20, "-"))  # "---hello world----"
print("42".zfill(5))                 # "00042" — pad with zeros

# Checking content
print("hello123".isalnum())    # True — letters and numbers only
print("hello".isalpha())       # True — letters only
print("12345".isdigit())       # True — digits only
print("HELLO".isupper())       # True
print("hello".islower())       # True

# Starting and ending
filename = "document.pdf"
print(filename.startswith("doc"))   # True
print(filename.endswith(".pdf"))    # True
print(filename.endswith((".pdf", ".doc", ".txt")))  # True — multiple options!
```

## Splitting and Joining

These two methods are workhorses for text processing. 🐴

### split()

Break a string into a list of parts:

``` python {title="Splitting Strings" linenums="1"}
# Split on whitespace (default)
sentence = "The quick brown fox"
words = sentence.split()
print(words)  # ['The', 'quick', 'brown', 'fox']

# Split on a specific delimiter
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Split with a limit
text = "one two three four five"
print(text.split(" ", 2))  # ['one', 'two', 'three four five']

# Split on newlines
multiline = "line1\nline2\nline3"
lines = multiline.split("\n")
print(lines)  # ['line1', 'line2', 'line3']

# Or use splitlines() for cross-platform newline handling
print(multiline.splitlines())  # ['line1', 'line2', 'line3']
```

### join()

The opposite of split — combine a list into a single string:

``` python {title="Joining Strings" linenums="1"}
words = ['The', 'quick', 'brown', 'fox']

# Join with spaces
sentence = " ".join(words)
print(sentence)  # "The quick brown fox"

# Join with any separator
print("-".join(words))     # "The-quick-brown-fox"
print("".join(words))      # "Thequickbrownfox"
print(", ".join(words))    # "The, quick, brown, fox"

# Build a path
path_parts = ["home", "user", "documents"]
print("/".join(path_parts))  # "home/user/documents"
```

!!! tip "join() is Faster Than + Concatenation"

    When combining many strings, `join()` is significantly more efficient than using `+`
    in a loop:

    ```python
    # Slow (creates many intermediate strings)
    result = ""
    for word in words:
        result = result + word + " "

    # Fast (single operation)
    result = " ".join(words)
    ```

## Multi-line Strings

For text that spans multiple lines, use triple quotes:

``` python {title="Multi-line Strings" linenums="1"}
# Triple double quotes
poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""

print(poem)

# Triple single quotes work too
sql_query = '''
SELECT *
FROM users
WHERE active = true
ORDER BY name
'''
```

Multi-line strings preserve all whitespace and newlines exactly as written. They're perfect
for:

- Long text blocks
- SQL queries
- HTML/JSON templates
- Docstrings (documentation)

??? tip "Removing Leading Whitespace"

    If indentation in your code adds unwanted leading spaces, use `textwrap.dedent()`:

    ```python
    import textwrap

    def example():
        query = textwrap.dedent("""
            SELECT *
            FROM users
            WHERE active = true
        """).strip()
        print(query)
    ```

## Raw Strings

Prefix a string with `r` to create a "raw" string where backslashes are treated literally:

``` python {title="Raw Strings" linenums="1"}
# Normal string — backslash is an escape character
print("Hello\nWorld")
# Hello
# World

# Raw string — backslash is just a backslash
print(r"Hello\nWorld")
# Hello\nWorld

# Useful for Windows paths
path = r"C:\Users\Documents\file.txt"
print(path)  # C:\Users\Documents\file.txt

# Essential for regular expressions
import re
pattern = r"\d{3}-\d{4}"  # Matches "123-4567"
```

Without the `r` prefix, you'd need to escape every backslash: `"C:\\Users\\Documents\\file.txt"`.
Raw strings save you from backslash madness. 🎭

## F-String Formatting

F-strings can do more than just insert variables — they support formatting expressions:

``` python {title="Advanced F-String Formatting" linenums="1"}
# Number formatting
price = 49.99
print(f"Price: ${price:.2f}")      # Price: $49.99
print(f"Price: ${price:10.2f}")    # Price: $     49.99 (padded)

pi = 3.14159265359
print(f"Pi: {pi:.4f}")             # Pi: 3.1416 (4 decimal places)

# Thousands separator
big_number = 1234567890
print(f"{big_number:,}")           # 1,234,567,890

# Percentage
ratio = 0.856
print(f"Score: {ratio:.1%}")       # Score: 85.6%

# Padding and alignment
name = "Bob"
print(f"{name:>10}")   # "       Bob" — right-aligned
print(f"{name:<10}")   # "Bob       " — left-aligned
print(f"{name:^10}")   # "   Bob    " — centered
print(f"{name:*^10}")  # "***Bob****" — centered with fill character

# Expressions inside f-strings
x = 10
print(f"{x} squared is {x**2}")    # 10 squared is 100
print(f"{'hello'.upper()}")         # HELLO
```

## Converting To and From Strings

``` python {title="Type Conversion" linenums="1"}
# Numbers to string
age = 25
age_str = str(age)
print("I am " + age_str)  # I am 25

# String to numbers
number = int("42")
decimal = float("3.14")

# Check if a string is a valid number
user_input = "123"
if user_input.isdigit():
    value = int(user_input)
else:
    print("Not a valid number")

# ord() and chr() — character ↔ ASCII/Unicode
print(ord("A"))      # 65
print(chr(65))       # 'A'
print(ord("🐍"))     # 128013
```

## Key Takeaways

| Concept | What to Remember |
|:--------|:-----------------|
| **Indexing** | Zero-based: `word[0]` is first, `word[-1]` is last |
| **Immutable** | Strings can't be changed; methods return new strings |
| **`in` operator** | `"sub" in string` checks for substring |
| **find() vs index()** | `find()` returns -1, `index()` raises error |
| **split() / join()** | Convert between strings and lists |
| **Triple quotes** | Multi-line strings: `"""text"""` |
| **Raw strings** | `r"path\to\file"` — backslashes are literal |
| **F-string formatting** | `f"{value:.2f}"` for formatted output |