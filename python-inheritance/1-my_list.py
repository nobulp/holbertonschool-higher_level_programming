#!/usr/bin/python3
"""
Module defining a custom list class.
"""


class MyList(list):
    """
    Custom list class that provides
    a method to display a sorted version
    of the list without modifying it.
    """

    def print_sorted(self):
        """
        Prints the elements of the list
        in ascending order.
        """
        print(sorted(self))
