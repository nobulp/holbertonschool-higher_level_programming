#!/usr/bin/python3
"""
This module provides a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The first name (must be a string)
        last_name: The last name (must be a string, default is "")

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
