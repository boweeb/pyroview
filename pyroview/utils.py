# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

import os
import logging

from pyroview.logging import L

logging.basicConfig(level=L.level)


def dir_check(directory):
    """ Check if directory exists, if not then create it. """
    # http://stackoverflow.com/questions/273192/...
    #   python-best-way-to-create-directory-if-it-doesnt-exist-for-file-write

    logging.debug("Checking \"{}\" exists... ".format(directory))
    try:
        os.makedirs(directory)
        logging.warning("Configuration directory created.")
    except OSError:
        if not os.path.isdir(directory):
            raise
        logging.debug("Configuration directory exists.")
