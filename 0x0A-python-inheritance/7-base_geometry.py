#!/usr/bin/python3
""" 6-base_geometry.py enhances BaseGeometry class """


class BaseGeometry():
    """ BaseGeometry class definition """
    def area(self):
        """ area not implemented, raise exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates values """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
