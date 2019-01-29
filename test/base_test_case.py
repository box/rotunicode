# coding: utf-8

from __future__ import absolute_import, unicode_literals

from unittest import skipIf, TestCase  # pylint:disable=unused-import

import six

if six.PY3:
    # pylint:disable=no-member,maybe-no-member
    TestCase.assertItemsEqual = TestCase.assertCountEqual
