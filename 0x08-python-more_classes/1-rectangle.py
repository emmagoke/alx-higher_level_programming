#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""


class Rectangle:
    """
    This is the Rectangle class.
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        """
        self.__width = width

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        """
        self.__height = height
