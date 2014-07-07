# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from pyroview import DB


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
from pyroview.data.models import Configuration
from pyroview.data.models import User


#############################################################################
# Initialize engine.

def init_engine():
    """
    """
    if DB.password != "":
        try:
            print("Initializing... ", end="")
            cx_str = ('postgresql+psycopg2://' + DB.user +
                      ':' + DB.password +
                      '@' + DB.host +
                      ':' + DB.port +
                      '/' + DB.db_name
                      # + '?charset=utf8'
                      )
            # print(cx_str)
            engine = create_engine(cx_str
                                   , echo=True
                                   )
            # Session.configure(binds={Configuration: engine,
            #                          User: engine})
            db_metadata.bind = engine
            db_metadata.create_all()
            print("Success")
            return engine

        except exc.SQLAlchemyError as e:
            print("SQLAlchemyError:: %s:" % e.args[0])
            return False
        except NameError as e:
            print("NameError: {}".format(e))
            return False
        except ValueError as e:
            print("There's something wrong with the database" +
                  " configuration. Likely the 'port' setting is wrong. {}".format(e))
            return False

    else:
        print("The password cannot be blank.")
        return False

#############################################################################
# Set global status of the engine being ready.

DB.ready = init_engine()

if DB.ready:
    print("Engine ready")
else:
    print("Engine NOT ready.")