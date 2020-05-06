#!/usr/bin/python3
def no_c(my_string):
    ret_str = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            ret_str += x
    return ret_str
