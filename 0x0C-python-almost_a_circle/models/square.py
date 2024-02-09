#!/usr/bin/python3
"""This module contains a square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Representation of a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantizes a Square instance"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The string representation of a square instance"""

        return (f"[Square] ({self.id)} {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
