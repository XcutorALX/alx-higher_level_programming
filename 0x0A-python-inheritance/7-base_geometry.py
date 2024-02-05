#!/usr/bin/python3
"""This module contains a Base geometry class"""


class BaseGeometry:
    """A BaseGeometry class"""


    def area(self):
        """returns the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer

        Args:
            name: the name
            value: the value to validate
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
