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
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
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
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
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
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
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
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        This method computes and returns the area of
        Rectagle instance
        """
        return self.width * self.height

    def display(self):
        """
        This method prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.y):
            print()
        for row in range(self.height):
            print(" " * self.x, end='')
            for col in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """
        This method return the string representation
        of this instance.
        """
        result = (self.id, self.x, self.y, self.width, self.height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*result)
