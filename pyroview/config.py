# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""
import logging
import configparser
import os

from pyroview.utils import dir_check
from pyroview.logging import L
logging.basicConfig(level=L.level)


def safe_init(caller, parser, global_var, section, option):
    """ Safely init variables, trapping parser errors. """
    # Goal (example):
    # self.src_host = self.config.get("db_src", "host")

    # The loop structure causes a *retry* after exception.
    while True:
        try:
            if not parser.has_section(section):
                parser.add_section(section)
            setattr(caller, global_var, parser.get(section, option))
        except configparser.NoOptionError as e:
            logging.error("Encountered an un-configured option. {}".format(e))
            parser.set(section, option, "Fill me.")
            continue
        break


def safe_init_dict_wrapper(caller, parser, option_array):
    """ High level option loader that parses a dictionary of options """
    o = option_array
    logging.debug("Parsing {} option section(s): {}... ".format(len(o), o.keys()))
    for s in o.keys():
        if o[s]['type'] == 'database':
            section = 'database'
            for field in o[s]['fields']:
                global_var = field
                safe_init(caller, parser, global_var, section, field)
    logging.debug("Done.")


class DatabaseConnection():
    def __init__(self):
        self.app_dir = os.path.join(os.path.expanduser("~"), ".pyroview")
        dir_check(self.app_dir)

        self.config_file = os.path.join(self.app_dir, "database_connection.cfg")

        self.config = configparser.ConfigParser()

        if not os.path.exists(self.config_file):
            logging.warning("Config file missing. Initializing new, blank one.")
            with open(self.config_file, "w") as fp:
                fp.write("[database]\n" +
                         "host = \n" +
                         "user = \n" +
                         "password = \n" +
                         "port = \n" +
                         "db_name = \n")

        self.config.read(self.config_file)

        self.ready = False

        option_array = {
            'DB': {
                'type': 'database',
                'fields': (
                    'host',
                    'user',
                    'password',
                    'port',
                    'db_name'
                )
            }
        }
        safe_init_dict_wrapper(self, self.config, option_array)
