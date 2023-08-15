#!/usr/bin/python3
"""Create object from JSON file"""
import json


def load_from_json_file(filename):
    """ Create object from JSON file
    Args:
        filename: the JSON file
    Returns:
        the object
    """
    with open(filename) as f:
        return json.load(f)
