# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

import logging

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pyroview import DB
from pyroview.logging import L

logging.basicConfig(level=L.level)


# Global session registry:
session_factory = sessionmaker(autoflush=True, autocommit=False)
Session = scoped_session(session_factory)

# Base class for all of our model classes.
# Defined with SQLAlchemy's declarative extension.
DB_Base = declarative_base()

# Global metadata.
# The default metadata is the one from the declarative base.
db_metadata = DB_Base.metadata

# Import models.
from pyroview.data.models import *


#############################################################################
# Initialize engine.

def init_engine():
    """
    """
    try:
        logging.debug("Initializing... ")
        cx_str = ''
        if DB.c_engine == 'postgresql':
            cx_str = ('postgresql+psycopg2://' + DB.p_user +
                      ':' + DB.p_password +
                      '@' + DB.p_host +
                      ':' + DB.p_port +
                      '/' + DB.p_db_name
                      )
        elif DB.c_engine == 'mysql':
            cx_str = ('mysql://' + DB.m_user +
                      ':' + DB.m_password +
                      '@' + DB.m_host +
                      ':' + DB.m_port +
                      '/' + DB.m_schema
                      # + '?charset=utf8'
                      )
        elif DB.c_engine == 'sqlite':
            cx_str = 'sqlite+pysqlite:///' + DB.s_path
        else:
            pass
        logging.debug('[[ CX_STR ]]: {}'.format(cx_str))

        engine = create_engine(cx_str
                               # , echo=True
                               )
        # Session.configure(binds={Configuration: engine,
        #                          User: engine})
        db_metadata.bind = engine
        db_metadata.create_all()
        logging.debug("Success")
        return engine

    except exc.SQLAlchemyError as e:
        logging.error("SQLAlchemyError:: %s:" % e.args[0])
        return False
    except NameError as e:
        logging.error("NameError: {}".format(e))
        return False
    except ValueError as e:
        logging.error("There's something wrong with the database" +
                      " configuration. Likely the 'port' setting is wrong. {}".format(e))
        return False


#############################################################################
# Set global status of the engine being ready.

DB.ready = init_engine()

if DB.ready:
    logging.debug("Engine ready")
else:
    logging.debug("Engine NOT ready.")