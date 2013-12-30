# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import codecs
from unittest import TestCase

from box.util.rotunicode import RotUnicode, ruencode, rudecode


class RotUnicodeUtilsTest(TestCase):
    """Tests for :mod:`box.util.rotunicode.utils`."""

    @classmethod
    def setUpClass(cls):
        super(RotUnicodeUtilsTest, cls).setUpClass()
        codecs.register(RotUnicode.search_function)

    def test_ruencode_encodes_string_with_no_extension_using_rotunicode(self):
        self.assertEqual(
            'ҏľȁȉń',
            ruencode('plain'),
        )
        self.assertEqual(
            'ҏľȁȉń',
            ruencode('plain', extension=False),
        )
        self.assertEquals(
            '.ȅхƭȅńŝȉőń',
            ruencode('.extension'),
        )
        self.assertEquals(
            '.ȅхƭȅńŝȉőń',
            ruencode('.extension', extension=False),
        )

    def test_ruencode_encodes_string_skipping_extension_using_rotunicode(self):
        self.assertEqual(
            'ҏľȁȉń.txt',
            ruencode('plain.txt'),
        )
        self.assertEqual(
            'ҏľȁȉń.txt',
            ruencode('plain.txt', extension=False),
        )
        self.assertEquals(
            'ƭŵő.ȅхƭ.sions',
            ruencode('two.ext.sions'),
        )
        self.assertEquals(
            'ƭŵő.ȅхƭ.sions',
            ruencode('two.ext.sions', extension=False),
        )

    def test_ruencode_encodes_string_including_extension_using_rotunicode(self):
        self.assertEqual(
            'ҏľȁȉń.ƭхƭ',
            ruencode('plain.txt', extension=True),
        )
        self.assertEquals(
            'ƭŵő.ȅхƭ.ŝȉőńŝ',
            ruencode('two.ext.sions', extension=True),
        )

    def test_rudecode_decodes_string_using_rotunicode(self):
        self.assertEqual(
            'Hello World!',
            rudecode('Ĥȅľľő Ŵőŕľď!'),
        )
