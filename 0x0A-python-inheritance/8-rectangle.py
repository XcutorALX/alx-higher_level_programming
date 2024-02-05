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
