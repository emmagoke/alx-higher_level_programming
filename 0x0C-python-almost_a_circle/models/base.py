#!/usr/bin/python3
"""
This module contains the Base Class
"""
import json


class Base:
    """
    This is the Base classs.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This methods is called when a
        new object of the Base Class is created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
