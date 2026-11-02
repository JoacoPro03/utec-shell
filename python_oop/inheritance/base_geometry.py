#!/usr/bin/env python3
"""Define the base class for geometric figures."""


class BaseGeometry:
    """Provide shared behavior for geometric figures."""

    def area(self):
        """Raise an exception because the area is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
