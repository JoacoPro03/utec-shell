#!/usr/bin/env python3
"""Define a square with its own string representation."""

SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represent a square with a square-specific description."""

    def __str__(self):
        """Return a readable description of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height,
        )
