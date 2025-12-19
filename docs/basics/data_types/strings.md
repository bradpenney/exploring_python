# Strings

Every program you've ever used displays text. Error messages, user prompts, search results, social media posts, this very sentence—all text, all represented as **strings** in the underlying code.

Strings are Python's fundamental data type for representing text. They're immutable sequences of Unicode characters, meaning they can contain everything from English letters to emojis to Chinese characters. Whether you're processing user input, reading files, scraping websites, or formatting output, you'll work with strings constantly.

Understanding strings deeply isn't optional for Python programmers—it's essential.

## What is a String?

A string in Python is any text enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`):

```python title="Creating Strings" linenums="1"
name = "Alice"              # (1)!
location = 'Halifax'        # (2)!
occupation = "Software Developer"
multiline = """This is a
longer string that spans
multiple lines."""          # (3)!
```

1. Double quotes are most common for strings
2. Single quotes work identically—use whichever you prefer
3. Triple quotes preserve line breaks and are useful for docstrings

Python treats single and double quotes identically. The flexibility lets you embed one type of quote inside the other:

```python title="Quotes Within Strings" linenums="1"
message = "He said, 'Python is great!'"
path = 'C:\\Users\\Alice\\Documents'  # (1)!
```

1. Backslash escapes special characters—here it prevents the backslash from being interpreted as an escape sequence

## Why Strings Matter

Strings are the interface between your program and the world:

- **User interaction**: Every input from a user starts as a string
- **File I/O**: Reading and writing files means processing strings
- **Web development**: HTML, JSON, URLs—all manipulated as strings
- **Data processing**: CSV files, log parsing, text analysis
- **APIs**: Most web APIs exchange data as JSON strings

You can't avoid strings in Python. The question isn't whether you'll use them, but how well you understand them.

## Building Strings with F-Strings

When you need to combine text with variables, use **f-strings** (formatted string literals)—Python's modern, preferred approach:

```python title="F-String Formatting" linenums="1"
name = "Alice"
age = 30
print(f"Hello, {name}! You are {age} years old.")  # (1)!

# F-strings support expressions
print(f"Next year you'll be {age + 1}.")  # (2)!

# And formatting specifications
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")  # (3)!
```

1. Variables inside `{...}` are automatically converted to strings and embedded
2. You can include any Python expression inside the braces
3. Format specifiers control number formatting (`.2f` means 2 decimal places)

F-strings are fast, readable, and powerful. They're the Pythonic way to build strings in modern Python (3.6+).

??? tip "Other String Building Methods You Might See"

    Older Python code uses different approaches for combining strings:

    **Concatenation with `+`**:
    ```python
    first_name = "Albert"
    last_name = "Einstein"
    full_name = first_name + " " + last_name  # Works, but verbose
    ```

    **The `.format()` method** (pre-3.6):
    ```python
    message = "Hello, {}! You are {} years old.".format(name, age)
    ```

    **Percent formatting** (very old):
    ```python
    message = "Hello, %s! You are %d years old." % (name, age)
    ```

    All three work, but f-strings are clearer, faster, and preferred in modern Python. Use f-strings unless you have a specific reason not to.

## String Indexing and Length

Need to extract the file extension from a filename? Validate that a password meets minimum length? Get the first letter of someone's name for an avatar? All require accessing specific positions in strings or checking their length.

Strings are sequences, which means each character has a position (index):

```python title="String Indexing" linenums="1"
language = "Python"
print(language[0])    # (1)!
print(language[5])
print(language[-1])   # (2)!
print(language[-2])
print(len(language))  # (3)!
```

1. Returns `'P'` - Python uses zero-based indexing so the first character is at index 0
2. Returns `'n'` - Negative indices count from the end: -1 is last, -2 is second-to-last, etc.
3. `len()` returns the number of characters in the string (6 in this case)

## Common String Methods

User input is messy. Someone types "JOHN SMITH" in all caps. Another enters "alice@email.com" when you need case-insensitive comparison. You're displaying book titles that need proper capitalization. String methods handle these real-world text processing tasks.

Python strings are immutable, but they have many methods that return modified copies:

### Case Manipulation

Converting case is essential for data normalization (comparing user input) and formatting output (displaying titles consistently):

```python title="Changing Case" linenums="1"
title = "the lord of the rings"
print(title.upper())       # (1)!
print(title.lower())
print(title.title())       # (2)!
print(title.capitalize())  # (3)!
```

1. Returns `"THE LORD OF THE RINGS"` - `.upper()` converts all characters to uppercase
2. Returns `"The Lord Of The Rings"` - `.title()` capitalizes the first letter of each word
3. Returns `"The lord of the rings"` - `.capitalize()` capitalizes only the first letter of the string

### Finding and Checking

Validating email addresses (does it contain `@`?), searching documents for keywords, checking if filenames start with a prefix, parsing structured text—all require finding or checking for substrings:

```python title="Searching Strings" linenums="1"
text = "Python is powerful and Python is popular"
print(text.find("Python"))      # (1)!
print(text.find("Ruby"))        # (2)!
print(text.count("Python"))
print(text.startswith("Python"))
print(text.endswith("popular"))
```

1. Returns `0` - `.find()` returns the index of the first occurrence
2. Returns `-1` - when substring is not found, `.find()` returns -1 (a common programming pattern)

### Splitting and Joining

CSV files, URLs, command-line arguments, user input with multiple values—all arrive as single strings that need parsing. Split them into pieces for processing, then join the results back together:

```python title="Split and Join" linenums="1"
sentence = "Python is great"
words = sentence.split()        # (1)!
print(words)                    # ['Python', 'is', 'great']

csv_data = "Alice,30,Engineer"
fields = csv_data.split(",")    # (2)!
print(fields)                   # ['Alice', '30', 'Engineer']

# Join reverses split
new_sentence = " ".join(words)  # (3)!
print(new_sentence)             # "Python is great"
```

1. `.split()` with no argument splits on whitespace
2. `.split(",")` splits on commas—useful for CSV data
3. `" ".join(list)` joins list elements with spaces between them

## Working with Whitespace

Users add trailing spaces in form fields. Tab characters appear in TSV files. You need to format output with proper indentation. Whitespace characters (spaces, tabs, newlines) matter in text processing:

```python title="Whitespace Characters" linenums="1"
print("Hello\tWorld")     # (1)!
print("Line 1\nLine 2")   # (2)!
```

1. `\t` inserts a tab character (typically displays as 4-8 spaces)
2. `\n` inserts a newline character, starting a new line

Stripping whitespace is critical when processing user input—"alice" and "alice " shouldn't be treated as different users:

```python title="Stripping Whitespace" linenums="1"
user_input = "   Alice   "
print(user_input.strip())   # (1)!
print(user_input.lstrip())  # (2)!
print(user_input.rstrip())  # (3)!
```

1. Returns `"Alice"` - `.strip()` removes whitespace from both ends (crucial for cleaning user input)
2. Returns `"Alice   "` - `.lstrip()` removes whitespace from the left side only
3. Returns `"   Alice"` - `.rstrip()` removes whitespace from the right side only

## Multiline Strings and Raw Strings

SQL queries, HTML templates, help text, formatted messages—readability matters. Triple quotes let you write multiline strings naturally without concatenation or `\n` everywhere:

```python title="Multiline Strings" linenums="1"
poem = """The road goes ever on and on,
Down from the door where it began.
Now far ahead the road has gone."""  # (1)!
print(poem)
```

1. Triple quotes preserve line breaks exactly as written

Regular expressions use lots of backslashes. Windows file paths use backslashes. Without raw strings, you'd need to double every backslash (`\\`). Raw strings treat backslashes literally, saving you from escaping hell:

```python title="Raw Strings" linenums="1"
regex_pattern = r"\d{3}-\d{2}-\d{4}"  # (1)!
windows_path = r"C:\Users\Alice\Documents"  # (2)!
```

1. The `r` prefix makes this a raw string—`\d` stays as literal `\d`, not an escape sequence
2. Without the `r`, you'd need to double every backslash: `"C:\\Users\\Alice\\Documents"`

## String Immutability

Why can't you change a string's characters in place? Immutability enables performance optimizations (string interning), makes strings safe as dictionary keys, and prevents bugs in concurrent code. When you "modify" a string, you're actually creating a new one:

```python title="Immutability Demonstration" linenums="1"
original = "Alice"

# Cannot modify in place - would raise TypeError:
# original[0] = "B"

# Must create a NEW string
modified = f"B{original[1:]}"  # (1)!
print(modified)   # (2)!
print(original)   # (3)!
```

1. Create a new string using an f-string with the slice `original[1:]` (everything after the first character)
2. Prints `"Blice"` - the new string
3. Prints `"Alice"` - the original string remains unchanged, proving immutability

This immutability makes strings safe for use as dictionary keys and enables performance optimizations.

## Practice Problems

??? question "Practice Problem 1: Indexing"

    What does `"Python"[-2]` return?

    ??? tip "Answer"

        It returns `'o'` (the second-to-last character). Negative indices count backwards from the end: `-1` is the last character, `-2` is second-to-last, etc.

??? question "Practice Problem 2: String Methods"

    Given `text = "  hello world  "`, what's the difference between `text.strip().title()` and `text.title().strip()`?

    ??? tip "Answer"

        They produce the same result: `"Hello World"`. Method chaining processes left-to-right, but in this case the order doesn't matter since `.strip()` only removes whitespace and `.title()` only affects capitalization.

??? question "Practice Problem 3: F-Strings"

    Write an f-string that prints `"The sum of 5 and 3 is 8"` using variables `a = 5` and `b = 3`.

    ??? tip "Answer"

        ```python
        a = 5
        b = 3
        print(f"The sum of {a} and {b} is {a + b}")
        ```

        F-strings evaluate expressions inside `{...}`, so `{a + b}` computes the sum.

??? question "Practice Problem 4: Split and Join"

    How would you convert `"one,two,three"` into `"one-two-three"`?

    ??? tip "Answer"

        ```python
        text = "one,two,three"
        result = "-".join(text.split(","))
        ```

        First `.split(",")` creates `['one', 'two', 'three']`, then `"-".join(...)` combines them with hyphens.

## Key Takeaways

| Concept | What It Means |
|:--------|:--------------|
| **String** | Immutable sequence of Unicode characters |
| **Indexing** | Access characters by position (zero-based, negative from end) |
| **F-strings** | Modern way to embed values: `f"Hello, {name}!"` |
| **Immutability** | Strings cannot be changed—methods return new strings |
| **Methods** | `.upper()`, `.lower()`, `.strip()`, `.split()`, `.find()`, etc. |
| **Raw strings** | `r"..."` treats backslashes literally |

## Further Reading

- [**Python String Documentation**](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) - Official reference for all string methods
- [**PEP 498 – Literal String Interpolation**](https://peps.python.org/pep-0498/) - The proposal that introduced f-strings
- [**Unicode HOWTO**](https://docs.python.org/3/howto/unicode.html) - Deep dive into Unicode support in Python
- [**Python String Formatting Best Practices**](https://realpython.com/python-f-strings/) - Real Python guide to f-strings
- [**Regular Expressions**](https://cs.bradpenney.io/fundamentals/regular_expressions/) - Advanced pattern matching for complex string operations
- [**How Parsers Work**](https://cs.bradpenney.io/fundamentals/how_parsers_work/) - Understanding how text gets parsed and processed

---

Strings are the foundation of text processing in Python. Master them early, and countless tasks—from parsing CSV files to building web applications—become straightforward. The methods are intuitive, f-strings are elegant, and the immutability prevents subtle bugs.

Every expert Python programmer started here, learning to slice, format, and manipulate text. Now it's your turn.
