#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for x in my_list:
        if x > max:
            max = x
    return max

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
