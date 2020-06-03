#!/usr/bin/python
""" 6-from_json_string """


def from_json_string(my_str):
    """ Return an object from json """
    import json
    return json.loads(my_str)
