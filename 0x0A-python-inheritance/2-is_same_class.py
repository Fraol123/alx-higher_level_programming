#!/usr/bin/python3
"""My module"""


def is_same_class(obj, a_class):
    """checks if it is exact the same

    Args:
         obj(any) = the object to check
         a_class(type) = the class to match the type with
    Return:
           True if the object is exactly an instance
           otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
