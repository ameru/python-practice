import math
import unittest
from lab2_funcs_tests import *

# star means everything
# for unit testing, you have to know the expected value
# 'pass' function skips over test case

# Run the unit tests.
    # if __name__ == '__main__':
    # unittest.main()

class TestCases(unittest.TestCase):

    def test_f_1(self):
        result = math_func1(1, 2)
        self.assertEqual(result, 5/8)

    def test_f_2(self):
        result = math_func2(1, 0, -2)
        self.assertEqual(result, math.sqrt(8)/2)

    def test_f_d(self):
        result = math_func_d(4, 2, 3, 1)
        self.assertEqual(result,math.sqrt(2))

    def test_f_is_negative(self):
        result = math_func_is_negative(2)
        self.assertEqual(result, False)