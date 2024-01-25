#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): the size of the new square

        """

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (type(position) == tuple and len(position) == 2 and
                type(position[0]) == int and type(position[1]) == int and
                position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Finds the area of the square

        Return: the area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with '#'"""

        if (self.size == 0):
            print()
            return

        if (self.__position[1] != 0):
            print("" * self.__position[1])
        for i in range(self.__size):
            if (self.__position[0] != 0):
                print(" " * self.__position[0], end='')
            print("#" * self.__size)
