#!/usr/bin/python3
"""This module contains a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle Object

        Args:
            width(int): the width of the rectangle
            heigth(int): the height of the rectangle
        """
        Rectangle.number_of_instances += 1
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
        """Returns the string representation of the object"""
        if self.width == 0 or self.height == 0:
            return ('')

        return (((str(self.print_symbol) * self.width + '\n')
                * self.height).rstrip())

    def __repr__(self):
        """Returns the official string representation of the object"""

        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """This function is called when an instance of this class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This function compares two rectangle instances

        Args:
            rect_1: the first rectangle
            rect_2: the second rectangle
        """

        param = {"rect_1": rect_1, "rect_2": rect_2}
        for obj in param:
            if not isinstance(param[obj], Rectangle):
                raise TypeError(f"{obj} must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """This class method returns a new class instance
        of height == width == size

        Args:
            size(int): the new size
        """
        return (cls(size, size))
