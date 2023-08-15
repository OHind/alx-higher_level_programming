#!/usr/bin/python3
"""Save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """ Save to json file
    Args:
        my_obj: the object to serialize
        filename: where to save
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
