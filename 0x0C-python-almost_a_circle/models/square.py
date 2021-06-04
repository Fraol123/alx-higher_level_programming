#!/usr/bin/python3
"""square defination"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of a square"""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """set value of size"""
        self.width = value
        self.height = value
