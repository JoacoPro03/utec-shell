#!/usr/bin/env python3
"""Define a square based on the complete rectangle class."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with equal width and height."""

    def __init__(self, size):
        """Initialize a square with the given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
