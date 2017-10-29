#! /usr/bin/python -tt

# usage from calculator_app/: python test/unit/calculate_this_test.py

import unittest

from calculate_this import Calculate



class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculate()

    def test_add_inputs_returns_correct_result(self):
        self.assertEqual(4, self.calc.add_inputs(2, 2))

    def test_add_inputs_raises_type_error_for_non_ints(self):
        self.assertRaises(TypeError, self.calc.add_inputs, 'Hello', 'Again')

if __name__ == '__main__':
    unittest.main()
