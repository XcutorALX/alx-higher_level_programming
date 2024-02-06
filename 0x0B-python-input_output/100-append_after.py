#!/usr/bin/python3
"""This module contains an append_after func"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after the line containing search_string"""

    if not search_string or not new_string:
        return 0

    with open(filename, mode='a+', encoding='utf-8') as f:
        f.seek(0)
        lines = f.readlines()
        f.seek(0)
        f.truncate(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
