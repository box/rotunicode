# coding: utf-8

from __future__ import unicode_literals
from os.path import splitext

from .rotunicode import RotUnicode


_ROT_UNICODE = RotUnicode()


def safe_unicode(data):
    """ Helper to safely convert <string's> that contain unicode to unicode.
    Otherwise argparse barfs. """
    if isinstance(data, str):
        return data.decode('utf-8')
    else:
        return unicode(data)


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

    encoded_value, _ = _ROT_UNICODE.encode(file_name)
    return encoded_value + file_ext


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
    decoded_value, _ = _ROT_UNICODE.decode(string)
    return decoded_value
