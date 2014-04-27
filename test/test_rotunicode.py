# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
from unittest import TestCase

# pylint:disable=import-error,no-name-in-module
from box.test.genty import genty, genty_dataset
# pylint:enable=import-error,no-name-in-module
from box.util.rotunicode import RotUnicode


@genty
class RotUnicodeTest(TestCase):
    """Tests for :mod:`box.util.rotunicode.rotunicode`."""

    @classmethod
    def setUpClass(cls):
        super(RotUnicodeTest, cls).setUpClass()
        codecs.register(RotUnicode.search_function)

    def test_encoder_is_searchable_by_name(self):
        encoder = codecs.getencoder('rotunicode')
        self.assertIsNotNone(encoder)

    def test_decoder_is_searchable_by_name(self):
        decoder = codecs.getdecoder('rotunicode')
        self.assertIsNotNone(decoder)

    def test_search_function_returns_none_for_non_rotunicode_encoding(self):
        self.assertIsNone(RotUnicode.search_function('random'))

    @genty_dataset('ignore', 'replace', 'xmlcharrefreplace')
    def test_encoding_using_unsupported_error_types_raise_exception(
        self,
        error_type,
    ):
        with self.assertRaises(UnicodeError):
            'Hello World!'.encode('rotunicode', error_type)

    @genty_dataset('ignore', 'replace', 'xmlcharrefreplace')
    def test_decoding_using_unsupported_error_types_raise_exception(
        self,
        error_type
    ):
        with self.assertRaises(UnicodeError):
            'Hello World!'.decode('rotunicode', error_type)

    @genty_dataset(
        encode_zero_length_byte_string=(b'', str.encode, ''),
        decode_zero_length_byte_string=(b'', str.decode, ''),
        encode_zero_length_unicode_string=('', unicode.encode, ''),
        decode_zero_length_unicode_string=('', unicode.decode, ''),
        encode_byte_string=(b'Hello World!', str.encode, 'Ĥȅľľő Ŵőŕľď!'),
        decode_byte_string=(b'Ĥȅľľő Ŵőŕľď!', str.decode, 'Hello World!'),
        encode_unicode_string=('Hello World!', unicode.encode, 'Ĥȅľľő Ŵőŕľď!'),
        decode_unicode_string=('Ĥȅľľő Ŵőŕľď!', unicode.decode, 'Hello World!'),
        encode_byte_string_with_unsupported_chars=(
            b'हेलो World!',
            str.encode,
            'हेलो Ŵőŕľď!',
        ),
        decode_byte_string_with_unsupported_chars=(
            b'हेलो Ŵőŕľď!',
            str.decode,
            'हेलो World!',
        ),
        encode_unidcode_string_with_unsupported_chars=(
            'हेलो World!',
            unicode.encode,
            'हेलो Ŵőŕľď!',
        ),
        decode_unicode_string_with_unsupported_chars=(
            'हेलो Ŵőŕľď!',
            unicode.decode,
            'हेलो World!',
        ),
    )
    def test_operation_returns_correct_string(self, source, operation, target):
        self.assertEqual(
            target,
            operation(source, 'rotunicode'),
        )
