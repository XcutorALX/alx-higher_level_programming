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

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of an instance"""

        if not args:
            for i in kwargs:
                if i == "size":
                    self.size = kwargs[i]
                elif i == "id":
                    self.id = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                else:
                    self.y = args[i]

    def to_dictionary(self):
        """The dictionary representation of a square"""

        result = {
                'size': self.size,
                'x': self.x,
                'y': self.y,
                'id': self.id
                }
        return (result)

    @staticmethod
    def dummyInstance():
        """creates a dummy instance of this class"""
        return (Square(1, 0, 0))
