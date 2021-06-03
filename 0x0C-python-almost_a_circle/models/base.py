#!/usr/bin/python3
"""base module"""


class Base:
    """number of constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initalize
        Args:
            id(int) = id attribute
        """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id
