#! /usr/bin/python -tt

"""Unit tests fr the hello_ops script
"""

import sys
import unittest

from a_hello_ops import get_input


# verify module import

#print get_input()


# unittest class
class TestHelloOps(unittest.TestCase):

    def test_get_input(self):
        """Check if test value equals return value
        """

        ans = int(raw_input('\nEnter value to verify:'))
        x = get_input()
        print 'From test_get_input: x = {}'.format(x)
        self.assertEqual(x, int(ans))
        print '\n--> Checking if value to verify:{} = input:{}'.format(ans, x)


if __name__ == '__main__':
    unittest.main()
