#!/usr/bin/python3
"""
This module contain the Square class that
inherits from the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is the Square class.
    """

    def __init__(self, size):
        """
        This method is called when a Square object
        is created.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        This method compute the area of the square object
        """
        return self.__size * self.__size

    def __str__(self):
        """
        This function returns the string representation
        of the Square class
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
