# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from codecs import open   # pylint:disable=redefined-builtin
from os.path import dirname, join

from setuptools import setup, find_packages


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Operating System :: OS Independent',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
]


def main():
    base_dir = dirname(__file__)
    test_requirements = ['genty>=1.0.0']
    test_suite = 'test'
    with open(join(base_dir, 'README.rst'), encoding='utf-8') as readme_file:
        long_description = readme_file.read()
    setup(
        name='rotunicode',
        version='2.3.0',
        description='Python library for converting between a string of ASCII '
                    'and non-ASCII chars maintaining readability',
        long_description=long_description,
        author='Box',
        author_email='oss@box.com',
        url='https://github.com/box/rotunicode',
        license=(
            'Apache Software License, Version 2.0, '
            'http://www.apache.org/licenses/LICENSE-2.0'
        ),
        packages=find_packages(exclude=['test']),
        install_requires=['six>=1.9.0'],
        tests_require=test_requirements,
        test_suite=test_suite,
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'rotunicode = rotunicode.console_scripts:main',
            ],
        },
        classifiers=CLASSIFIERS,
    )


if __name__ == '__main__':
    main()
