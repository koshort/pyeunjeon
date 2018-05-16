"""
Eunjeon
=======

Eunjeon is a Korean morphological analysis project made on top of mecab.
This is python implementation of eunjeon with stand-alone installation functionality.
"""

from __future__ import absolute_import

import pkg_resources
import os

__title__ = 'eunjeon'
__author__ = 'nyanye'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2018 Nyanye'

try:
    __version__ = pkg_resources.get_distribution('eunjeon').version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"

installpath = os.path.dirname(os.path.realpath(__file__))

from eunjeon._mecab import Mecab
