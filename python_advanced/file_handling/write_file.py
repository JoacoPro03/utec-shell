#!/usr/bin/env python3
"""Utilities for writing text files."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
