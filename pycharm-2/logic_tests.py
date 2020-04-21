import math
import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_f_is_even(self):
        result = is_even(22)
        self.assertEqual(result, True)
        result = is_even(12345)
        self.assertEqual(result, False)

    def test_f_in_an_interval(self):
        result = in_an_interval(49)
        self.assertEqual(result, True)
        result = in_an_interval(105)
        self.assertEqual(result, False)
        result = in_an_interval(9)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()