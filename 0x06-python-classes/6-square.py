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

    def __init__(self, size=0, position=(0, 0)):
        """
        This creates an instance of the square class
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns: The value of position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the value of 'position'
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        This method prints in stdout the square with the character '#'
        """
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print("")
            for i in range(self.size):
                for y in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end="")
                print()

    def area(self):
        """
        Returns:
            The area of the square of size
        """
        return (self.__size * self.__size)
