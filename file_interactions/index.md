# File Interactions

Writing stand-alone programs is fun, but programming gets a lot more fun and interesting when we deal with persistent data. This section of the website will contain info about how to interact with four (4) common types of files - CSV, JSON, XML and databases.

- [CSV](./csv.md)
- [JSON](./json.md)
- [XML](./xml.md)
- [SQL Databases](./databases.md)


# Using Basic `txt` Files

[![Socratica: Text Files in Python](https://img.youtube.com/vi/4mX0uPQFLDU/maxresdefault.jpg)](https://youtu.be/4mX0uPQFLDU)

To open a standard text file in Python, use the `open()` method.  The most basic way to do this is to by setting a variable equal to the open method:

```python
f = open("./my_sample_text_file.txt")
text = f.read()
f.close()
```

At this point, if the programmer were to print the contents of `my_sample_text_file.txt` (`print(text)`) then whatever is written in the text file would be printed to standard output.

There is, however, a more robust way to open a file that doesn't require explicit closing and will not cause corruption if there is an error before the file is closed (or the programmer forgets to close it!).  This is done using the `with` keyword:

```python
with open("./my_sample_text_file.txt") as file_object:
    my_text = file_object.read()
    
print(my_text)
```

The advantage of this method (other than it is a little shorter) is that Python will handle any exception that occurs and will close the file automatically. This means that even if an exception occurs or something goes wrong, the file gets closed (meaning it is safe from corruption and the computer's memory is managed properly).

```{warning}
Attempting to open a file that doesn't exist will throw an `Error` unless explicitly handled.
```

The `open` function accepts several arguments, the first being the filename, and the second being the file "mode".  Possible modes include `r` (read), `w` (write), and `a` (append). 

```{note}
The `open` method accepts more arugments, this discussion isn't exhaustive.
```

When opening a file in write mode, Python will overwrite the file if it exists already, and will create the file if it doesn't.  As an example:

```python
motorcycles = ['kawasaki', 'honda', 'ducati', 'bmw', 'suzuki']

with open("motorcycles.txt", "w") as f:
    for motorcycle in motorcycles:
        print(motorcycle, file=f) # each entry on its own line
        f.write(motorcycle) # all entries together, no spaces or line breaks
```

As mentioned above, the default behaviour of `"w"` is to overwrite the file, thereby losing anything that was pre-existing in the file.  While this is advantageous in some circumstances, a more cautious apprach would be to use `"a"` (append), which simply writes to the end of the file.  Append will also create the file if it doesn't exist, so it is usually the better choice unless the requirement is explicitly to overwrite existing text files. 
