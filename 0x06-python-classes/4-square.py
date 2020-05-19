#!/usr/bin/python3
class Square:
    """A Square"""

    def __init__(self, size=0):
        """Init"""
        self.__size = size

    @property
    def size(self):
        """gets the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of Square"""
        return self.__size ** 2
