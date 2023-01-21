#!/usr/bin/python3
"""
This module contains the Base Class
"""


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
