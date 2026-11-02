#!/usr/bin/env python3
"""Define a square with a position and printable representation."""


class Square:
    """Represent a square with validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with its size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the square position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and set the square position."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(item, int) for item in value)
            or not all(item >= 0 for item in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square at its current position."""
        print(self)

    def __str__(self):
        """Return the square as text at its current position."""
        if self.__size == 0:
            return ""
        vertical = "\n" * self.__position[1]
        horizontal = " " * self.__position[0]
        rows = "\n".join(
            horizontal + ("#" * self.__size)
            for _ in range(self.__size)
        )
        return vertical + rows
