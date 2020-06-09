#!/usr/bin/python3
"""
Tests for Base Class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_base(unittest.TestCase):
    """ Test Base methods """
    def setUp(self):
        """ Imports module, instantiates class """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_nb_objects_private(self):
        """ Tests if nb_objects is a private class attribute """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_nb_objects_initialized(self):
        """ Tests if nb_objects initializes to zero """
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instantiation(self):
        b = Base(1)
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_constructor(self):
        """ Tests constructor """
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(e.exception), msg)

    def test_consecutive_ids(self):
        """ Tests id consecutively """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_synced(self):
        """ Tests sync between class and instance id """
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)

    def test_custom_id_int(self):
        """ Tests custom id """
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_custom_id_str(self):
        i = "Tabitha"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_id_keyword(self):
        """ Tests id passed as kwarg """
        i = 98
        b = Base(id=i)
        self.assertEqual(b.id, i)

    # -- #15 -- #
    def test_to_json_string(self):
        """ Tests to_json_string() """
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 5, 'y': 5, 'width': 4, 'id': 12, 'height': 3}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{"Tabitha": 98}]
        self.assertEqual(Base.to_json_string(d), '[{"Tabitha": 98}]')
        d = [{"Tabitha": 98}, {"cat": 5}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"Tabitha": 98}, {"cat": 5}, {"HI": 0}]')
        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')

        r1 = Rectangle(1, 2, 3, 4)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dict)

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(10, 7, 2)
        r2 = Square(1, 2, 3)
        r3 = Square(2, 3, 4)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # -- #16 -- #
    def test_save_to_file(self):
        """ Tests save_to_file method """
        import os
        r1 = Rectangle(15, 4, 3, 2)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        r2 = Square(1)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

    # -- #17 -- #
