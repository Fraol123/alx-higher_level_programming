#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    num = 0

    for i in range(len(roman_string)):
        if my_dict.get(roman_string[i], 0) == 0:
            return 0

        if (i != (len(roman_string) - 1) and
            my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]):
            num += my_dict[roman_string[i]] * -1
        else:
            num += my_dict[roman_string[i]]
    return (num)
