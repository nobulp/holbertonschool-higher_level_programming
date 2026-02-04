#!/usr/bin/python3
"""Defines a BaseGeometry class with area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raises an exception for unimplemented area."""
        raise Exception("area() is not implemented")
