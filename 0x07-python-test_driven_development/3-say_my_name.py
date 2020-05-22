#!/usr/bin/python3
"""
This say_my_name module contains only say_my_nmae()
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
