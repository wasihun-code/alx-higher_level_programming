#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        self.__size = size

    def get_size(self):
        """getter function for validation."""
        return self.__size

    def set_size(self, x):
        """Setter to check user input."""
        if x.isdigit():
            if (x < 0):
                raise ValueError("size must be >= 0")
            self.__size = x
        else:
            raise TypeError("it must be a digit")
