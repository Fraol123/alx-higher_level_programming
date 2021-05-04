#!/usr/bin/python3
"""
reverse int
"""


def print_reversed_list_integer(my_list=[]):

        if not my_list:
                return None
        for x in my_list[::-1]:
                print("{:d}".format(x))
