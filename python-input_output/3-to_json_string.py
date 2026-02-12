#!/usr/bin/python3
"""Module that provides a function to return the JSON representation of an object."""


import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of an object."""
    return json.dumps(my_obj)
