#!/usr/bin/python3
"""Rectangle class with area, perimeter, comparison, and square creation."""


class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
        number_of_instances (int): Tracks number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        bigger_or_equal(): Compares two rectangles based on area.
        square(): Creates a square-shaped Rectangle.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Return the string representation of the
         rectangle using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ''
        return '\n'.join(str(self.print_symbol) *
                         self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string that can recreate the instance with eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Called when an instance is deleted. Decreases instance count."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """
        Create a square rectangle (width == height == size).

        Args:
            size (int): Size of the square sides.

        Returns:
            Rectangle: New square-shaped rectangle.
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with the bigger area.

        Args:
            rect_1 (Rectangle): First rectangle.
            rect_2 (Rectangle): Second rectangle.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If either argument is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width (must be non-negative integer).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height (must be non-negative integer).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width 
         or height is 0."""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * \
            (self.__width + self.__height)
