#!/usr/bin/python3
""" 100-my_int.py creates a rebellious MyInt() class """


class MyInt(int):
    """ MyInt is an int with == and != operators inverted """
    def __eq__(self, other):
        """ Check if two MyInt's are equal """
        return int(self) != int(other)

    def __ne__(self, other):
        """ Check if two MyInt's are inequal """
        return int(self) == int(other)
