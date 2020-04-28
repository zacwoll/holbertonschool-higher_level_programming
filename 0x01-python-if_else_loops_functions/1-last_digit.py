#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "and is 0"
if number % 10 > 5:
    str = "and is greater than 5"
elif number % 10 < 6 and number % 10 != 0:
    str = "and is less than 6 and not 0"
print("Last digit of {0} is {1} {2}".format(number, number % 10, str))
