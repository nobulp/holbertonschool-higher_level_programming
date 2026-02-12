#!/usr/bin/python3
"""Module that provides a function to append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF-8) and return chars added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
