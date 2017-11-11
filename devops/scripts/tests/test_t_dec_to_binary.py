#! /usr/bin/python -tt

import unittest

from t_dec_to_binary import convert_to_binary


class TestConversion(unittest.TestCase):

    def test_convert_to_binary_function_exists(self):
        exist = convert_to_binary(1)
        self.assertTrue(exist)



if __name__ == '__main__':
    unittest.main()
