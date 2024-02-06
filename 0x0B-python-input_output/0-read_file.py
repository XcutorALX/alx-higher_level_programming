#!/usr/bin/python3
"""This module contains a read_file function"""


def read_file(filename=""):
    """This function reads a text file and prints it"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
