
# `os` Module

[Offical Documentation for the OS module](https://docs.python.org/3/library/os.html?highlight=os#module-os)

One of the most important modules for DevOps practitioners - the `os` module is a portable way of using operating system dependent functionality.  In a standard installation of Linux, it can be found at `/usr/lib/python3.10/os.py`.   

A lot of the functionality that is built into UNIX and Linux systems is mirrored in `os`. For example, to list the contents of the current directory:

```{code-cell} ipython3
import os
print(os.listdir('.'))
```

## Getting Started

Like other Python modules, a simple `import os` at the top of the Python program will make it methods available in the program.  The most basic usage of `os` would be to print the current working directory:

```{code-cell} ipython3
import os
print(f"The current working directory is: {os.getcwd()}")
```

To switch directories, use :p:`os.chdir('<path>')`, passing the target path as a string:

```{code-cell} ipython3
import os
print(f"The current working directory is: {os.getcwd()}")
os.chdir('../') # no output
print(f"The current working directory is: {os.getcwd()}")
```

## Working with Directories

### Making Directories

The `os` module is capable of making directories to store files such as logs in.  There are two main functions, `makedir` and `mkdirs`.  The difference between these two is that `mkdir` can only create a directory if a parent is present, whereas `makedirs` will create the parent structure as needed.  For example:

```{code-cell} ipython3
os.mkdir('./myNewDirectory/') # will work
os.makedirs('./newParentDirectory/myNewDirectory') # will succeed
```

Both `os.mkdir()` and `os.makdirs` will fail if the directory already exists (a very common scenario when running a program that generates logs).

```{note}
Use `os.makedirs()` with caution.  It is notorious for creating difficult-to-track logical errors.  If the directory structure does not exist, it will be created, even if there is an error in the path.  So it would be very easy to create `~/newParentDirectry/myNewDirectory` (note the missing "o" in "Directory").
```

### Removing Directories

Getting rid of **empty** directories is also possible.  The `os.rmdir()` and `os.removedirs()` functions work in the same way as making directories above - the `os.rmdir` will only remove one directory, wherease the `os.removedirs()` will remove all the parent structure as well.  For example:

```{code-cell} ipython3
os.rmdir('./myNewDirectory') # will only remove target directory
                             # assuming current working directory is /home/prog1700/Desktop/myNewDirectory'
os.removedirs('./newParentDirectory/myNewDirectory') # will remove all empty directories in the path
```

```{note}
    Both `os.rmdir()` and `os.removedirs()` only work with **empty** directories.  As soon as a directory contains either a file or another directory, the command will fail (or, in the case of `os.removedirs()` stop recursively walking up the file tree).  Therefore, it is possible to use either relative or absolute paths with these functions, as long as the target directories are empty.
```

+++

## Resources

[![Corey Schafer - Python Tutorial: OS Module - Use Underlying Operating System Functionality](https://img.youtube.com/vi/tJxcKyFMTGo/maxresdefault.jpg)](https://youtu.be/tJxcKyFMTGo)

```{code-cell} ipython3

```
