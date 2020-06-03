#!/usr/bin/python3
""" 11-student.py """


class Student:
    """ A Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieve the __dict__ of Student """
        return self.__dict__
