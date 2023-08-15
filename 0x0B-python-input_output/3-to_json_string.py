#!/usr/bin/python3
"""The JSON representation of an object"""
import json

def to_json_string(my_obj):
    """a JSON representation of an object 
    Args:
        my_obj: the python object
    Returns:
        The JSON representation
    """
    return json.dumps(my_obj)
