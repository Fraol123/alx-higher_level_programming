#!/usr/bin/python3
"""json loading module"""
import json


def load_from_json_file(filename):
    """creats an object from json file"""
    with open(filename) as f:
        return json.load(f)
