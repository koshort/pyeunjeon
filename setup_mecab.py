#!/usr/bin/env python
from distutils.core import setup, Extension, os
import string
import sys

if sys.version > '3':

    def cmd1(strings):
        return os.popen(strings).readlines()[0][:-1]

    def cmd2(strings):
        return cmd1(strings).split()
else:

    def cmd1(strings):
        return os.popen(strings).readlines()[0][:-1]

    def cmd2(strings):
        return string.split(cmd1(strings))


setup(
    name="mecab-python",
    version=cmd1("mecab-config --version"),
    py_modules=["MeCab"],
    ext_modules=[
        Extension(
            "_MeCab",
            ["MeCab_wrap.cxx"],
            include_dirs=cmd2("mecab-config --inc-dir"),
            library_dirs=cmd2("mecab-config --libs-only-L"),
            libraries=cmd2("mecab-config --libs-only-l"))
    ])
