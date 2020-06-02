#!/usr/bin/python3
""" 4-inherits_from.py checks if obj inherits from a_class """


def inherits_from(obj, a_class):
    """ inherits_from checks if obj is a subclass of a_class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
