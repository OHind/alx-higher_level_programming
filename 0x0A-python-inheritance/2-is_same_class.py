#!/usr/bin/python3
""" Determin if the object is exactly the specified instance of the specified class"""



def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class


    Args:
        obj (any): the object to check
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True
        else - False
        """

    if type(obj) == a_class:
        return True
    return False
