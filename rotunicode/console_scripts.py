# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

import argparse
from io import StringIO
import sys

from six.moves import map   # pylint:disable=redefined-builtin

from .utils import (
    get_rotunicode_function_for_decode_argument,
    parse_escape_sequences,
    safe_unicode,
    stream_file_lines,
)


def main(args=None):
    parser = argparse.ArgumentParser(
        description='Rotate to Unicode. Convert ASCII characters in a string'
                    'to non-ASCII characters while maintaining readability.',
    )
    parser.add_argument(
        '-d',
        '--decode',
        action='store_true',
        help='Decode a string previously encoded with rotunicode.',
    )
    parser.add_argument(
        '-e',
        dest='should_parse_escape_sequences',
        action='store_true',
        help=(
            'Like `echo -e`, use the backslash character for escape sequences,'
            ' including \\uxxxx. Only valid with an explicit string argument.'
        ),
    )
    input_group = parser.add_argument_group(
        title='Input',
        description='What to rotate to unicode. The following options are'
                    'mutually exclusive.',
    )
    input_group.add_argument(
        '-f',
        '--file',
        action='store',
        type=argparse.FileType('r'),
        nargs='?',
        help='The stream to be rotated from ASCII to non-ASCII (or decoded, if'
             '-d is specified.',
    )
    input_group.add_argument(
        'string',
        type=safe_unicode,
        action='store',
        nargs='?',
        help='The string to be rotated from ASCII to non-ASCII (or decoded, if'
             '-d is specified.',
    )
    options = parser.parse_args(args)
    if options.string:
        input_string = options.string + '\n'
        if options.should_parse_escape_sequences:
            input_string = parse_escape_sequences(input_string)
        file_to_read = StringIO(input_string)
    else:
        file_to_read = options.file or sys.stdin
    for line in rotunicode(file_to_read, decode=options.decode):
        print(line, end='')
    return 0


def rotunicode(io_object, decode=False):
    """Rotate ASCII <-> non-ASCII characters in a file.

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
        Yield the converted lines of the file.
    :rtype:
        `generator` of `unicode`
    """
    rotu_fn = get_rotunicode_function_for_decode_argument(decode=decode)
    return map(rotu_fn, map(safe_unicode, stream_file_lines(io_object)))
