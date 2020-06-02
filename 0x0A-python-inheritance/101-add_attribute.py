#!/usr/bin/python3
""" 101-add_attribute.py """


def add_attribute(self, key, value):
    """ adds attribute if possible to obj """
    if hasattr(self, '__dict__'):
        setattr(self, key, value)
    else:
        raise TypeError('can\'t add new attribute')
