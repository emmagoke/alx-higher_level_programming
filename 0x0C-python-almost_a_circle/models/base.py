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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function rites the JSON string representation of
        list_objs to a file.
        """
        output = []
        name = ''
        if list_objs is None:
            output = None
            name = cls.__class__.__name__
        else:
            name = list_objs[0].__class__.__name__
            for obj in list_objs:
                output.append(obj.to_dictionary())
        with open(name + '.json', mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(output))
