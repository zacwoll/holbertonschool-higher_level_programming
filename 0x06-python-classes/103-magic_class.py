#!/usr/bin/python3
import math


class MagicClass:
    """Defines a MagicClass"""

    def __init__(self, radius=0):
        """Init MagicClass"""
        self.__radius = 0
        if type(radius) != int and type(radius != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

        def area(self):
            """Area"""
            return self.__radius ** 2 * math.pi

        def circumference(self):
            """Circumference"""
            return 2 * math.pi * self.__radius
