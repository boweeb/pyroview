# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

import logging
import shlex

from pyroview import DB
from pyroview import data as d
from pyroview.logging import L

logging.basicConfig(level=L.level)


def get_config(session, args):
    """ Get application configuration """
    result_set = session.query(d.Configuration).all()
    keys = []
    values = []
    for item in result_set:
        keys.append(item.key)
        values.append(item.value)
    default_config_dict = dict(zip(keys, values))

    # Evaluate and apply defaults
    args_keys = set(args)
    defaults_keys = set(default_config_dict)
    total_keys = args_keys | defaults_keys
    logging.debug("[[ TOTAL_KEYS ]]: {}".format(total_keys))
    config_dict = dict.fromkeys(total_keys)
    for key in total_keys:
        if (key in args.keys()) and (args[key] is not None):
            config_dict[key] = args[key]
        else:
            if key in default_config_dict.keys():
                config_dict[key] = default_config_dict[key]
            else:
                # config_dict.pop(key)
                config_dict[key] = None

    logging.debug("[[ CONFIG_DICT ]]: {}".format(config_dict))

    config_list = []
    if config_dict['bin'] is not None:
        config_list.append(config_dict['bin'])
    if config_dict['host'] is not None:
        config_list.append(config_dict['host'])
    if config_dict['title'] is not None:
        config_list.extend(['-T', "\"{} {}\"".format(config_dict['title'], config_dict['host'])])
    if config_dict['user'] is not None:
        config_list.extend(['-u', config_dict['user']])
    if config_dict['no_admin'] is not None:
        if not config_dict['no_admin']:
            config_list.append('-0')

    logging.debug("[[ CONFIG_LIST ]]: {}".format(config_list))

    return config_list, config_dict


def get_parameters(session):
    """ Get rdesktop configuration """
    result_set = session.query(d.Parameter).filter(d.Parameter.active).order_by(d.Parameter.id).all()
    keys = []
    values = []
    for item in result_set:
        keys.append(item.id)
        values.append((item.parameter, item.value))
    parameter_dict = dict(zip(keys, values))
    parameter_list = []
    for key in parameter_dict.keys():
        parameter_list.append("-{}".format(parameter_dict[key][0]))
        if parameter_dict[key][1] is not None:
            parameter_list.append(parameter_dict[key][1])
    logging.debug("[[ PARAMETER_LIST ]]: {}".format(parameter_list))
    return parameter_list


def get_geometry(session, config_dict):
    """
    Get geometry
    :param session:
    :param config_dict:
    :return:
    """

    slug = config_dict['display']
    geometry = session.query(d.Geometry).filter(d.Geometry.slug == slug).first()

    cmd_list = ["-g", "{}x{}".format(geometry.width, geometry.height)]

    return cmd_list


def get_user(session, config_dict, method):
    """

    :param session:
    :param config_dict:
    :return:
    """

    result = None
    qry = session.query(d.User).order_by(d.User.user)
    if method == 'by_user':
        result = qry.filter(d.User.user == config_dict['user']).first()
    elif method == 'by_host':
        result = qry.filter(d.User.hostname == config_dict['host']).first()

    if result is not None:
        user = ['-u', result.user,
                '-p', result.password]
        logging.debug("\n>>>{}\n>>>{}".format(user, result.hostname))
        return user, result.hostname
    else:
        return False


def create_cmd(args):
    """

    :return:
    """

    if not DB.ready:
        logging.error("Engine not ready")
        return False

    session = d.Session()

    config_list, config_dict = get_config(session, args)
    parameter_list = get_parameters(session)
    geometry = get_geometry(session, config_dict)

    if (args['host'] is None) and (args['user'] is not None):
        logging.debug("======>HOST is None")
        user, host = get_user(session, config_dict, "by_host")
        config_list.remove(config_dict['user'])
        # logging.debug("\n>>>{}\n>>>{}".format(user, host))
    elif (args['user'] is None) and (args['host'] is not None):
        logging.debug("======>USER is None")
        user, host = get_user(session, config_dict, "by_user")
        config_list.remove(config_dict['host'])
        # logging.debug("\n>>>{}\n>>>{}".format(user, host))
        config_list.append(host)
    elif (args['host'] is not None) and (args['user'] is not None):
        logging.debug("======>NEITHER is None")
        pass
    elif (args['host'] is None) and (args['user'] is None):
        logging.debug("======>BOTH are None")
        pass
    else:
        logging.debug("======>WTF")
        raise AttributeError

    # Build command
    cmd = []
    cmd.extend(config_list)
    cmd.extend(parameter_list)
    cmd.extend(geometry)
    # logging.debug("[[ CMD LIST ]]: {}".format(cmd))

    return cmd