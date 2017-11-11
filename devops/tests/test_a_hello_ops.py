#! /usr/bin/python -tt

"""Unit tests fr the hello_ops script
"""

import sys
import unittest

# from a_hello_ops import get_input
import a_hello_ops


# verify module import

#print get_input()


# unittest class
class TestHelloOps(unittest.TestCase):

    def test_get_input(self):
        """Verify returns expected value

        """

        #ans = int(raw_input('\nEnter value to verify:'))
        ans = 100
        x = a_hello_ops.get_input(ans)
        print '\n\nFrom test_get_input: x = {}'.format(x)
        self.assertEqual(x, int(ans))
        print '--> Checking if value to verify:{} = input:{}'.format(ans, x)

    def test_print_hello_devops_to_console(self):
        """Verify returns expected value"""

        expect = 9
        got = a_hello_ops.print_hello_devops_to_console(expect)
        self.assertEqual(expect, got)

if __name__ == '__main__':
    unittest.main()
