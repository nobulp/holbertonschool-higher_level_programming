#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initializes a Square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
