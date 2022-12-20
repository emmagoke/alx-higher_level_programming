#!/usr/bin/python3
"""
This Module contains the Square class
"""


class Square():
    """
    This is a Square class

    Args:
        size: A private attribute
    """
    __size = 3

    def __init__(self, size):
        """
        This creates an instance of the square class
        """
        self.__size = size
