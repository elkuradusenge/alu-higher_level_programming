#!/usr/bin/python3
'''function that returns the dictionary's description with data structure
'''


def class_to_json(obj):
    '''module class_to_json
       returns builds a dictionary
    '''
    return obj.__dict__
