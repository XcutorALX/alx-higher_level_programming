#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    i = 0
    number = 0
    values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    while i < len(roman_string):
        if i < len(roman_string) - 1 and \
        (values[roman_string[i]] < values[roman_string[i + 1]]):
            number += values[roman_string[i + 1]] - values[roman_string[i]]
            i += 1
        else:
            number += values[roman_string[i]]

        i += 1
    return number
