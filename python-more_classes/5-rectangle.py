#!/usr/bin/python3
"""Rectangle module with basic geometry operations."""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): New width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): New height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Returns:
            str: The rectangle as a string or an 
            empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string that can recreate the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor that prints a message when the rectangle is deleted.
        """
        print("Bye rectangle...")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
