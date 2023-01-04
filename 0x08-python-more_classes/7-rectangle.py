#!/usr/bin/python3
"""
This module contains the Rectangle class.
"""


class Rectangle:
    """
    This is the Rectangle class.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        This method is called when an instance is created.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        This method calculate the area of a rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        This method calculate the perimeter of a rectangle.
        """
        if (self.width == 0) or (self.height == 0):
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        """
        This method return the informal string representation
        when the class is printed.
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string += str(self.print_symbol)
                string += '\n'
            return string[:-1]

    def __repr__(self):
        """
        This method return a string representation of the rectangle to
        be able to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        This method is called when an instance is delected.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
