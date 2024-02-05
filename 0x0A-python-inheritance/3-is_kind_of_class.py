#!/usr/bin/python3
"""This module contains an object comparing function"""


def is_kind_of_class(obj, a_class):
    """This function checks if an object is an instance or subclass

    Args:
        obj: the object to check
        a_class: the class to compare with

    Return: True or False
    """
    return (isinstance(obj, a_class))
