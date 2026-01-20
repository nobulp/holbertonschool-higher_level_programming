#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for characters in my_string:
        if characters != 'c' and characters != 'C':
            new_string += characters
    return new_string
