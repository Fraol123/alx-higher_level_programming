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

    def update(self, *args, **kwargs):
        """update square with key word arg"""
        attribute = ['id', 'size', 'size', 'x', 'y']

        for i, x in enumerate(args):
            if i >= len(attribute):
                return

            self.__setattr__(attribute[i], x)

        if args:
            return

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def to_dictionary(self):
        """dict representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
