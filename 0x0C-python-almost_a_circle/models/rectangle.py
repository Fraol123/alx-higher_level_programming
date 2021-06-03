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
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value to height"""
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value to y"""
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    @property
    def x(self):
        """get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value to x"""
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    def area(self):
        """returns the area of rec"""
        return self.width * self.height

    def display(self):
        """ display # in rectangle form"""
        for i in range(self.width):
            for j in range(self.height):
                print('#', end='')
            print()
