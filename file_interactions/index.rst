.. role:: p(code)
   :language: python

File Interactions
=================

Writing stand-alone programs is fun, but programming gets a lot more fun and interesting when we deal with persistent data. This section of the website will contain info about how to interact with four (4) common types of files - CSV, JSON, XML and databases.

.. toctree::
   :maxdepth: 1
   
   csv
   json
   xml
   databases

Using Basic :p:`txt` Files
--------------------------

.. figure:: https://img.youtube.com/vi/4mX0uPQFLDU/maxresdefault.jpg
    :width: 500
    :alt: Text Files in Python
    :target: https://youtu.be/4mX0uPQFLDU

    Text Files in Python

To open a standard text file in Python, use the :p:`open()` method.  The most basic way to do this is to by setting a variable equal to the open method:

.. code-block:: python

   f = open("mySampleTextFile.txt")
   text = f.read()
   f.close()

At this point, if the programmer were to print the contents of :p:`text` (:p:`print(text)`) then whatever is written in the text file would be printed to standard output.

There is, however, a more robust way to open a file that doesn't require explicit closing and will not cause corruption if there is an error before the file is closed (or the programmer forgets to close it!).  This is done using the :p:`with` keyword:

.. code-block:: python

   with open("mySampleTextFile.txt") as fileObject:
       myText = fileObject.read()

The advantage of this method (other than it is a little shorter) is that Python will handle any exception that occurs and will close the file automatically. This means that even if an exception occurs or something goes wrong, the file gets closed (meaning it is safe from corruption and the computer's memory is managed properly).

.. warning::

   Attempting to open a file that doesn't exist will throw an :p:`Error` unless explicitly handled.

The :p:`open` function accepts several arguments, the first being the filename, and the second being the file "mode".  Possible modes include :p:`r` (read), :p:`w` (write), and :p:`a` (append). 

.. note::

   The :p:`open` method accepts more arugments, this discussion isn't exhaustive.

When opening a file in write mode, Python will overwrite the file if it exists already, and will create the file if it doesn't.  As an example:

.. code-block::

   motorcycles = ['kawasaki', 'honda', 'ducatti', 'bmw', 'suzuki']

   with open("motorcycles.txt", "w") as f:
       for motorcycle in motorcycles:
           print(motorcycle, file=f) # each entry on its own line
           f.write(motorcycle) # all entries together, no spaces or line breaks

As mentioned above, the default behaviour of :p:`"w"` is to overwrite the file, thereby losing anything that was pre-existing in the file.  While this is advantageous in some circumstances, a more cautious apprach would be to use :p:`"a"` (append), which simply writes to the end of the file.  Append will also create the file if it doesn't exist, so it is usually the better choice unless the requirement is explicitly to overwrite existing text files.
