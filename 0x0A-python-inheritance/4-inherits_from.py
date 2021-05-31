#!/usr/bin/python3
"""My module"""


def inherits_from(obj, a_class):
    """checks if it  inherited instance
      of the class
    Args:
         obj(any) = the object to check
         a_class(type) = the class to match the type with
    Return:
           True if the object is exactly an instance
           otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
