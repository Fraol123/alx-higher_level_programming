#!/usr/bin/env python3
"""
removes all characters c and C from a string
"""


def no_c(my_string):

    new = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(new)
