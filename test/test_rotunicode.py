# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
from unittest import TestCase

from box.util.rotunicode import RotUnicode


class RotUnicodeTest(TestCase):

    codecs.register(RotUnicode.search_function)

    def test_encoder_is_searchable_by_name(self):
        encoder = codecs.getencoder('rotunicode')
        self.assertIsNotNone(encoder)

    def test_decoder_is_searchable_by_name(self):
        decoder = codecs.getdecoder('rotunicode')
        self.assertIsNotNone(decoder)

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
