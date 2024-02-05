#!/usr/bin/python3
"""This module contains a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a Square

    Base:
        Rectangle: a class representation of a rectangle
    """

    def __init__(self, size):
        """Instantizes a Square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of Square"""
        return (f"[Square] {self.__size}/{self.__size}")
