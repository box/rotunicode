rotunicode
==========

.. image:: https://travis-ci.org/box/rotunicode.png?branch=master
    :target: https://travis-ci.org/box/rotunicode

.. image:: https://coveralls.io/repos/box/rotunicode/badge.png
    :target: https://coveralls.io/r/box/rotunicode

.. image:: https://pypip.in/v/rotunicode/badge.png
    :target: https://pypi.python.org/pypi/rotunicode

.. image:: https://pypip.in/d/rotunicode/badge.png
    :target: https://pypi.python.org/pypi/rotunicode

Upcoming Breaking Change!
-------------------------

When RotUnicode was released through version 0.3.0, it was released under the namespace
box.util. In version 1.1.2, importing rotunicode became easier:

.. code-block:: python

    from rotunicode import RotUnicode

vs.

.. code-block:: python

    from box.util.rotunicode import RotUnicode

In version 2.0.0, however, you will no longer be able to import rotunicode from box.util.

About
-----

RotUnicode is a Python codec that can convert a string of ASCII characters to
a Unicode string with non-ASCII characters maintaining readability.

.. code-block:: pycon

    >>> import codecs
    >>> from rotunicode import RotUnicode
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

.. code-block:: console

    pip install rotunicode


Contribute
----------

See `CONTRIBUTING <https://github.com/box/rotunicode/blob/master/CONTRIBUTING.rst>`_.


Setup
~~~~~

Create a virtual environment and install packages:

.. code-block:: console

    mkvirtualenv rotunicode
    pip install -r requirements-dev.txt


Testing
~~~~~~~

Run all tests using:

.. code-block:: console

    tox

The tox tests include code style checks via pep8 and pylint.


Why is this named RotUnicode?
-----------------------------

RotUnicode stands for rotate-to-unicode. Or rotten-unicode for those who have
nightmares about Unicode. It was inspired by Rot13.


Copyright and License
---------------------

::

 Copyright 2014 Box, Inc. All rights reserved.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
