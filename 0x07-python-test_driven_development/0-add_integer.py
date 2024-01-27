#!/usr/bin/python3
"""Contains a function that adds integers"""

def add_integer(a, b=98):
    """This function adds two integers

    Args:
        a: the first integer to be added
        b: the second integer to be added

    Return: a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    
    return (a + b)
