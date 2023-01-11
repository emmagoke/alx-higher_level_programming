#!/usr/bin/python3
"""
This module contains the Student class
"""


class Student:
    """
    This is the Student Class
    """

    def __init__(self, first_name, last_name, age):
        """
        This method is called when an Instance of Student
        is created.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrieves a dictionary representation
        of a Student instance
        """
        if attrs is None:
            out = self.__dict__
        else:
            out = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    out[key] = value
        return out

    def reload_from_json(self, json):
        """

        """
        self.__dict__ = json
