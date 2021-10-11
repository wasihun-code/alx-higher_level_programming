#!/usr/bin/python3
"""a class that inherits from list."""


class MyList(list):
        """Inherits from A list super class."""

        def print_sorted(self):
            """Prints the list in sorted assencing order."""
            print(sorted(self))
