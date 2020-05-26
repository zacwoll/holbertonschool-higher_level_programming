#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Destroy Rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __str__(self):
        """Print Rectangle"""
        st = ''
        if self.__width is 0 or self.__height is 0:
            return string
        st += (str(self.print_symbol) * self.__width + '\n') * self.__height
        return st[:-1]

    def __repr__(self):
        """String Rectangle"""
        return ('Rectangle(' + str(self.__width) + ', ' +
                str(self.__height) + ')')

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the larger rectangle based on area."""
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
