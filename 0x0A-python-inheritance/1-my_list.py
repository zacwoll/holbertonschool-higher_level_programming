#!/usr/bin/python3
""" 1-my_list.py MyList that inherits from list """


class MyList(list):
    """ MyList() subclass of List """
    def print_sorted(self):
        """prints the list but sorted (ascending)"""
        print(sorted(self))
