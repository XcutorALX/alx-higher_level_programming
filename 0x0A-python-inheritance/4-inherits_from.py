#!/usr/bin/python3
"""This module contains an object comparing function"""


def inherits_from(obj, a_class):
    """This function checks if an object is an instance or subclass

    Args:
        obj: the object to check
        a_class: the class to compare with

    Return: True or False
    """

    return (type(obj) != a_class and isinstance(obj, a_class))
