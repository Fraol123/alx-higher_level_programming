#!/usr/bin/python3
""" My Square Module"""


def print_square(size):
    """ Prints a square based on the argument size
    Args:
        size (int): Size of the square to be printed
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for row in range(size):
            print("#"*size)
