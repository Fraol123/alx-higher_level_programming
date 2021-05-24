#!/usr/bin/python3
"""module that computes Area and perimeter"""


class Rectangle:
    """Represent a rectangle
      Attributes:
         number_of_instances(int) = counts how many instance of rectangles
         print_symbol = Used as symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intialize a rectangle
        Args:
             width(int): the width of the new rectangle.
             height(int): the height of the new rectangle.
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getters - get value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter- sets the value of width
        Args:
           value(int): the value to set the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter- gets value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: sets the value of height
        Args:
            value(int): the value to set to width
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns Area"""

        return (self.height * self.width)

    def perimeter(self):
        """Returns perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width + self.height) * 2)

    def __str__(self):
        """Return the printable reprresentation of a rectangle.
        represents the rectangle with # """

        new_str = ""
        if self.width == 0 or self.height == 0:
            return new_str

        else:
            for num in range(self.height):
                for rw in range(self.width):
                    new_str += str(self.print_symbol)
                if num != self.height - 1:
                    new_str += "\n"
            return new_str

    def __repr__(self):
        """Return the string representation of Rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """delates Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigest Rectangle besed on area

        Args:

            rect_1(Rectangle) = rectangle 1
            rect_2(Rectangle) = rectangle 2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
