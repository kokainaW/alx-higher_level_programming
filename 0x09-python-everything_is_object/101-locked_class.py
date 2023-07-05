#!/usr/bin/python3
"""it will define a locked class."""


class LockedClass:
    """
    Will prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
