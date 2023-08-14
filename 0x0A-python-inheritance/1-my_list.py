#!/usr/bin/python3
class MyList(list):
    """A class myList that inherits from list"""
    
    def __init__(self):
        super().__init__()


    def print_sorted(self):
        print(sorted(self))
