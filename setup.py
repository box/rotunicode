# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup, find_packages
from os.path import dirname, join


def main():
    setup(
        name='rotunicode',
        version='0.1.0',
        description='RotUnicode',
        long_description=open(join(dirname(__file__), 'README.md')).read(),
        author='Kunal Parmar',
        author_email='kunalparmar@gmail.com',
        packages=find_packages(exclude=['test']),
        namespace_packages=[b'box'],
        test_suite='test',
        zip_safe=False,
    )


if __name__ == '__main__':
    main()
