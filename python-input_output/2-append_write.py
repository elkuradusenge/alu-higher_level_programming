#!/usr/bin/python3
"""Create a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): Name of file to append to.
        text (str): The string to append to the file.
    Returns:
        Number appended characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
