#!/usr/bin/env python3
"""Serialize a Python dictionary to XML and deserialize XML back to a dictionary."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary into XML and save it to `filename`."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = "" if value is None else str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserialize XML data from `filename` and return it as a dictionary.

    Return None if the file doesn't exist or is malformed.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = "" if child.text is None else child.text
        return result
    except (FileNotFoundError, ET.ParseError, OSError):
        return None
