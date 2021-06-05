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














































    if __name__ == "__main__":
        unittest.main()
