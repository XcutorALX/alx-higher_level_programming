#!/usr/bin/python3
"""This module contains a read_file function"""


def read_file(filename=""):
    """This function reads a text file and prints it"""

    if not filename:
        return 0

    with open(filename, encoding="UTF-8") as f:
        print(f.read())
