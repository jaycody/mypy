#! /usr/bin/python -tt

import unittest

from calculate_this import Calculate



class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.calc = Calculate()

    def test_add_inputs_returns_correct_result(self):
        self.assertEqual(4, self.calc.add_inputs(2,2))

if __name__ == '__main__':
    unittest.main()
