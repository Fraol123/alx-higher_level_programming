#!/user/bin/python3

import json
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_instantiation(unittest.TestCase):
    """unittest for checking for square instantiation"""
    def test_square_is_Rectangle(self):
        self.assertIsInstance(Square(10, 2), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_with_one_arg(self):
        s1 = Square(3)
        s2 = Square(4)
        self.assertEqual(s1.id, s2.id - 1)

    def test_with_two_arg(self):
        s1 = Square(3, 4)
        s2 = Square(5, 6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(3, 4, 5)
        s2 = Square(6, 7, 8)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(5, Square(2, 3, 6, 5).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(2, 3, 4, 5, 6)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 3, 4, 1).__size)

    def test_size_gitter(self):
        self.assertEqual(2, Square(2, 3, 4, 5).size)

    def test_size_setter(self):
        s = Square(2, 3, 4, 2)
        s.size = 4
        self.assertEqual(4, s.size)
if __name__ == "__main__":
    unittest.main()
