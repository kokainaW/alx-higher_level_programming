#!/usr/bin/python3
"""
Will create a class that inherits from int
"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behaviour of != and ==
    """

    def __eq__(self, other):
        """Equality becomes inequality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality"""

        return super().__eq__(other)
