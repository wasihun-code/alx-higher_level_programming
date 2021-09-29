#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a circle."""
        return (self.__size * self.__size)
    def my_print(self):
        """Prints the square using hashtag."""
        if self.__size <= 0:
            print()
        else:
            for i in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end='')
                print()
