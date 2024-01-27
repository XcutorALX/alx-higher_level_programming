#!/usr/bin/python3
"""This module contains a function that prints out squares"""


def print_square(size):
    """A function that prints a square with provided dimensions

    Args:
        size(int): the size of the square to print
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
        return

    print((("#" * size) + '\n') * size, end="")
