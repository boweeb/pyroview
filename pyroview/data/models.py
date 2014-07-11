# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

"""
Created on Jul 07, 2014

@author: Jesse Butcher

"""

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean

from pyroview.data import DB_Base

__all__ = ['Configuration', 'User', 'Parameter', 'Geometry']


class Configuration(DB_Base):
    """ Configuration model
    """
    __tablename__ = "configuration"

    key = Column(String, primary_key=True)
    value = Column(String, nullable=False)
    description = Column(String)

    # Pretty print -- set blank str default for nullable fields
    def __str__(self):
        p_description = self.description if self.description is not None else ""
        props = [self.key,
                 self.value,
                 p_description]
        return "Config -- ({}|{}) \"{}\"".format(*props)

    def __repr__(self):
        props = [repr(self.key),
                 repr(self.value)]
        return "<Config: key={}, value={}>".format(*props)


class User(DB_Base):
    """ User model
    """
    __tablename__ = "user"

    user = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    hostname = Column(String)
    active = Column(Boolean, default=True, nullable=False)

    # Pretty print -- set blank str default for nullable fields
    def __str__(self):
        return "User -- {}".format(self.user)

    def __repr__(self):
        props = [repr(self.user),
                 repr(self.name),
                 repr(self.active)]
        return "<User: user={}, name={}, active={}>".format(*props)


class Parameter(DB_Base):
    """ Parameter model
    """
    __tablename__ = "parameter"

    id = Column(Integer, primary_key=True)
    parameter = Column(String, nullable=False)
    value = Column(String)
    description = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Pretty print -- set blank str default for nullable fields
    def __str__(self):
        p_value = self.value if self.value is not None else "<Empty>"
        props = [self.parameter,
                 p_value,
                 self.description]
        return "Parameter -- ({}|{}) \"{}\"".format(*props)

    def __repr__(self):
        props = [repr(self.parameter),
                 repr(self.value)]
        return "<Parameter: parameter={}, value={}>".format(*props)


class Geometry(DB_Base):
    """ Geometry model
    """
    __tablename__ = "geometry"

    name = Column(String, nullable=False)
    slug = Column(String(1), primary_key=True)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)

    # Pretty print -- set blank str default for nullable fields
    def __str__(self):
        props = [self.name,
                 self.slug,
                 self.width,
                 self.height]
        return "Geometry -- {} ({}): {}x{}".format(*props)

    def __repr__(self):
        props = [repr(self.slug),
                 repr(self.width),
                 repr(self.height)]
        return "<Geometry: slug={}, geometry='{}x{}'>".format(*props)
