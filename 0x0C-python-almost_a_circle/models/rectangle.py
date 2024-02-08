#!/usr/bin/python3
"""This module contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Representation of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        
        self.typeValidator("width", value)
        self.greaterThanValidator("width", value, 0)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for the height attribute"""

        self.typeValidator("height", value)
        self.greaterThanValidator("height", value, 0)
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setter for the x attribute"""

        self.typeValidator("x", value)
        self.greaterOrEqualValidator("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setter for the y attribute"""

        self.typeValidator("y", value)
        self.greaterOrEqualValidator("y", value, 0)
        self.__y = value

    def area(self):
        """Returns the area of a rectangle instance"""

        return (self.width * self.height)

    def display(self):
        """Prints a rectangle instance unto stdout"""

        print(("#" * self.width + "\n") * self.height, end="")
