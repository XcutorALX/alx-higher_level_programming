#!/usr/bin/python3
"""This module contains a Base class"""


class Base:
    """Base class of all other classes"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Instantizes a Base class with the specified ID"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def typeValidator(name, value):
        """Checks if value if of type int"""

        if type(value) != int:
            raise ValueError(f"{name} must be an integer")

        return (1)

    @staticmethod
    def greaterThanValidator(name, value, test):
        """Checks if value > test"""

        if value <= test:
            raise TypeError(f"{name} must be > 0")

        return (1)

    @staticmethod
    def greaterOrEqualValidator(name, value, test):
        """Checks if value >= test"""

        if value < test:
            raise TypeError(f"{name} must be >= 0")

        return (1)

    @staticmethod
    def resetId():
        Base.__nb_objects = 0
