#!/usr/bin/python3


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """__init__ method
        Args:
            width (int): width integer must be greater than 0
            height (int): height integer must be greater than 0
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
