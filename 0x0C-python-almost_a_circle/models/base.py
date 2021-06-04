#!/usr/bin/python3
"""base module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json str representation"""
        if not list_dictionaries:
            return []

        return json.dumps(list_dictionaries)
