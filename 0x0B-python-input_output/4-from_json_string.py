#!/usr/bin/python3
"""from JSON to python object"""
import json


def from_json_string(my_str):
    """From JSON to py object
    Args:
        my_str: the string represented
    Returns:
        returns a python data structure
    """
    return json.loads(my_str)
