#!/usr/bin/python3
"""
This function contains the BaseGeometry class
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.
    """

    def area(self):
        """
        This is the area method.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        This mathod validates an value which must be
        an Integer.
        ars:
            name: A string
            value: must be an integer greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
