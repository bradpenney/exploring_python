.. role:: p(code)
   :language: python

:p:`os` Module
==============

* `Offical Documentation for the OS module <https://docs.python.org/3/library/os.html?highlight=os#module-os>`_

One of the most important modules for DevOps practitioners - the :p:`os` module is a portable way of using operating system dependent functionality.  In a standard installation of Linux, it can be found at :p:`/usr/lib/python3.10/os.py`.   

A lot of the functionality that is built into UNIX and Linux systems is mirrored in :p:`os`.  For example, to list the contents of the current directory:

.. code-block:: python

    import os
    print(os.listdir('.'))

Which would list the contents of the current directory in a Python :ref:`lists`.

Getting Started
---------------

Like other Python modules, a simple :p:`import os` at the top of the Python program will make it methods available in the program.  The most basic usage of :p:`os` would be to print the current working directory:

.. code-block:: python

    import os

    print(f"The current working directory is: {os.getcwd()}")

Which would return the current working directory, such as :p:`The current working directory is : /home/prog1700/Documents`

To switch directories, use :p:`os.chdir('<path>')`, passing the target path as a string:


.. code-block:: python

    import os

    print(f"The current working directory is: {os.getcwd()}")
    os.chdir('/home/prog1700/Desktop') # no output
    print(f"The current working directory is: {os.getcwd()}")

This would show the new working directory:

.. code-block:: html

    The current working directory is : /home/prog1700/Documents
    The current working directory is : /home/prog1700/Desktop

Working with Directories
------------------------

Making Directories
~~~~~~~~~~~~~~~~~~

The :p:`os` module is capable of making directories to store files such as logs in.  There are two main functions, :p:`makedir` and :p:`mkdirs`.  The difference between these two is that :p:`mkdir` can only create a directory if a parent is present, whereas :p:`makedirs` will create the parent structure as needed.  For example:

.. code-block:: python

    os.mkdir('/home/prog1700/Desktop/myNewDirectory/') # will work
    os.mkdir('/home/prog1700/Desktop/newParentDirectory/myNewDirectory') # will fail
    os.makedirs('/home/prog1700/Desktop/newParentDirectory/myNewDirectory') # will succeed

Both :p:`os.mkdir()` and :p:`os.makdirs` will fail if the directory already exists (a very common scenario when running a program that generates logs).

.. note::
    Use :p:`os.makedirs()` with caution.  It is notorious for creating difficult-to-track logical errors.  If the directory structure does not exist, it will be created, even if there is an error in the path.  So it would be very easy to create :p:`/home/prg1700/Desktop/newParentDirectory/myNewDirectory` (note the missing "o" in "prog").

Removing Directories
~~~~~~~~~~~~~~~~~~~~

Getting rid of **empty** directories is also possible.  The :p:`os.rmdir()` and :p:`os.removedirs()` functions work in the same way as making directories above - the :p:`os.rmdir` will only remove one directory, wherease the :p:`os.removedirs()` will remove all the parent structure as well.  For example:

.. code-block:: python

    os.rmdir('myNewDirectory') # will only remove target directory
                               # assuming current working directory is /home/prog1700/Desktop/myNewDirectory'
    os.removedirs('/home/prog1700/Desktop/newParentDirectory/myNewDirectory') # will remove all empty directories in the path

.. note::
    Both :p:`os.rmdir()` and :p:`os.removedirs()` only work with **empty** directories.  As soon as a directory contains either a file or another directory, the command will fail (or, in the case of :p:`os.removedirs()` stop recursively walking up the file tree).  Therefore, it is possible to use either relative or absolute paths with these functions, as long as the target directories are empty.


Resources
---------

.. figure:: https://img.youtube.com/vi/tJxcKyFMTGo/maxresdefault.jpg
    :width: 500
    :alt: Corey Schafer - Python Tutorial: OS Module - Use Underlying Operating System Functionality
    :target: https://youtu.be/tJxcKyFMTGo

    Corey Schafer - Python Tutorial: OS Module - Use Underlying Operating System Functionality