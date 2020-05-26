#!/usr/bin/python3
"""
this text_indentation module contains only text_indentation()
"""


def text_indentation(text):
    """
    Print a text with 2 newlines after the characters: .?:
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    cont = False
    for x in text.strip(' '):
        if cont:
            cont = False
            continue
        if x in '.?:':
            print('{}\n\n'.format(x), end='')
            cont = True
        else:
            print(x, end='')
