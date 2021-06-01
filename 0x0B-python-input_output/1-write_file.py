#!/usr/bin/python3
"""my module"""


def write_file(filename="", text=""):
    """writes a text to a string file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
