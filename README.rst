rotunicode
==========

.. image:: https://travis-ci.org/box/rotunicode.png?branch=master
    :target: https://travis-ci.org/box/rotunicode

.. image:: https://coveralls.io/repos/box/rotunicode/badge.png
    :target: https://coveralls.io/r/box/rotunicode

.. image:: https://pypip.in/v/rotunicode/badge.png
    :target: https://crate.io/packages/rotunicode

.. image:: https://pypip.in/d/rotunicode/badge.png
    :target: https://crate.io/packages/rotunicode

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
easy to create strings with non-ASCII characters. Example -

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

This bug is filed at http://bugs.python.org/issue18695.


Supported Characters
--------------------

RotUnicode converts lower case and upper case characters of the English
alphabet and digits 0 to 9 to non-ASCII characters. All characters that are
outside this range are left as is.

.. code-block:: pycon

    >>> 'हेलो World!'.encode('rotunicode')
    हेलो Ŵőŕľď!
    >>> 'हेलो Ŵőŕľď!'.decode('rotunicode')
    हेलो World!


Installation
------------

To install, simply:

.. code-block:: bash

    $ pip install rotunicode


Contribute
----------

Contributions are welcome and encouraged! The easiest way is to fork the repo
and then make a pull request from your fork. Read `this
<https://help.github.com/articles/fork-a-repo>`_ for help.


Setup
^^^^^

Install packages using:

.. code-block:: bash

    $ pip install -r requirements-dev.txt


Testing
^^^^^^^

Run all tests using:

.. code-block:: bash

    $ tox

The tox tests include code style checks via pep8 and pylint.


Why is this named RotUnicode?
-----------------------------

RotUnicode stands for rotate-to-unicode. Or rotten-unicode for those who have
nightmares about Unicode. It was inspired by Rot13.
