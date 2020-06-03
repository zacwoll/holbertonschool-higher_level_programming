#!/usr/bin/python3
""" 5-to_json_string """


def to_json_string(my_obj):
    """ render object to json string """
    import json
    return json.dumps(my_obj)
