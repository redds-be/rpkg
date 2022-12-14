#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Actions taken in function of the options
"""

import sys
import logging
from actions.install import install
from actions.uninstall import uninstall


def take_action(argv):
    """ Checks what to do with arguments """
    if '-i' in argv:
        install(argv)
    if '-u' in argv:
        uninstall(argv)
    else:
        logging.error('Invalid arguments')
        sys.exit("\033[1;33mArgument not recognized use -h to print an help message.")
