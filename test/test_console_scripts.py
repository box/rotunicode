# coding: utf-8

from __future__ import absolute_import, unicode_literals

import codecs
from collections import Iterator
from io import StringIO
import sys

from genty import genty, genty_args, genty_dataset
from six.moves import map   # pylint:disable=redefined-builtin

from rotunicode import RotUnicode, console_scripts
from rotunicode.utils import get_rotunicode_function_for_decode_argument
from test.base_test_case import TestCase


@genty
class TestConsoleScripts(TestCase):
    """Tests for :mod:`rotunicode.console_scripts`."""

    @classmethod
    def setUpClass(cls):
        super(TestConsoleScripts, cls).setUpClass()
        codecs.register(RotUnicode.search_function)

    @genty_dataset(False, True)
    def test_rotunicode(self, decode):
        original_lines = ['foo', 'bar', 'baz', '\u2345', 'foo\u2345baz']
        original_lines_with_newlines = [line + '\n' for line in original_lines]
        anti_action = get_rotunicode_function_for_decode_argument(not decode)
        lines = list(map(anti_action, original_lines_with_newlines))
        content = ''.join(lines)
        io_object = StringIO(content)
        result = console_scripts.rotunicode(io_object, decode=decode)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(map(anti_action, result)), lines)

    @genty_dataset(
        ('ƒőő\n', 'foo'),
        genty_args('foo\n', 'ƒőő', decode=True),
        genty_args('ƒőő', 'foo', use_stdin=True),
        genty_args('foo', 'ƒőő', decode=True, use_stdin=True),
        genty_args('ƒőő\nƒőő', 'foo\nfoo', use_stdin=True),
        ('ƒőő\\ńƒőő\n', 'foo\\nfoo'),
        ('ƒőő\\ȕᎾ➁➄➅ƒőő\n', 'foo\\u0256foo'),
        genty_args('ƒőő\nƒőő\n', 'foo\\nfoo', should_parse_escape_sequences=True),
        genty_args('ƒőőɖƒőő\n', 'foo\\u0256foo', should_parse_escape_sequences=True),
        genty_args('foo\nfoo\n', 'ƒőő\\nƒőő', decode=True, should_parse_escape_sequences=True),
        genty_args('fooɖfoo\n', 'ƒőő\\u0256ƒőő', decode=True, should_parse_escape_sequences=True),
    )
    def test_main(self, expected_string, string, decode=False, use_stdin=False, should_parse_escape_sequences=False):
        # pylint:disable=too-many-arguments
        args = []
        if decode:
            args.append('-d')
        if should_parse_escape_sequences:
            args.append('-e')
        stdin = sys.stdin
        stdout = sys.stdout
        try:
            if use_stdin:
                io_object = StringIO(string)
                sys.stdin = io_object
            else:
                args.append(string)
            sys.stdout = StringIO()
            console_scripts.main(args)
            sys.stdout.seek(0)
            self.assertEqual(sys.stdout.read(), expected_string)
        finally:
            sys.stdin = stdin
            sys.stdout = stdout
