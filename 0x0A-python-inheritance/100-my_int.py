#!/usr/bin/python3
"""This module contains a MyInt class"""


class MyInt(int):
    """Rebel integer"""

    def __init__(self, value):
        """Instantizes a MyInt instance"""

        super().__init__()
        self.__value = value

    def __eq__(self, other):
        """A comparison constructor"""

        return (self.__value != other)

    def __ne__(self, other):
        """A comparison constructor"""

        return (self.__value == other)
