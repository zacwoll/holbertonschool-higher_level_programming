#!/usr/bin/python3
""" 12-student.py """


class Student:
    """ A Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves attributes os Student """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ Reload attributes from json """
        for k, v in json.items():
            setattr(self, k, v)
