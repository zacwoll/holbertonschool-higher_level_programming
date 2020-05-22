#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer()"""

    def test_max(self):
        """Test valid inputs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-2, -3, 0]), 0)
        self.assertEqual(max_integer([500]), 500)

    def test_type(self):
        """Test other input types"""
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer((1, 2, 4)), 4)
        self.assertEqual(max_integer([1, 2, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, float('nan')]), 2)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
