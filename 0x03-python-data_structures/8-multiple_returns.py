#!/usr/bin/python3
"""Returns length of string and its first charachter"""


def multiple_returns(sentence):

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
