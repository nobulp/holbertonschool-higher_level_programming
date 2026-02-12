#!/usr/bin/python3
"""
Provides a helper to serialize a Python object into JSON
and write it to a file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of `my_obj` into `filename` (UTF-8).
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
