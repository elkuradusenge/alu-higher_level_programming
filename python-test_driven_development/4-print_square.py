#!/usr/bin/python3
""" module documented"""


def print_square(size):
    """Prints a square with the character #.
    Args:
        size (int): Size of the square
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
