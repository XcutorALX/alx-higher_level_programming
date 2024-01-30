#!/usr/bin/python3
"""This module defines a function that prints out a first and last name provided"""


def say_my_name(first_name, last_name=""):
    """This function prints a first and last name to stdout

    Args:
        first_name: a string representing a first name
        last_name: a string representing a last name

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is " + first_name + " " + last_name)
