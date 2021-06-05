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


    def test_four_args(self):
        r1 = Rectangle(3,5,6,4)
        r2 = Rectangle(4,6,5,3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(3, Rectangle(10, 2, 0, 0, 3).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2,3,4,2,1).__widtth)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2,3,4,2,1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2,3,4,2,1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2,3,4,2,1).__y)

    def test_width_getter(self):
        r = Rectangle(2,3,4,5,1)
        self.assertEqual(2, r.width)

    def test_width_setter(self):
        r = Rectangle(3,7,7,3,1)
        r.width = 6
        self.assertEqual(6, r.width)

    def test_height_getter(self):
        r = Rectangle(2,3,4,2,1)
        self.assertEqual(3, r.height)

    def test_height_setter(self):
        r = Rectangle(3,7,7,3,1)
        r.height = 6
        self.assertEqual(6, r.height)

    def test_y_getter(self):
        r = Rectangle(2,3,4,2,1)
        self.assertEqual(2, r.y)

    def test_y_setter(self):
        r = Rectangle(3,7,7,3,1)
        r.y = 6
        self.assertEqual(6, r.y)

    def test_x_getter(self):
        r = Rectangle(2,3,4,2,1)
        self.assertEqual(4, r.x)

    def test_x_setter(self):
        r = Rectangle(3,7,7,3,1)
        r.x = 6
        self.assertEqual(6, r.x)


class TestRectangle_width(unittest.TestCase):
    """unittest for initalization of width attribute"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(2.2, 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(complex(3), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle({'k': 2, 'm': 3}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle([1,2,3], 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle((1,2,3), 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle({1,2,3}, 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(float('inf'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
                Rectangle(0, 2)

class TestRectangle_height(unittest.TestCase):
    """unittest for initalization of height attribute"""

    def test_height_width(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle( 2, "invalid")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, 2.2)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, complex(3))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, {'k': 2, 'm': 3})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, True)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, [1,2,3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, (1,2,3))

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, {1,2,3})

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(2, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
                Rectangle(2, 0)
























    if __name__ == "__main__":
        unittest.main()
