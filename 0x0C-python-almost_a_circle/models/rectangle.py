#!/usr/bin/python3
"""A rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ A rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ The condtructor
        Args:
            width - The width of the class
            height - The height of the class
            x - the x coordinate
            y - The y coordinate
        Raises:
            TypeError: if the input is not integer
            ValueError: if width and height values are under or equal 0
            ValueError: if x and y are under 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ The getter of the private attribute width
        Returns:
            The width value
        """
        return self.__width

    @property
    def height(self):
        """The getter of the private attribute height
        Returns:
            The height value
        """
        return self.__height

    @property
    def x(self):
        """ The getter of the private attribute x
        Returns:
            The x value
        """
        return self.__x

    @property
    def y(self):
        """The getter of the private attribute y
        Returns:
            The y value
        """
        return self.__y

    @width.setter
    def width(self, width):
        """The setter for the private attribute __width
        Args:
            width - the width value
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """The setter for the private attribute __height
        Args:
            height - the height value
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """The setter for the private attribute __x
        Args:
            x - the x value
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """The setter for the private attribute __y
        Args:
            y - the y value
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """The area of the rectangle
        Returns:
            The area of the rectangle
        """

        return self.width * self.height

    def display(self):
        """Prints the rectangle instance"""
        rows = self.height
        columns = self.width
        for a in range(self.y):
            print()
        for r in range(self.height):
            print(' ' * self.x, end='')
            for c in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ ___str__ overrided"""

        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__,
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Update each attribute
        Args:
            *args: the arguments passed into the function
        """

        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
