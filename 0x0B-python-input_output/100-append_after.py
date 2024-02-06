#!/usr/bin/python3
"""This module contains an append_after func"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after the line containing search_string"""

    with open(filename, mode='a+', encoding='utf-8') as f:
        f.seek(0)
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.truncate()
            f.write(line)
            if search_string in line:
                f.write(new_string.rstrip("\n") + "\n")
