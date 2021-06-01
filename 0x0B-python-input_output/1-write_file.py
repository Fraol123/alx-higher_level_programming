#!/usr/bin/python3
"""my module"""


def write_file(filename="", text=""):
    """writes a text to a string file"""
    qoute = 'Holberton School is so cool!'

    with open("my_first_file.txt", "w", encoding="utf-8") as f:
        return (f.write(qoute))
