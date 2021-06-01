#!/usr/bin/python3
"""my module"""


def append_write(filename="", text=""):
    """appends a text to a string file"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
