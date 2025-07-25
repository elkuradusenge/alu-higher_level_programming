#!/usr/bin/python3
"""module documented"""


def say_my_name(first_name, last_name=""):
    """Prints a name
    Args:
        first_name (str): First name
        last_name (str): Last name
    Returns:
        None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
