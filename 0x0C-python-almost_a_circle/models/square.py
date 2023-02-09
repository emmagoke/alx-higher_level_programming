#!/usr/bin/python3
"""
This Module contains the python class Square
that inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class that has following attribute:

    attributes:
        size
        x
        y
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This method is called when the instance of the
        class square is created.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This method returns the string representation
        of the instance of this class
        """
        args = (self.id, self.x, self.y, self.width)
        return "[Square] ({}) {}/{} - {}".format(*args)
