#!/usr/bin/env python3
"""Custom object serialization/deserialization using pickle."""

import pickle


class CustomObject:
    """Represent a simple custom object that can be pickled."""

    def __init__(self, name, age, is_student):
        """Initialize the object with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to `filename` using pickle.

        Return None if an error occurs (e.g., invalid path/permissions).
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an instance of CustomObject from `filename`.

        Return None if the file doesn't exist or is malformed.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            return obj if isinstance(obj, cls) else None
        except (OSError, EOFError, pickle.UnpicklingError, AttributeError):
            return None
