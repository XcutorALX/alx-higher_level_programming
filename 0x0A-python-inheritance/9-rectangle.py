#!/usr/bin/python3
"""This module contains a rectangle classs"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle

    SuperClass:
        BaseGeometry
    """

    def __init__(self, width, height):
        """Instantize a rectangle instance

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        defines the string representation of a rectangle
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
