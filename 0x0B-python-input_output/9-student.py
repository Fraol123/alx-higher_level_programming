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

    def to_json(self):
        """dict representation of student"""
        return self.__dict__
