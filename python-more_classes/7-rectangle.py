#!/usr/bin/python3
"""Rectangle class with area, perimeter, and print support."""


class Rectangle:
    """Defines a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(str(self.print_symbol) *
                         self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return formal string representation for eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Get rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width, must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height, must be int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
