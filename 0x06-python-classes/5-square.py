#!/usr/bin/python3
"""Prints a representation of a Square Class"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Init"""
        self.__size = size

    @property
    def size(self):
        """Size Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of Square"""
        return self.__size ** 2

    def my_print(self):
        """Square Print"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
                print(self.__size * "#")
