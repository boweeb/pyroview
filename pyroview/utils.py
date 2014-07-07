# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

import os


def dir_check(directory):
    """ Check if directory exists, if not then create it. """
    # http://stackoverflow.com/questions/273192/...
    #   python-best-way-to-create-directory-if-it-doesnt-exist-for-file-write
    
    print("Checking \"{}\" exists... ".format(directory), end="")
    try: 
        os.makedirs(directory)
        print("False. Created directory.")
    except OSError:
        if not os.path.isdir(directory):
            raise
        print("True. Directory exists.")
