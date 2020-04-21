import math
import unittest
from conditional import *

class TestCases(unittest.TestCase):

    def test_f_max_101(self):
        result = math_func_max_101(1, 2)
        self.assertEqual(result, 2)


    def test_f_max_of_three(self):
        result = math_func_max_of_three(47, 592, 234)
        self.assertEqual(result, 592)


    def test_f_rental_late_fee (self):
        result = math_func_rental_late_fee(36)
        self.assertEqual(result, 100)

if __name__ == '__main__':
    unittest.main()