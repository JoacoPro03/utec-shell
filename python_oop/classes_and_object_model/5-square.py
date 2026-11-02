#!/usr/bin/env python3
"""Define a square with controlled size and text output."""


class Square:
    """Represent a square with validated size accessors."""

    def __init__(self, size=0):
        """Initialize a square with the given size."""
        self.size = size

    @property
    def size(self):
        """Return the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and set the square size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character."""
        for _ in range(self.__size):
            print("#" * self.__size)
