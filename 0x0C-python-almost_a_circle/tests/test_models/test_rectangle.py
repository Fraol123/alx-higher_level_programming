#!/user/bin/python3
import unittest
import json
from models.rectangle  import Rectangle
from models.base import Base

class TestRectangle_instantiation(unittest.TestCase):
    """unitest for checking rectangle instantiation"""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
           Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 1, 3)
        r2 = Rectangle(3, 1, 2)
        self.assertEqual(r1.id, r2.id - 1)











































    if __name__ == "__main__":
        unittest.main()
