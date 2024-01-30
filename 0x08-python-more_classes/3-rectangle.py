#!/usr/bin/python3
"""This module contains a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle Object

        Args:
            width(int): the width of the rectangle
            heigth(int): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Gets the width of the instance of the rectangle object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle instance

        Args:
            value(int): the value to set the width to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height of the instance of the rectangle object"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle instance

        Args:
            value(int): the value to set the height to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle (height * width)"""
        return (self.height * self.width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return (0)

        return (2 * (self.height + self.width))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ('')

        return (("#" * self.width + '\n') * self.height)
