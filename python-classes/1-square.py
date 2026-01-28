#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: The size of the square.
        """
        self.__size = size
