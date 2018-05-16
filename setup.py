# -*- coding: utf-8 -*-

import os
import sys
import string
import platform
import distutils.sysconfig as config
from setuptools import find_packages, setup, Extension


__version__ = '0.3.9.5'

system = platform.system()
data_files = None
extension = []
package_data = {
    'eunjeon': [
        'data/mecab-ko-dic/*',
        'data/*.cxx'
        ]
}


def requirements():
    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if system == "Windows":
        return _openreq('requirements-win.txt')
    else:
        return _openreq('requirements.txt')


if system == "Windows":
    # Experimental stand-alone extension and data_files
    extension = [
        Extension(
            "_MeCab",
            ["eunjeon/MeCab_wrap.cxx",],
            include_dirs=["eunjeon/data/sdk"],
            library_dirs=["eunjeon/data/sdk"],
            libraries=["libmecab"]
        )
    ]
    package_data['eunjeon'].append('data/*')
    package_data['eunjeon'].append('data/sdk/*')

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
    url='https://github.com/koshort/pyeunjeon',
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
    package_data=package_data,
    data_files=data_files,
    license='GPL v3+',
    ext_modules=extension,
    platforms=["Windows", "Linux", "Mac"],
    packages=find_packages(),
    install_requires=requirements())