#!/usr/bin/python3
"""Represent a Square Object with a __repr__ toString"""


class Square:
    """A Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Init"""
        self.__size = size
        self.__position = position

    def __repr__(self):
        """Square toString"""
        to_str = ''
        if self.__size == 0:
            to_str += '\n'
        else:
            to_str += ('\n' * self.__position[1])
            for i in range(self.__size):
                to_str += (' ' * self.__position[0])
                to_str += ('#' * self.__size + '\n')
        return to_str[:-1]

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

    @property
    def position(self):
        """gets the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position"""
        if type(value) != tuple or len(value) != 2 or \
                not all(type(x) == int and x >= 0 for x in a):
                    raise TypeError('position must be a \
                            tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
