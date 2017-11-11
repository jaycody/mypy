#! /usr/bin/python -tt

import unittest

import b_counter

class TestCounter(unittest.TestCase):

    def test_count_function_returns_default(self):

        default_expected = 'from default val, yo'
        total_expected = len(default_expected)

        # dig on the multiple assigment tuple unpack thingy
        default_returned, total_returned = b_counter.count()

        self.assertEqual(default_expected, default_returned)
        ## wait, shouldn't this be a different test?
        #self.assertEqual(total_expected, total_returned)
