#!/usr/bin/python3
"""Reading module"""


def read_file(filename=""):
    """reads a text file"""
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
