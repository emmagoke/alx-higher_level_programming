#!/usr/bin/python3
"""
This script contains the City class which inherit from the Base class.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
#  from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    The City class.
    args:
        id(Integer): The id of each row in the database
        name(String): The name of each city.
        state_id(Integer): A foreign key to the states Table
        state: This help in accessing the State Table
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    #  state = relationship('State', backref='cities')
