#!/usr/bin/python3

"""it defines a class Square."""


class Square:
    """It represents a square."""

    def __init__(self, size):
        """It initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Will Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
