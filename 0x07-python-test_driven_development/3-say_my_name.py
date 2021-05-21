#!/usr/bin/python3

"""Define a name printing function"""


def say_my_name(first_name, last_name=""):
    """print a name.

    Args:
       first_name(str): the first name to be printed
       last_name(str): last name to be printed.

    Raises:
          TypeError: if either of them are not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
