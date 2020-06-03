#!/usr/bin/python3
""" 7-save_to_json_file.py """


def save_to_json_file(my_obj, filename):
    """ write an object to a text file using JSON repr """
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
