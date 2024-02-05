#!/usr/bin/python3
"""This module contains an add_attribute func"""


def add_attribute(obj, atr, val):
    """Adds a new attribute to an object if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, val)
