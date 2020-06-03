#!/usr/bin/python3
''' 1-number_of_lines '''


def number_of_lines(filename=""):
    """ Read file, return number of lines """
    with open(filename, 'r') as f:
        return len(f.readlines())
