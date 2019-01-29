# coding: utf-8

from __future__ import absolute_import, unicode_literals

import codecs
import platform

# pylint:disable=import-error,no-name-in-module
from genty import genty, genty_dataset
# pylint:enable=import-error,no-name-in-module
import six

from rotunicode import RotUnicode
# pylint:disable=wrong-import-order
from test.base_test_case import skipIf, TestCase
# pylint:enable=wrong-import-order


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

    @skipIf(six.PY3, 'Python 3 strings cannot be decoded.')
    @genty_dataset('ignore', 'replace', 'xmlcharrefreplace')
    def test_decoding_using_unsupported_error_types_raise_exception(
            self,
            error_type
    ):
        with self.assertRaises(UnicodeError):
            'Hello World!'.decode('rotunicode', error_type)

    @skipIf(
        not six.PY2 or platform.python_implementation() == 'PyPy',
        'Encoders must return bytes except in Python 2.',
    )
    @genty_dataset(
        zero_length_byte_string=(b'', ''),
        zero_length_unicode_string=('', ''),
        byte_string=(b'Hello World!', 'Ĥȅľľő Ŵőŕľď!'),
        unicode_string=('Hello World!', 'Ĥȅľľő Ŵőŕľď!'),
        byte_string_with_unsupported_chars=(
            'हेलो World!'.encode('utf-8'),
            'हेलो Ŵőŕľď!',
        ),
        unidcode_string_with_unsupported_chars=('हेलो World!', 'हेलो Ŵőŕľď!'),
    )
    def test_encode_returns_correct_string(self, source, target):
        self.assertEqual(
            target,
            source.encode('rotunicode'),
        )

    @skipIf(six.PY3, 'Python 3 strings cannot be decoded.')
    @genty_dataset(
        zero_length_byte_string=(b'', ''),
        zero_length_unicode_string=('', ''),
        byte_string=('Ĥȅľľő Ŵőŕľď!'.encode('utf-8'), 'Hello World!'),
        unicode_string=('Ĥȅľľő Ŵőŕľď!', 'Hello World!'),
        byte_string_with_unsupported_chars=(
            'हेलो Ŵőŕľď!'.encode('utf-8'),
            'हेलो World!',
        ),
        unicode_string_with_unsupported_chars=('हेलो Ŵőŕľď!', 'हेलो World!'),
    )
    def test_decode_returns_correct_string(self, source, target):
        self.assertEqual(
            target,
            source.decode('rotunicode'),
        )
