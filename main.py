#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
===========================
pyroview
===========================

SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    TODO This describes how to use this script. This docstring
    will be printed by the script if there is an error or
    if the user requests help (-h or --help).

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    Jesse Butcher <boweeb@gmail.com>

LICENSE

    This script is in the public domain, free from copyrights or restrictions.

    Copyright (c) 2014, Jesse Butcher
    See LICENSE.txt

    ::

    This file is part of pyroview.

    VImPy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    VImPy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with VImPy.  If not, see <http://www.gnu.org/licenses/>.

VERSION

    0.5

"""

import sys
import traceback
import logging
from pyroview.config import get_cli_args
from pyroview.logging import L


logging.basicConfig(level=L.level)


def main(args):
    """
    :param args:
    :return:
    """

    # import pyroview
    from pyroview import data

    logging.debug('<<<Main>>>')

if __name__ == '__main__':
    try:
        # parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),
        #                                usage=globals()['__doc__'], version='0.5')
        # parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')

        ARGS = get_cli_args()
        logging.debug('CLI Arguments: {}'.format(ARGS))
        main(ARGS)

        sys.exit(0)
    except KeyboardInterrupt as e:
        # Ctrl-C
        raise e
    except SystemExit as e:
        # sys.exit()
        raise e
    except Exception as e:
        logging.error('ERROR, UNEXPECTED EXCEPTION')
        logging.error(str(e))
        traceback.print_exc()
        sys.exit(1)
