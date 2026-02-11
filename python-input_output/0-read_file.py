#!/usr/bin/python3
"""Module for reading and printing text files."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
