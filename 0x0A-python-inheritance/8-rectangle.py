#!/usr/bin/python3
"""Documentation for BaseGeometry class"""


class BaseGeometry:
    """Creates Base geometry class"""

    def area(self):
        """Calcuates the area of a geometrical object."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

class Rectangle(BaseGeometry):
    """Inherits from base geometry class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height
