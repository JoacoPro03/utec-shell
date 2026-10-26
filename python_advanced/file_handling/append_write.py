#!/usr/bin/env python3
"""Utilities for appending text to files."""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return the number of characters."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
