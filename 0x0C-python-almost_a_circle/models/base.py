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
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jasonfile:
            if list_objs is None:
                jasonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jasonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """json str to dict"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class initiated with attr alredy set
        Args:
           dictionary = key/value pair attribute to intialize
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns list of instance"""
        filname = cls.__name__ + '.json'
        new = []

        try:
            with open(filname) as f:
                content = f.read()

        except:
            return new

        json_file = Base.from_json_string(content)
        for obj in json_file:
            new.append(cls.create(**obj))
        return new
