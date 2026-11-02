#!/usr/bin/env python3
"""Define a complete rectangle based on the inherited rectangle class."""

RectangleBase = __import__('1-rectangle').Rectangle


class Rectangle(RectangleBase):
    """Represent a rectangle with area and string representation."""

    def area(self):
        """Return the rectangle area."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return a readable description of the rectangle."""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height,
        )
