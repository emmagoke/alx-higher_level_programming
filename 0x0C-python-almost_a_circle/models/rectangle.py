#!/usr/bin/python3
"""
This module contains the rectangle class
"""
from .base import Base


class Rectangle(Base):
    """
    This is the Rectangle class
    Args:
        width
        height
        x
        y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This method is called when an object of
        the class Rectangle is created.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        This method gets the width private attritube.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        This method sets the width private attribute.
        """
        self.__width = width
    
    @property
    def height(self):
        """
        This method gets the height private attribute.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        This method sets the height private attribute.
        """
        self.__height = height

    @property
    def x(self):
        """
        This method gets the x private attribute.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        This method sets the y private attribute.
        """
        self.__x = x

    @property
    def y(self):
        """
        This method gets the y private attribute.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        This method sets the y private attribute.
        """
        self.__y = y

