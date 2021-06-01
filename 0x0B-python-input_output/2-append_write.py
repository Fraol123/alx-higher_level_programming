#!/usr/bin/python3
"""my module"""


def append_write(filename="", text=""):
    """appends a text to a string file"""
    qoute = 'Holberton School is so cool!\n'

    with open("file_append.txt", "a", encoding="utf-8") as f:
        return (f.write(qoute))
