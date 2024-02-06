#!/usr/bin/python3
"""This module contains a append_write function"""


def append_write(filename="", text=""):
    """This function appends text to the end of a file"""

    with open(filename, encoding='utf-8', mode='a') as f:
        return (f.write(text))
