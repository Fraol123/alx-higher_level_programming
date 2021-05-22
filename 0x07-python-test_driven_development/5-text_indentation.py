#!/usr/bin/python3
"""text indetaion Module"""


def text_indentation(text):
    """prints 2 new line after each . ? or : charachter in a string

    Args:
        text(str): the text to perform the operation on
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    wild = ['.', '?', ':']
    new_text = ""
    for letter in text:
        new_text += letter
        if letter in wild:
            new_text += "\n"
            print(new_text.strip(" "))
            new_text = ""
    if letter not in wild:
        print(new_text.strip(" "), end="")
