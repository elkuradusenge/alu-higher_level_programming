#!/usr/bin/python3
"""Module for Rectangle class with area, perimeter, and string representation.
"""


class Rectangle:
    """Defines a rectangle by width and height with related operations."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: Perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def _draw_rectangle(self):
        """
        Build a string representation of the rectangle using '#'.

        Returns:
            str: The rectangle represented with '#' characters.
        """
        rect = ""
        for row in range(self.__height):
            rect += '#' * self.__width
            if self.__width != 0 and row < (self.__height - 1):
                rect += '\n'
        return rect

    def __str__(self):
        """
        Informal string representation of the rectangle.

        Returns:
            str: The visual rectangle using '#'.
        """
        return self._draw_rectangle()

    def __repr__(self):
        """
        Official string representation of the rectangle.

        Returns:
            str: A string that can recreate the rectangle using eval().
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
