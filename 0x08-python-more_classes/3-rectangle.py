#!/usr/bin/python3
"""Rectangle class with getter and setter."""


class Rectangle:
    """Represents a rectangle class."""

    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle."""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Print the rectangle with the character #."""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
