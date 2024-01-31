#!/usr/bin/python3
"""This module contains a locked class that limits
attributes adding"""


class LockedClass:
    """A class that prevents users from
    dynamically creating attributes"""

    __slots__ = ["first_name"]
