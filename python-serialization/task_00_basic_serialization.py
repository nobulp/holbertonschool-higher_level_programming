#!/usr/bin/env python3
"""Basic serialization utilities: save/load a Python dictionary as JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to JSON and save it to a file (overwrite)."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON data from a file and return it as a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
