#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    if a_dictionary:
        return max(a_dictionary)
