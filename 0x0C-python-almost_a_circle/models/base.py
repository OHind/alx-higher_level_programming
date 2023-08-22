#!/usr/bin/python3
""" A base class"""
import json
import csv
import turtle


class Base:
    """ A base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ A constructor
        Args:
            id - the id of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ The JSON representation
        Args:
            list_dictionaries - The list of dictionaries to represent in JSON
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_directionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSO representation of the list_objs into a file
        Args:
            list_objs - a list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ deserialization of JSON strin
        Args:
            json_string - the JSON strin
        Returns:
            The python list represented by the JSON string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
