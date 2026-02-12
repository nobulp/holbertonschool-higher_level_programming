#!/usr/bin/python3
"""Module that provides a function to write an object to a text file using JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
