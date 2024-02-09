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

        if self.y != 0:
            print("\n" * self.y, end='')

        print((" " * self.x + ("#" * self.width) + "\n") * self.height, end="")

    def __str__(self):
        """String representation of a rectangle instance"""

        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Updates all the attributes of rectangle"""

        if len(args) == 0:
            for i in kwargs:
                if i == 'id':
                    self.id = kwargs[i]
                elif i == 'width':
                    self.width = kwargs[i]
                elif i == 'height':
                    self.height = kwargs[i]
                elif i == 'x':
                    self.x = kwargs[i]
                elif i == 'y':
                    self.y = kwargs[i]

        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            else:
                self.y = args[i]
