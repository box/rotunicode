# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from sys import version_info
from setuptools import setup, find_packages
from os.path import dirname, join


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
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
    if version_info[0] == 2 and version_info[1] == 6:
        test_requirements.append('unittest2')
        test_suite = 'unittest2.collector'
    setup(
        name='rotunicode',
        version='2.2.0',
        description='Python library for converting between a string of ASCII '
                    'and non-ASCII chars maintaining readability',
        long_description=open(join(base_dir, 'README.rst')).read(),
        author='Box',
        author_email='oss@box.com',
        url='https://github.com/box/rotunicode',
        license=open(join(base_dir, 'LICENSE')).read(),
        packages=find_packages(exclude=['test']),
        install_requires=['six'],
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
