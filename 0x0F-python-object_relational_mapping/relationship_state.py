#!/usr/bin/python3
"""
This python file contains the class definition of a State
and an instance Base = declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """
    This is the State class.
    args:
        id(Integer) - The id of the states
        name(String) - The name of the states.
        cities: This connects the State to the City Table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=True)
    cities = relationship("City", backref='state', cascade="all, delete")
