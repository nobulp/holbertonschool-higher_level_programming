#!/usr/bin/python3
"""Defines a function that checks class inheritance."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or
    an instance of a class that inherited from a_class.
    """
    return isinstance(obj, a_class)
