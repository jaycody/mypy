#! /usr/bin/python -tt

# usage from calculator_app/: python test/unit/calculate_this_test.py

import unittest2

from calculate_this import Calculate


class TestCalculate(unittest2.TestCase):

    def setUp(self):
        self.calc = Calculate()


    ###############################
    ### verify it works as expected

    def test_add_inputs_returns_correct_result(self):
        self.assertEqual(4, self.calc.add_inputs(2, 2))


    ###############################
    ### verify it breaks as expected

    def test_add_inputs_raises_type_error_for_non_ints(self):
        self.assertRaises(TypeError, self.calc.add_inputs, 'Hello', 'Again')

    def test_add_inputs_raises_attribute_error_on_non_existent_method_call(self):
        with self.assertRaises(AttributeError):
            [].get


if __name__ == '__main__':
    unittest2.main()
