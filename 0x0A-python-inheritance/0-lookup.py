#!/usr/bin/python3
"""This module contains a function that prints
all the attributes of an object"""


def lookup(obj):
    """This function returns the attributes of an object

    Args:
        obj: the object

    Return: a list of all the attributes
    """

    return (dir(obj))
