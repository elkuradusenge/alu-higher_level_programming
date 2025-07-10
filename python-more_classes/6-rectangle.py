#!/usr/bin/python3
"""Defines a Rectangle class with area, perimeter, 
    and string representation."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # Tracks active Rectangle instances

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Return the string representation of the rectangle using '#' characters.

        Returns:
            str: Formatted rectangle string or empty string
             if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Return an official string representation of the rectangle.

        Returns:
            str: String that can recreate the rectangle instance using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor for Rectangle. Decreases instance count and prints a
         message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
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
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
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
