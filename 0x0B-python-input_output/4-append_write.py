#!/usr/bin/python3
""" 4-append_write """


def append_write(filename="", text=""):
    """ append to a file """
    with open(filname, 'a') as f:
        return f.write(text)
