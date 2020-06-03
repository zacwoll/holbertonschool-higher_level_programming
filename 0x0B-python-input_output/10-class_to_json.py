#!/usr/bin/python3
""" 10-class_to_json """


def class_to_json(obj):
    """ returns the dictionary description of JSON serialized object """
    return obj.__dict__
