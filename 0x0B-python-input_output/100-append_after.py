#!/usr/bin/python3
"""This module contains an append_after func"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after the line containing search_string

    Args:
        filename: the name of the file
        search_string: the string to search for
        new_string: the string to add
    """

    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
