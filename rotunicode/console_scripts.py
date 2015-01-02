# coding: utf-8

from __future__ import unicode_literals
import argparse
import sys
from .utils import rudecode, ruencode


def safe_unicode(data):
    """ Helper to safely convert <string's> that contain unicode to unicode.
    Otherwise argparse barfs. """
    if isinstance(data, str):
        return data.decode('utf-8')
    else:
        return unicode(data)


def main():
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
    options = parser.parse_args()
    if options.string:
        string = options.string
    elif options.file:
        string = safe_unicode(options.file.read()).rstrip('\n')
    else:
        string = safe_unicode(sys.stdin.read()).rstrip('\n')
    if options.decode:
        print rudecode(string)
    else:
        print ruencode(string).encode('utf-8')
