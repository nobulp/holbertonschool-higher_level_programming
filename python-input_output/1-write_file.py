#!/usr/bin/python3
"""Module that provides a function to write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
