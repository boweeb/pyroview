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

    TODO: Name <name@example.org>

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

    $Id$

"""

import sys
# import os
import traceback
import optparse
import time


def main():

    global options, args
    import pyroview
    from pyroview import data

    print('Hello world!')

if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(),
                                       usage=globals()['__doc__'], version='$Id$')
        parser.add_option('-v', '--verbose', action='store_true', default=False, help='verbose output')
        (options, args) = parser.parse_args()
        #if len(args) < 1:
        #    parser.error ('missing argument')
        if options.verbose:
            print(time.asctime())
        main()
        if options.verbose:
            print(time.asctime())
            print('TOTAL TIME IN MINUTES:',)
            print((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt as e:
        # Ctrl-C
        raise e
    except SystemExit as e:
        # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        sys.exit(1)
