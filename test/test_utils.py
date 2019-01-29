# coding: utf-8

from __future__ import absolute_import, unicode_literals

import codecs
from collections import Iterator
from io import StringIO

from genty import genty, genty_dataset, genty_args
from six import with_metaclass

from rotunicode import RotUnicode, ruencode, rudecode
from rotunicode.utils import get_rotunicode_function_for_decode_argument, parse_escape_sequences, safe_unicode, stream_file_lines
# pylint:disable=wrong-import-order
from test.base_test_case import TestCase
# pylint:enable=wrong-import-order


class TypeWithoutStringMethods(type):
    def __new__(mcs, name, bases, dictionary):
        def string(self):   # pylint:disable=unused-argument
            raise ValueError
        dictionary.update(dict.fromkeys(['__str__', '__unicode__', '__bytes__', '__repr__'], string))
        return super(TypeWithoutStringMethods, mcs).__new__(mcs, name, bases, dictionary)


class ClassWithoutStringMethods(with_metaclass(TypeWithoutStringMethods, object)):  # pylint:disable=too-few-public-methods
    pass


@genty
class RotUnicodeUtilsTest(TestCase):
    """Tests for :mod:`box.util.rotunicode.utils`."""

    @classmethod
    def setUpClass(cls):
        super(RotUnicodeUtilsTest, cls).setUpClass()
        codecs.register(RotUnicode.search_function)

    @genty_dataset(
        genty_args('plain', 'ҏľȁȉń'),
        genty_args('plain', 'ҏľȁȉń', extension=False),
        genty_args('.extension', '.ȅхƭȅńŝȉőń'),
        genty_args('.extension', '.ȅхƭȅńŝȉőń', extension=False),
        genty_args('plain.txt', 'ҏľȁȉń.txt'),
        genty_args('plain.txt', 'ҏľȁȉń.txt', extension=False,),
        genty_args('plain.txt', 'ҏľȁȉń.ƭхƭ', extension=True),
        genty_args('two.ext.sions', 'ƭŵő.ȅхƭ.sions'),
        genty_args('two.ext.sions', 'ƭŵő.ȅхƭ.sions', extension=False),
        genty_args('two.ext.sions', 'ƭŵő.ȅхƭ.ŝȉőńŝ', extension=True),
    )
    def test_ruencode_encodes_string_using_rotunicode(
            self,
            source,
            target,
            extension=None,
    ):
        encoded_source = ruencode(source) if extension is None else ruencode(source, extension=extension)
        self.assertEqual(
            target,
            encoded_source,
        )

    def test_rudecode_decodes_string_using_rotunicode(self):
        self.assertEqual(
            'Hello World!',
            rudecode('Ĥȅľľő Ŵőŕľď!'),
        )

    @genty_dataset(
        ascii_byte_string=(b'plain', u'plain'),
        ascii_unicode_string=(u'plain', u'plain'),
        non_ascii_byte_string=(u'ƒøø'.encode('utf-8'), u'ƒøø'),
        non_ascii_unicode_string=(u'ƒøø', u'ƒøø'),
        non_string_object_with_unicode_method=(17, u'17'),
        undecodable_byte_string=(u'ƒøø'.encode('utf-16'), None, UnicodeDecodeError),
        non_string_object_without_unicode_method=(ClassWithoutStringMethods(), None, ValueError),
    )
    def test_safe_unicode(self, string, expected_result, expected_exception_classes=()):

        def run():
            return safe_unicode(string)

        if expected_exception_classes:
            with self.assertRaises(expected_exception_classes):
                run()
        else:
            self.assertEqual(run(), expected_result)

    @genty_dataset(False, True)
    def test_get_rotunicode_function_for_decode_argument(self, decode):
        expected_result = rudecode if decode else ruencode
        self.assertIs(get_rotunicode_function_for_decode_argument(decode=decode), expected_result)

    @genty_dataset(
        empty_string=('', ''),
        plain=('ƒøøbar', 'ƒøøbar'),
        trailing_backslash_character=('\\', None, ValueError),
        invalid_escape_sequence=('\\z', None, ValueError),
        two_backslash_characters=('\\\\', '\\'),
        mixed=('foo\\nƒøø\\t', 'foo\nƒøø\t'),
        uxxxx=('foo\\u0256', 'fooɖ'),
    )
    def test_parse_escape_sequences(self, string, expected_result, expected_exception_classes=None):

        def run():
            return parse_escape_sequences(string)

        if expected_exception_classes:
            with self.assertRaises(expected_exception_classes):
                run()
        else:
            self.assertEqual(run(), expected_result)

    def test_stream_file_lines(self):
        lines = ['foo', 'bar', 'baz', 'ƒøø', '', 'ƒoobarbaz']
        lines_with_newlines = [line + '\n' for line in lines]
        content = ''.join(lines_with_newlines)
        io_object = StringIO(content)
        result = stream_file_lines(io_object)
        self.assertIsInstance(result, Iterator)
        self.assertEqual(list(result), lines_with_newlines)
