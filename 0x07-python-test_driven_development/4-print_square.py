#!/usr/bin/python3
"""
This module contains 
"""


def print_square(size):
    """
    This function prints a square of size size
    and using the symbol #
    Arguments:
        @size: The size of the square.
    """
    if type(size) not in [int, float]:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print("")
