#!/usr/bin/python3
"""This module contains a function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if two objects are of the same class

    Args:
        obj: the first object to test
        a_class: class to test with

    Return: True if same class otherwise False
    """

    return (type(obj) == a_class)
