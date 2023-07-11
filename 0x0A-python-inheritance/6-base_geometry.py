#!/usr/bin/python3
"""
Will create a class
"""


class BaseGeometry:
    """Class with public instance method"""

    def area(self):
        """Raises an Exception with the message
        'area() is  not implemented'
        """

        raise Exception('area() is not implemented')
