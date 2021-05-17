#!/usr/bin/python3
"""dividing an intger"""


def safe_print_division(a, b):
    quo = 0
    try:
        quo = a / b
    except (ZeroDivisionError):
        quo = None
    finally:
        print("Inside result: {}".format(quo))
        return quo
