#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """ module called write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
