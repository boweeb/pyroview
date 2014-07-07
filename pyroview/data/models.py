# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean

from pyroview.data import DB_Base


class Configuration(DB_Base):
    """ Configuration model
    """
    __tablename__ = "configuration"

    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)
    description = Column(String)


class User(DB_Base):
    """ User model
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    hostname = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)


class Parameter(DB_Base):
    """ Parameter model
    """
    __tablename__ = "parameter"

    id = Column(Integer, primary_key=True)
    parameter = Column(String, nullable=False)
    value = Column(String, nullable=False)
    description = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)


class Geometry(DB_Base):
    """ Geometry model
    """
    __tablename__ = "geometry"

    name = Column(String, nullable=False)
    slug = Column(String(1), primary_key=True)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
