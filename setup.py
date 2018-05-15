# -*- coding: utf-8 -*-

import os
import sys
import string
import platform
import distutils.sysconfig
from setuptools import find_packages, setup, Extension


__version__ = '0.3.9.1'

system = platform.system()
data_files = None
extension = []


def requirements():
    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if system == "Windows":
        return _openreq('requirements-win.txt')
    else:
        return _openreq('requirements.txt')


if system == "Windows":
    if sys.maxsize > 2**32:
        extension = [
            Extension(
                "_MeCab",
                ["eunjeon/MeCab_wrap.cxx",],
                include_dirs=["C:\\Program Files\\MeCab\\sdk"],
                library_dirs=["C:\\Program Files\\MeCab\\sdk"],
                libraries=["libmecab"]
            )
        ]
        data_files = [(distutils.sysconfig.get_python_lib(), ['C:\\Program Files\\MeCab\\bin\\libmecab.dll'])]
    else:
        extension = [
            Extension(
                "_MeCab",
                ["eunjeon/MeCab_wrap.cxx",],
                include_dirs=["C:\\Program Files (x86)\\MeCab\\sdk"],
                library_dirs=["C:\\Program Files (x86)\\MeCab\\sdk"],
                libraries=["libmecab"]
            )
        ]
        data_files = [(distutils.sysconfig.get_python_lib(), ['C:\\Program Files (x86)\\MeCab\\bin\\libmecab.dll'])]

else:
    def cmd1(strings):
        return os.popen(strings).readlines()[0][:-1]

    if sys.version > '3':
        def cmd2(strings):
            return cmd1(strings).split()
    else:
        def cmd2(strings):
            return string.split(cmd1(strings))

    extension = [Extension(
        "_MeCab",
        ["eunjeon/MeCab_wrap.cxx"],
        include_dirs=cmd2("mecab-config --inc-dir"),
        library_dirs=cmd2("mecab-config --libs-only-L"),
        libraries=cmd2("mecab-config --libs-only-l")
    )]


setup(
    name='eunjeon',
    version=__version__,
    description='Python interface for eunjeon project & mecab based morphological analyzer.',
    url='https://github.com/koshort/peunjeon',
    author='nyanye',
    author_email='iam@nyanye.com',
    keywords=['Korean', 'CJK',
              'NLP', 'natural language processing',
              'CL', 'computational linguistics',
              'tagging', 'tokenizing', 'linguistics', 'text analytics'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        ],
    entry_points={
        'console_scripts': [],
    },
    package_data={'eunjeon': [
        'mecab-ko-dic/*',
    ]},
    data_files=data_files,
    license='GPL v3+',
    ext_modules=extension,
    packages=find_packages(),
    install_requires=requirements())