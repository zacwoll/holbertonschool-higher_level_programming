#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __del__(self):
        """Destroy Rectangle"""
        print('Bye rectangle...')
        self.__class__.number_of_instances -= 1

    def __str__(self):
        """Print Rectangle"""
        string = ''
        if self.__width is 0 or self.__height is 0:
            return string
        string += ('#' * self.__width + '\n') * self.__height
        return string[:-1]

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

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
