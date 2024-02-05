#!/usr/bin/python3
"""This module contains a class that inherits from list"""


class MyList(list):
    """A class that inherits from my list
    
    Base:
        list: the python list object
    """

    def print_sorted(self):
        print(sorted(self))
