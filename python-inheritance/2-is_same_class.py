#!/usr/bin/python3
"""Defines a function that checks for exact class match."""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise returns False.
    """
    return type(obj) is a_class
