#! /usr/bin/python -tt

# usage from c_calc.py/: python tests/test_c_calc.py

import unittest

from c_calc import Calculate


class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculate()


    ###############################
    ### verify it works as expected

    def test_add_inputs_returns_correct_result(self):
        self.assertEqual(4, self.calc.add_inputs(2, 2))


    ###############################
    ### verify it breaks as expected

    def test_add_input_fails_as_expected(self):
        """Test that sending strings forces correct error message"""

        response = self.calc.add_inputs('h', 'i')
        expected = type('str'), type('str')
        self.assertEqual(expected, response[0:2])


if __name__ == '__main__':
    unittest.main()
