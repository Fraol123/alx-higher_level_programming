#!/usr/bin/python3
"""my module"""


class Student:
    """class of student"""

    def __init__(self, first_name, last_name, age):
        """initalizing parameters
        Args:
            first_name(str) = first given name of student
            last_name(str) = last name of  student
            age(int) = age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation of student
        Args:
        attrs(list) = attribute too represent
        """
        if (type(attrs) == list and all(
                type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
