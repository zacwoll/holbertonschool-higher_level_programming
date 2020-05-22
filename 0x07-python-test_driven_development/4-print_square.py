#!/usr/bin/python3
"""
This '4-print_square' module contains only print_square()
"""


def print_square(size):
    """
    Prints a square using '#'
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    print(('#' * size + '\n') * size, end='')
