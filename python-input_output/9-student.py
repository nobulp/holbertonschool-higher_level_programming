#!/usr/bin/python3
"""Module that defines a Student class and returns its dictionary representation."""


class Student:
    """Represent a student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of the instance."""
        return self.__dict__
