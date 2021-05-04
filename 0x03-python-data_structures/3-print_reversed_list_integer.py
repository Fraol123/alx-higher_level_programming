#!/usr/bin/python3
"""
reverse int
"""


def print_reversed_list_integer(my_list=[]):

        if my_list:
                my_list.reverse()
                for x in my_list:
                        print("{}".format(x))
