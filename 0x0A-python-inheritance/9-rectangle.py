#!/usr/bin/python3
"""
This module contains the Rectangle class
that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The Rectangle class
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        This method calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        This method returns the string representation
        of the Rectangle class
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
