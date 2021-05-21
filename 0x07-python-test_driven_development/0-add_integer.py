#!/usr/bin/python3
"""Define an integer addition function"""


def add_integer(a, b=98):
    """ return the addition of  a and b.

    flot must be first casted to integers

    raises:
           TypeError: if either of a and b ae non-integer & n0n-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
