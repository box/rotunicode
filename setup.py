# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from setuptools import setup, find_packages
from os.path import dirname, join


def main():
    base_dir = dirname(__file__)
    setup(
        name='rotunicode',
        version='2.1.0',
        description='Python codec for converting between a string of ASCII '
                    'and non-ASCII chars maintaining readability',
        long_description=open(join(base_dir, 'README.rst')).read(),
        author='Kunal Parmar',
        author_email='oss@box.com',
        url='https://github.com/box/rotunicode',
        license=open(join(base_dir, 'LICENSE')).read(),
        packages=find_packages(exclude=['test']),
        test_suite='test',
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'rotunicode = rotunicode.console_scripts:main',
            ],
        },
    )


if __name__ == '__main__':
    main()
