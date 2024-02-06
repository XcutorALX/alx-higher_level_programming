#!/usr/bin/python3
"""This module contains a write file function"""


def write_file(filename="", text=""):
    """This function writes a string to a text file"""

    with open(filename, mode="w", encoding='utf-8') as f:
        return (f.write(text))
