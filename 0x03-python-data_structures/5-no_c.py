#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for x in range(len(my_string)):
        if my_string[x] != 'C' and my_string[x] != 'c':
            new_str += my_string[x]
    return new_str
