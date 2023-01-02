#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""


class Rectangle:
    """
    This is the Rectangle class.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This method returns the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        This method sets the width attribute to only integer.
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        """
        This method returns the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        This methods sets the height attribute to integers only.
        """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
