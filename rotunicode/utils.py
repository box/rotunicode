# coding: utf-8

from __future__ import absolute_import, unicode_literals

from itertools import repeat, takewhile
from json.decoder import scanstring
from operator import methodcaller
from os.path import splitext

from six import binary_type, raise_from, text_type
from six.moves import map   # pylint:disable=redefined-builtin

from .rotunicode import RotUnicode


_ROT_UNICODE = RotUnicode()


def safe_unicode(data):
    """ Helper to safely convert <string's> that contain unicode to unicode.
    Otherwise argparse barfs. """
    if isinstance(data, binary_type):
        return data.decode('utf-8')
    return text_type(data)


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


_ROTUNICODE_FUNCTION_FOR_DECODE_ARGUMENT = {
    False: ruencode,
    True: rudecode,
}


def get_rotunicode_function_for_decode_argument(decode=False):
    """Return either `ruencode` or `rudecode`, depending on :param:`decode`.

    :param decode:
        (optional) If True, return `rudecode`.
        Defaults to False (return `ruencode`).
    :type decode:
        `bool`
    :return:
        Either `ruencode` or `rudecode`.
    :rtype:
        `callable` of (`basestring`) -> `unicode`
    """
    return _ROTUNICODE_FUNCTION_FOR_DECODE_ARGUMENT[decode]


def parse_escape_sequences(string):
    """Parse a string for possible escape sequences.

    Sample usage:
    >>> parse_escape_sequences('foo\\nbar')
    'foo\nbar'
    >>> parse_escape_sequences('foo\\\\u0256')
    'foo\\u0256'

    :param string:
        Any string.
    :type string:
        `basestring`
    :raises:
        :class:`ValueError` if a backslash character is found, but it doesn't
        form a proper escape sequence with the character(s) that follow.
    :return:
        The parsed string. Will parse the standard escape sequences, and also
        basic \\uxxxx escape sequences.
        \\uxxxxxxxxxx escape sequences are not currently supported.
    :rtype:
        `unicode`
    """
    string = safe_unicode(string)
    characters = []
    i = 0
    string_len = len(string)
    while i < string_len:
        character = string[i]
        if character == '\\':
            # Figure out the size of the escape sequence. Most escape sequences
            # are two characters (e.g. '\\' and 'n'), with the sole exception
            # being \uxxxx escape sequences, which are six characters.
            if string[(i + 1):(i + 2)] == 'u':
                offset = 6
            else:
                offset = 2

            try:
                # `json.decoder.scanstring()` mostly does what we want, but it
                # also does some stuff that we don't want, like parsing quote
                # characters. This will mess us up. The iteration and scanning
                # within this loop is meant to isolate the escape sequences, so
                # that we'll always be calling it with something like
                # >>> scanstring('"\n"', 1)
                # or
                # >>> scanstring('"\u0256"', 1)
                # The 1 refers to the location of the first character after the
                # open quote character.
                json_string = '"' + string[i:(i + offset)] + '"'
                character = scanstring(json_string, 1)[0]
                characters.append(character)
                i += offset
            except ValueError:
                # If an exception was raised, raise a new `ValueError`. The
                # reason we don't re-raise the original exception is because,
                # in Python 3, it is a custom JSON `ValueError` subclass. We
                # don't want to raise a JSON error from a function that has
                # nothing to do with JSON, so we create a new `ValueError`. The
                # error message is also nonsensical to the caller, in all
                # cases.
                raise_from(ValueError(string), None)
        else:
            characters.append(character)
            i += 1
    return ''.join(characters)


def stream_file_lines(io_object):
    """Stream the lines of a file.

    This is a more powerful version of `io.TextIOWrapper.readlines()`. For file
    streams / pipes such as `sys.stdin`, that method will hang until EOF has
    been read, preventing the caller from acting on any lines until the full
    content is available.

    Callers can get data from `io.TextIOWrapper.readline()` (which only hangs
    between reads of newline characters). This generator does that, and
    provides the user with an iterable stream of lines that can be iterated
    through at any time.

    The generator will automatically terminate when EOF has been reached, i.e.
    when `io.TextIOWrapper.readline()` returns the empty string.

    :param io_object:
        The file object to convert.
    :type io_object:
        :class:`io.TextIOWrapper`
    :param decode:
        If True, perform a rotunicode-decode (rotate from non-ASCII to ASCII).
        Defaults to False (rotate from ASCII to non-ASCII).
    :type decode:
        `bool`
    :return:
        Yield the converted lines of the file. The generator will terminate
        before it would have yielded an empty string. Each line will contain
        its terminating newline.
    :rtype:
        `generator` of `unicode`
    """
    return takewhile(
        bool,
        map(methodcaller('readline'), repeat(io_object)),
    )
