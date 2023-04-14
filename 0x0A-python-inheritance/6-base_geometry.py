#!/usr/bin/python3
"""
Contain the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raise an exception when called"""
        raise Exception("area() is not implemented")
