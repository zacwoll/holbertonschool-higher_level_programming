#!/usr/bin/python3
""" Base Class """
from json import dumps, loads
import csv


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init a Base Instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Json's a dict """
        if not list_dictionaries or list_dictionaries is None:
            return '[]'
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ un-Json's a dict """
        if not json_string or json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves obj to .json """
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from .json """
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, 'r') as f:
            return [cls.create(**ob) for ob in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance set with attributes """
        if cls.__name__ is "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ is "Square":
            new = cls(1)
        else:
            new = None
        cls.update(new, **dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves object to .csv """
        if list_objs is not None:
            if cls.__name__ is "Rectangle":
                data = [[o.id, o.width, o.height, o.x, o.y] for o in
                        list_objs]
            elif cls.__name__ is "Square":
                data = [[o.id, o.size, o.x, o.y] for o in list_objs]
        with open("{}.csv".format(cls.__name__), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """ Return a list of instances from .csv """
        dictionary = []
        with open("{}.csv".format(cls.__name__), 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls.__name__ is "Rectangle":
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                elif cls.__name__ is "Square":
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                dictionary.append(cls.create(**d))
        return dictionary
