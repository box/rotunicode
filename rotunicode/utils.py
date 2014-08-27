# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from os.path import splitext


def ruencode(string, extension=False):
    """Encode a string using 'rotunicode' codec.

    :param string:
        The input string to encode.
    :type string:
        `basestring`

    :param extension:
        True if the entire input string should be encoded.
        False to split the input string using :func:`os.path.splitext` and
        encode only the file name portion keeping the extension as is.
    :type extension:
        `bool`

    :return:
        Encoded string.
    :rtype:
        `unicode`
    """
    if extension:
        file_name = string
        file_ext = ''
    else:
        file_name, file_ext = splitext(string)

    return file_name.encode('rotunicode') + file_ext


def rudecode(string):
    """Decode a string using 'rotunicode' codec.

    :param string:
        The input string to decode.
    :type string:
        `basestring`

    :return:
        Decoded string.
    :rtype:
        `unicode`
    """
    return string.decode('rotunicode')
