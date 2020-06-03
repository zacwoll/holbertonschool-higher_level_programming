#!/usr/bin/python3
""" 8-load_from_json_file """


def load_from_json_file(filename):
    """ Create an object from JSON file """
    import json
    with open(filename, 'r') as f:
        return json.loads(f.read())
