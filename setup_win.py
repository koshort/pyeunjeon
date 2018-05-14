#!/usr/bin/env python

import distutils.sysconfig
from setuptools import setup, Extension
import sys

if sys.maxsize > 2**32:
    ext_modules = [
        Extension(
            "_MeCab",
            ["MeCab_wrap.cxx",],
            include_dirs=["C:\Program Files\MeCab\sdk"],
            library_dirs=["C:\Program Files\MeCab\sdk"],
            libraries=["libmecab"]
        )
    ]
    data_files = [(distutils.sysconfig.get_python_lib(), ['C:\Program Files\MeCab\\bin\libmecab.dll'])]
else:
    ext_modules = [
        Extension(
            "_MeCab",
            ["MeCab_wrap.cxx",],
            include_dirs=["C:\Program Files (x86)\MeCab\sdk"],
            library_dirs=["C:\Program Files (x86)\MeCab\sdk"],
            libraries=["libmecab"]
        )
    ]
    data_files = [(distutils.sysconfig.get_python_lib(), ['C:\Program Files (x86)\MeCab\\bin\libmecab.dll'])]

setup(
    name="mecab-python-windows",
    version="0.996.0",
    py_modules=["MeCab"],
    ext_modules=ext_modules,
    data_files=data_files,
    author='Yukino Ikegami',
    author_email='yknikgm@gmail.com',
    platforms=['Windows'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: Microsoft',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing'
    ],
    description='Python wrapper for MeCab on Windows: Morphological Analysis engine',
    long_description='''This is a python wrapper for MeCab. It works on Windows.

    License
    ---------
    MeCab is copyrighted free software by Taku Kudo <taku@chasen.org> and Nippon Telegraph and Telephone Corporation, and is released under any of the GPL (see the file GPL), the LGPL (see the file LGPL), or the BSD License (see the file BSD).
    '''
)
