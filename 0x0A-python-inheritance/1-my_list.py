#!/usr/bin/python3
"""module for sorting"""


class MyList(list):
    """sub class of list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
