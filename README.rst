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


RotUnicode is a Python library that can convert a string containing ASCII
characters to a string with non-ASCII characters without losing readability.

.. code-block:: pycon

    >>> 'Hello World!'.encode('rotunicode')
    Ĥȅľľő Ŵőŕľď!
    >>> 'Ĥȅľľő Ŵőŕľď!'.decode('rotunicode')
    Hello World!

In the above example, the 'Hello World' string has all ASCII characters.
Encoding it with RotUnicode gives you 'Ĥȅľľő Ŵőŕľď' which reads like
'Hello World' but has all non-ASCII characters.


Why is this named RotUnicode?
-----------------------------

RotUnicode stands for rotate-to-unicode. Or rotten-unicode for those who have
nightmares about Unicode. It was inspired by Rot13.


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


Use
---

.. code-block:: pycon

    >>> from rotunicode import ruencode
    >>> ruencode('Hello World!')
    Ĥȅľľő Ŵőŕľď!
    >>> rudecode('Ĥȅľľő Ŵőŕľď!')
    Hello World!


As a Codec
----------

In Python 2, RotUnicode can also be used as a codec, but it must first
be registered with the codecs library. This allows python to know what
functions to call to encode or decode a string using RotUnicode.

.. code-block:: pycon

    >>> import codecs
    >>> from rotunicode import RotUnicode
    >>> codecs.register(RotUnicode.search_function)
    >>> 'Hello World!'.encode('rotunicode')
    Ĥȅľľő Ŵőŕľď!


Command Line
------------

Installing RotUnicode also includes a command line tool.

.. code-block:: console

    $ rotunicode "Hello World"
    Ĥȅľľő Ŵőŕľď!
    $ rotunicode -d "Ĥȅľľő Ŵőŕľď!"
    Hello World!
    $ echo "Hello World!" > hello.txt
    $ rotunicode -f hello.txt
    Ĥȅľľő Ŵőŕľď!
    $ cat hello.txt | rotunicode -f
    Ĥȅľľő Ŵőŕľď!


Why should I use RotUnicode?
----------------------------

RotUnicode it extremely helpful in testing because it reduces the friction for
developers to test with non-ASCII strings. Imagine for example that you have a
class to represent a contact for your address book application:

.. code-block:: python

    class Contact(object):

        def __init__(self, first_name, last_name):
            super(Contact, self).__init__()
            self.first_name = first_name
            self.last_name = last_name

        def display_name(self):
            return '{} {}'.format(self.first_name, self.last_name)

Most developers would test this as follows:

.. code-block:: python

    from unittest import TestCase
    from contact import Contact

    class ContactTests(TestCase):

        def test_display_name(self):
            contact = Contact('John', 'Doe’)
            self.assertEqual('John Doe', contact.display_name()))

This test is good. But it is going to miss catching problems in the code with
non-ASCII characters. Requiring developers to remember how to type non-ASCII
characters is not practical. With RotUnicode, this is super easy:

.. code-block:: python

    from unittest import TestCase
    from contact import Contact

    class ContactTests(TestCase):

        def test_display_name_with_ascii_name(self):
            contact = Contact(u'John', u'Doe')
            self.assertEqual(u'John Doe', contact.display_name())

        def test_display_name_with_non_ascii_name(self):
            contact = Contact(ruencode(u'John'), ruencode(u'Doe'))
            self.assertEqual(ruencode(u'John Doe'), contact.display_name())


This is an example of a bug in Python
(`issue18695 <http://bugs.python.org/issue18695>`_) with non-ASCII characters -

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

