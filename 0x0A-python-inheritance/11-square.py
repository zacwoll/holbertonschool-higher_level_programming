#!/usr/bin/python3
""" 8-rectangle.py creates a Rectangle from BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square inherits from Rectangle """
    def __init__(self, size):
        """ init """
        self.integer_validator("size", size)
        self.__size = size

    def __repr__(self):
        """ prints a Square """
        return '[Square] {}/{}'.format(self.__size, self.__size)

    def area(self):
        """ Area of Square """
        return self.__size ** 2
