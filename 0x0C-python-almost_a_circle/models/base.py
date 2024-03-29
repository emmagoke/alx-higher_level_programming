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
        name = cls.__name__
        if list_objs is None:
            output = []
        else:
            for obj in list_objs:
                output.append(obj.to_dictionary())
        with open(name + '.json', mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(output))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set.
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        else:
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances.
        """
        file_name = cls.__name__ + '.json'
        obj_list = []
        output = []
        try:
            with open(file_name, mode='r', encoding='utf-8') as f:
                obj_list = cls.from_json_string(f.read())
        except FileNotFoundError:
            return output
        for obj in obj_list:
            output.append(cls.create(**obj))
        return output
