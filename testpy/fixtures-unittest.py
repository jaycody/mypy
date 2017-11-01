#!/usr/bin/env python -tt

""" jstephens - pyfu - fixtures in unittest

Implement unittest fixture syntax for test functions, class, module.


#test function syntax           setUp() / tearDown()

#test class syntax              @classmethod: setUpClass() / tearDownClass()

#test module syntax             setUpModule() / tearDownModule()

_____________________________________
CLI for this module:

     $ python -m unittest -vv -q fixtures-unittest
# where
"""



import unittest 
import inspect


# module level fixtures
def setUpModule():
	print '\nrunning module level setUp fixture'

def tearDownModule():
	print '\nrunning module level tearDown fixture'




class TestExampleClass(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print "\nrunning class level setUp fixture ONCE before running a single test from this class."

	@classmethod
	def tearDownClass(cls):
		print "\nrunning class level tearDown fixture ONCE after running all tests from this class."


	def setUp(self):
		print "\nrunning function level setUp fixture for EACH test in this class"
	
	def test_a(self):
		print 'running test_a()'
		print 'self.id() = ' + self.id()
		self.assertEqual('a', 'a')

	def test_b(self):
		print "running test_b()"
    	assert 'b' == 'b'

	def tearDown(self):
		print "running function level tearDown fixture for EACH test in this class"






if __name__ == '__main__':

	unittest.main()
