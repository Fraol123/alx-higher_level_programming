#!/usr/bin/python3


def max_integer(my_list=[]):

    if len(my_list) == "":
        return None

    large = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > large:
            large = my_list[i]
    return (large)
