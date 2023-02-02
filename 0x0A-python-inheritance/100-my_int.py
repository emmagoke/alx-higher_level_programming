#!/usr/bin/python3
"""
This module contains MyInt class
that inherits from the int class.
"""


class MyInt(int):
    """
    MyInt class
    """

    def __eq__(self, other):
        """
        This method handle the equal to(==) in 
        reverse other
        """
        return self.real != other

    def __ne__(self, other):
        """
        This method handle the not equal(!=)
        in reverse other.
        """
        return self.real == other
