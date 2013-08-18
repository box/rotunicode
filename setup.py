# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup, find_packages
from os.path import dirname, join


def main():
    base_dir = dirname(__file__)
    setup(
        name='rotunicode',
        version='0.1.1',
        description='RotUnicode',
        long_description=open(join(base_dir, 'README.rst')).read(),
        author='Kunal Parmar',
        author_email='kunalparmar@gmail.com',
        url='https://pypi.python.org/pypi/rotunicode',
        license='Apache License 2.0',
        packages=find_packages(exclude=['test']),
        namespace_packages=[b'box'],
        test_suite='test',
        zip_safe=False,
    )


if __name__ == '__main__':
    main()
