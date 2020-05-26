#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    def __str__(self):
        """Print Rectangle"""
        string = ''
        if self.__width is 0 or self.__height is 0:
            return string
        string += ('#' * self.__width + '\n') * self.__height
        return string[:-1]

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return Area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2
