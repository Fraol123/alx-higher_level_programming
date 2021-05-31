#!/usr/bin/python3
"""Geomtrt module"""


class BaseGeometry:
    """empty geomtry module"""
    def area(self):
        """raises error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name(str)= the name of paramter
            value(int) = the parameter to validate"
        Return:
               TypeError = if the value is not int
                ValueError = if the value is less than zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
