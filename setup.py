# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup
from os.path import dirname, join


def main():
    setup(
        name='rotunicode',
        version='0.1.0',
        description='RotUnicode',
        long_description=open(join(dirname(__file__), 'README.md')).read(),
        author='Kunal Parmar',
        author_email='kunalparmar@gmail.com',
        packages=[b'rotunicode'],
        test_suite='test',
    )


if __name__ == '__main__':
    main()
