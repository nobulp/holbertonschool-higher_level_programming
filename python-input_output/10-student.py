#!/usr/bin/python3
"""Module that defines a Student class with a filtered JSON representation."""


class Student:
    """Represent a student with basic public attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance.

        If `attrs` is a list of strings, only return the listed attributes
        that exist on the instance. Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
