#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """class rectangle inherted from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """construct a rectangle class"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value to width"""
        self.__width = value

    @property
    def height(self):
        """get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value to height"""
        self.__height = value

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value to y"""
        self.__y = value

    @property
    def x(self):
        """get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value to x"""
        self.__x = value
