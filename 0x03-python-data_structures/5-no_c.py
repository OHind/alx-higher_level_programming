#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    new_string = ''
    for x in new_list:
        if x != 'c' and x != 'C':
            new_string += x
    return new_string
