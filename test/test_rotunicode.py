# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
from unittest import TestCase

from box.util.rotunicode import RotUnicode


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

    def test_encoding_using_unsupported_error_types_raise_exception(self):
        with self.assertRaises(UnicodeError):
            'Hello World!'.encode('rotunicode', 'ignore')
        with self.assertRaises(UnicodeError):
            'Hello World!'.encode('rotunicode', 'replace')
        with self.assertRaises(UnicodeError):
            'Hello World!'.encode('rotunicode', 'xmlcharrefreplace')

    def test_decoding_using_unsupported_error_types_raise_exception(self):
        with self.assertRaises(UnicodeError):
            'Hello World!'.decode('rotunicode', 'ignore')
        with self.assertRaises(UnicodeError):
            'Hello World!'.decode('rotunicode', 'replace')
        with self.assertRaises(UnicodeError):
            'Hello World!'.decode('rotunicode', 'xmlcharrefreplace')

    def test_encoding_zero_length_byte_string_returns_zero_length_unicode_string(self):
        self.assertEqual(
            '',
            b''.encode('rotunicode'),
        )

    def test_decoding_zero_length_byte_string_returns_zero_length_unicode_string(self):
        self.assertEqual(
            '',
            b''.decode('rotunicode'),
        )

    def test_encoding_zero_length_unicode_string_returns_zero_length_unicode_string(self):
        self.assertEqual(
            '',
            ''.encode('rotunicode'),
        )

    def test_decoding_zero_length_unicode_string_returns_zero_length_unicode_string(self):
        self.assertEqual(
            '',
            ''.decode('rotunicode'),
        )

    def test_encoding_byte_string_returns_encoded_unicode_string(self):
        self.assertEqual(
            'Ĥȅľľő Ŵőŕľď!',
            b'Hello World!'.encode('rotunicode'),
        )

    def test_decoding_byte_string_returns_decoded_unicode_string(self):
        self.assertEqual(
            'Hello World!',
            b'Ĥȅľľő Ŵőŕľď!'.decode('rotunicode'),
        )

    def test_encoding_unicode_string_returns_encoded_unicode_string(self):
        self.assertEqual(
            'Ĥȅľľő Ŵőŕľď!',
            'Hello World!'.encode('rotunicode'),
        )

    def test_decoding_unicode_string_returns_decoded_unicode_string(self):
        self.assertEqual(
            'Hello World!',
            'Ĥȅľľő Ŵőŕľď!'.decode('rotunicode'),
        )

    def test_encoding_byte_string_with_unsupported_chars_returns_unicode_string_with_unsupported_chars_unchanged(self):
        self.assertEqual(
            'हेलो Ŵőŕľď!',
            b'हेलो World!'.encode('rotunicode'),
        )

    def test_encoding_unicode_string_with_unsupported_chars_returns_unicode_string_with_unsupported_chars_unchanged(self):
        self.assertEqual(
            'हेलो Ŵőŕľď!',
            'हेलो World!'.encode('rotunicode'),
        )

    def test_decoding_byte_string_with_unsupported_chars_returns_unicode_string_with_unsupported_chars_unchanged(self):
        self.assertEqual(
            'हेलो World!',
            b'हेलो Ŵőŕľď!'.decode('rotunicode'),
        )

    def test_decoding_unicode_string_with_unsupported_chars_returns_unicode_string_with_unsupported_chars_unchanged(self):
        self.assertEqual(
            'हेलो World!',
            'हेलो Ŵőŕľď!'.decode('rotunicode'),
        )
