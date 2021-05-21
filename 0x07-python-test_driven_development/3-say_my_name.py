#!/usr/bin/python3
"""This module prints people's names"""


def say_my_name(first_name, last_name=""):
    """This function will print names
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
