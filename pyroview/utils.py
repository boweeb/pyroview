# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""
import argparse

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


def get_cli_args():
    """

    :return:
    """
    # parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),
    #                                usage=globals()['__doc__'], version='0.5')
    # parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')

    parser = argparse.ArgumentParser(description="Description x"
                                     , usage=globals()['__doc__']
                                     )
    parser.add_argument('-U', '--user', help='Username')
    parser.add_argument('-H', '--host', help='Hostname')
    parser.add_argument('-P', '--password', help='Password')
    parser.add_argument('-N', '--no-admin', help='Administrator mode', action='store_true', default=False)
    parser.add_argument('-D', '--display', help='Geometry of display')
    parser.add_argument('-T', '--title', help='Window title prefix')
    parser.add_argument('-d', '--debug', help='Dry run and display rdesktop command', action='store_true', default=False)
    args = vars(parser.parse_args())

    return args