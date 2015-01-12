# coding: utf-8

from __future__ import unicode_literals
import codecs
from genty import genty, genty_dataset, genty_args

from rotunicode import RotUnicode, ruencode, rudecode
from test.base_test_case import TestCase


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
