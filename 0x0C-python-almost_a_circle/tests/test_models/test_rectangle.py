#!/user/bin/python3
import unittest
import json
import io
import sys
from models.rectangle import Rectangle
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
        r1 = Rectangle(3, 5, 6, 4)
        r2 = Rectangle(4, 6, 5, 3)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(3, Rectangle(10, 2, 0, 0, 3).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 4, 2, 1).__widtth)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 4, 2, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 4, 2, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 4, 2, 1).__y)

    def test_width_getter(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(2, r.width)

    def test_width_setter(self):
        r = Rectangle(3, 7, 7, 3, 1)
        r.width = 6
        self.assertEqual(6, r.width)

    def test_height_getter(self):
        r = Rectangle(2, 3, 4, 2, 1)
        self.assertEqual(3, r.height)

    def test_height_setter(self):
        r = Rectangle(3, 7, 7, 3, 1)
        r.height = 6
        self.assertEqual(6, r.height)

    def test_y_getter(self):
        r = Rectangle(2, 3, 4, 2, 1)
        self.assertEqual(2, r.y)

    def test_y_setter(self):
        r = Rectangle(3, 7, 7, 3, 1)
        r.y = 6
        self.assertEqual(6, r.y)

    def test_x_getter(self):
        r = Rectangle(2, 3, 4, 2, 1)
        self.assertEqual(4, r.x)

    def test_x_setter(self):
        r = Rectangle(3, 7, 7, 3, 1)
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
                Rectangle([1, 2, 3], 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle((1, 2, 3), 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle({1, 2, 3}, 2)

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
                Rectangle(2, "invalid")

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
                Rectangle(2, [1, 2, 3])

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, (1, 2, 3))

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(2, {1, 2, 3})

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


class TestRectangle_x(unittest.TestCase):
    """unittest for initalization of x attribute"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, 2.2, 3)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, complex(3))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, {'k': 2, 'm': 3}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, [1, 2, 3], 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, (1, 2, 3), 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, {1, 2, 3}, 2)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(1, 2, -1, 2)


class TestRectangle_y(unittest.TestCase):
    """unittest for initalization of y attribute"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 2, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, 2.2)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, complex(3))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, {'k': 2, 'm': 3})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, [1, 2, 3])

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, (1, 2, 3))

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, {1, 2, 3})

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
                Rectangle(1, 2, 3, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
                Rectangle(1, 2, 1, -2)


class TestRectangle_x(unittest.TestCase):
    """unittest for initalization of x attribute"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, 2.2, 3)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, complex(3))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, {'k': 2, 'm': 3}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, [1, 2, 3], 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, (1, 2, 3), 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, {1, 2, 3}, 2)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
                Rectangle(1, 2, -1, 2)


class TestRectangle_order_of_initialization(unittest.TestCase):
    """unittest for testing of Rectangle order of attribute initalize"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
                Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
                Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before__y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
                Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """unittest for testing the area method of the rectangle class."""

    def test_area_small(self):
        r = Rectangle(2, 3, 0, 0, 0)
        self.assertEqual(6, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Rectangle(3, 2, 5, 1, 1)
        r.width = 7
        r.height = 8
        self.assertEqual(56, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """unittests for testing __str__ and display methods of rectangle class"""

    def hold_stdout(rect, method):
        """hold and return text printed to stdout.
        Args:
           rect(Rectangle): the rectangle to print to stdout
           method (str): the method to run on rect.
        """

        hold = io.StringIO()
        sys.stdout = hold
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return hold

        # Test for __str__ method
    def test_str_method_prinnt_width_height(self):
        r = Rectangle(4, 6)
        hold = TestRectangle_stdout.hold_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, hold.getvalue())

    def test_str_method__width_height_x(self):
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    # test display method
    def test_display_width_height(self):
        r = Rectangle(2, 3, 0, 0, 0)
        hold = TestRectangle_stdout.hold_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", hold.getvalue())

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        hold = TestRectangle_stdout.hold_stdout(r, "display")
        self.assertEqual("###\n###\n", hold.getvalue())

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        hold = TestRectangle_stdout.hold_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, hold.getvalue())


class TestRectangle_update_args(unittest.TestCase):
    """unittests for testing update args method of the rectangle class"""

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")

        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)

        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()

        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=99, width=1, height=2)
        self.assertEqual("[Rectangle] (99) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 10/9 - 10/7".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (89) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """test dictionery"""
    def test_to_dictionary_output(self):
        r = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
