#!/usr/bin/env python3
"""Convert CSV data to JSON format and save it to data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Read a CSV file and write its contents as JSON to data.json.

    Return True if successful, otherwise return False (e.g., file not found).
    """
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True
    except (FileNotFoundError, OSError, csv.Error, json.JSONDecodeError):
        return False
