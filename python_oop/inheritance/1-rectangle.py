#!/usr/bin/env python3
"""Define a rectangle based on BaseGeometry."""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with validated private dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle with its width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
