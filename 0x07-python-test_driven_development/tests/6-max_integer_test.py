#!/usr/bin/python3
"""Unittest for max_integer([...])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the function max_integer for correct out put"""

    def test_max_at_the_end(self):
        """Teast all postive number"""
        self.assertEqual(max_integer([1,2,3,4]), 4)

    def test_one_negative_number(self):
        """Test when there is one negative number"""
        self.assertEqual(max_integer([1,-2, 3, 5]), 5)

    def test_only_negative(self):
        """ test when all elemnts are negative"""
        self.assertEqual(max_integer([-1,-2,-3,-4]), -1)

    def test_Zero(self):
        """test when there is no element"""
        self.assertEqual(max_integer([]), None)

    def test_postive_and_negative(self):
        """ test when the list contain postive and negative"""
        self.assertEqual(max_integer([-55,5,85,-78,-1,200]), 200)

    def test_max_in_the_middle(self):
        """when max comes at the middle"""
        self.assertEqual(max_integer([1,2,12,3,4]), 12)

    def test_max_at_the_begining(self):
        """when max comes at the begining"""
        self.assertEqual(max_integer([12,1,2,3,4]), 12)

    def test_max_all_equal(self):
        """when elements are equal"""
        self.assertEqual(max_integer([12,12,12]), 12)

    def test_list_with_one_element(self):
        """when the list contain only one element"""
        self.assertEqual(max_integer([12]), 12)

if __name__ == '__main__':
    unittest.main()
