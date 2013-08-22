rotunicode
==========

.. image:: https://badge.fury.io/py/rotunicode.png
    :target: http://badge.fury.io/py/rotunicode

.. image:: https://travis-ci.org/box/rotunicode.png?branch=master
    :target: https://travis-ci.org/box/rotunicode

RotUnicode is a Python codec that can convert a string of ASCII characters to
a Unicode string with non-ASCII characters maintaining readability.

.. code-block:: pycon

    >>> import codecs
    >>> codecs.register(RotUnicode.search_function)
    >>> 'Hello World!'.encode('rotunicode')
    Ĥȅľľő Ŵőŕľď!
    >>> 'Ĥȅľľő Ŵőŕľď!'.decode('rotunicode')
    Hello World!


RotUnicode is extremely helpful in testing your application because it makes it
easy to create strings with non-ASCII characters. Here's a bug discovered while
I was using rotunicode -

.. code-block:: pycon

    >>> import os, errno
    >>> name = 'foo'.encode('rotunicode')
    >>> os.mkdir(name)
    >>> print(name)
    ƒőő
    >>> os.path.exists(name)
    True
    >>> os.statvfs(name)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2:
    ordinal not in range(128)

The bug is filed at http://bugs.python.org/issue18695.


Supported Characters
--------------------

RotUnicode converts lower case and upper case characters of the English
alphabet and digits 0 to 9 to non-ASCII characters. All characters that are
outside this range are left as is.

.. code-block:: pycon

    >>> 'हिन्दी'.encode('rotunicode')
    हिन्दी
    >>> 'हिन्दी'.decode('rotunicode')
    हिन्दी


Installation
------------

To install, simply:

.. code-block:: bash

    $ pip install requests


Why is this named RotUnicode?
-----------------------------

RotUnicode stands for rotate-to-unicode. Or rotten-unicode for those who have
nightmares about Unicode. It was inspired by Rot13.
