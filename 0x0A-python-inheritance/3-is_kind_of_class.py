#!/usr/bin/python3
""" A function that verifies two objects"""



def is_kind_of_class(obj, a_class):
    """checks object is an instance of, or if the object is an instance of a class that inherited from
    

    Args:
        obj (any): the object to check
        a_class (type): the reference object
    Returns:
        if object is an instance of a_class of a class that inherited from - True
        Else -False
    """

    if isinstance(obj, a_class):
        return True
    return False

