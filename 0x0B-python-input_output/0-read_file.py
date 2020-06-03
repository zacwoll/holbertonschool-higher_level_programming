#!/usr/bin/python3
""" 0-read_file """


def read_file(filename=""):
    """ Print the contents of a txt file """
    with open(filename, 'r') as f:
        print(f.read(), end="")
