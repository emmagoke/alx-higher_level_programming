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

    @property
    def size(self):
        """
        Returns the value of size
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        This method sets the value od size
        """
        if type(size) != int:
            raise TypeError('width must be an integer')
        if size <= 0:
            raise ValueError('width must be > 0')
        self.width, self.height = size, size

    def update(self, *args, **kwargs):
        """
        This method update the attributes (id, size, 
        x, y) of the Square class.
        """
        len_args = len(args)
        if args is not None and len_args != 0:
            list_id = ['id', 'size', 'x', 'y']
            for i in range(len_args):
                setattr(self, list_id[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        This method returns the string representation
        of the instance of this class
        """
        args = (self.id, self.x, self.y, self.width)
        return "[Square] ({}) {}/{} - {}".format(*args)
