#!/usr/bin/env python -tt

""" jstephens aug 2014 - unittest simple usage exercise

Use unittest framework to run a series of generic tests against basic math operations
- create TestCase classs
- create test cases using test methods with 'test_foo' syntax

Next:
- create test fixture using setup() and teardown()

Command Line Interface:

# to run unittest:
	$ python -m unittest -v gen-unittest    #### --> note: no '.py' on script title
# or
	$ python -m unittest -v gen-unittest.mathTest    #### --> note: no '.py' on script title
# or
	$ python -m unittest -v gen-unittest.mathTest.test_add    #### --> note: no '.py' on script title

	
# to run doctest
$ python -m doctest -v gen-unittest.py    #### --> note: ADD '.py' to script title
"""


import unittest

class mathTester(unittest.TestCase):

	def test_add(self):
		"""verify python's ability to add.
		Create test method with unittest framework
		>>> 1 + 2
		3
		"""
		self.assertEqual((1+2), 3)
		#self.assertEqual((5+5), 9)

	def test_sub(self):
		"""verify python's ability to subtract.
		Create test method with unittest framework
		>>> 5 - 3
		2
		"""
		self.assertEqual((5-3), 2)
		'''
		try:
			self.assertEqual((5-3), 0)
		except:
			raise Exception("Failed the subtraction portion and found this exception messaage")
		'''

	def test_dataType(self):
		"""Evaluate a callable object and Use assertRaises(exception)
		The assertion here is that these evaluations will fail!
		When the evaluation doesn't fail, the assertion is wrong, throwing an error
		"""
		#  
		#self.assertRaises(ValueError, int, '8ca2', base=16)
		self.assertRaises(ValueError, int, 'stringCheese')

	def test_fail(self):
		"""Call fail function"""
		# condition is expected to 
		if not 2 > 5:
			self.fail('2 is not not less than 5')


# BOILERPLATE:

# standard boilerplate 
#    to run from command line:
#			$ pythoon -m unittest -v gen-utilities

"""
if __name__ == '__main__':
	
	unittest.main()
"""


# Instead of unittest.main(), use TestLoader() and TextTestRunner() for finer control
# Create a Test Suite as the boiler plate and alter command line interface:
#   $

# store individual tests methods in the 'suite' variable
suite = unittest.TestLoader().loadTestsFromTestCase(mathTester)

#create a test runner
unittest.TextTestRunner(verbosity=2).run(suite)

