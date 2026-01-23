#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating their types.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Reject NaN and infinity
    if a != a or a in (float("inf"), float("-inf")):
        raise TypeError("a must be an integer")
    if b != b or b in (float("inf"), float("-inf")):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
