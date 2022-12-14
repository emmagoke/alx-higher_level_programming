#!/usr/bin/python3
"""
This Module contains the Square class
"""


class Square():
    """
    This is a Square class

    Args:
        size (integer): A private attribute
    """
    __size = 3

    def __init__(self, size=0):
        """
        This creates an instance of the square class
        """
        self.size = size

    @property
    def size(self):
        """
        Returns: The Value of size (getter for size)
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        This method sets the value of size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns:
            The area of the square of size
        """
        return (self.__size * self.__size)
