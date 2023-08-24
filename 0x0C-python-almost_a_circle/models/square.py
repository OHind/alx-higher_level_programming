#!/usr/bin/python3
"""The square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor
        Args:
            size - The size of the square
            x - x coordinate
            y - y coordinate
            id - the id of each instance of the class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of the size attribute
        Returns:
            width
        """
        return self.width

    @size.setter
    def size(size):
        """The setter of the size attrbute
        Args:
            size : size of the square
        Raises:
            TypeError: if the siez is not an integer
            ValueError: if not grater than zero
        """
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of square object"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the squer using none key-worded values and key-worded values
        Args:
            *args - Number of arguments
            **kwargs - Number of key-worded arguments
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """ The dictionary representation of the square
        Returns:
        The dictionary representation of the square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
