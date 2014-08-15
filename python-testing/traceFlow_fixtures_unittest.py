#!/usr/bin/env python -tt

""" jstephens - pyfu - unittest test fixtures with control flow tracer utility function


from Brian Okken's unittest fixtures tutorial
http://pythontesting.net/framework/unittest/unittest-fixtures/

create 2 traceFlow utility methods:
1) inside the class to trace methods via self.traceFlow()
2) outside the class to trace module and class via traceFlow(currentContext)
"""



import unittest

import inspect 



## Module Fixtures

def setUpModule():
	print ''
	traceFlow('module: %s' % __name__)

def tearDownModule():
	traceFlow('module: %s' % __name__)

## Control Flow Tracer Utlity
def traceFlow(currentContext):
	callingFunction = inspect.stack()[1][3]
	#print " %s  ==> %s()" % (currentContext, callingFunction)
	if currentContext[0] == 'm':        # if it's the module
		print "- for %s  ==> running: %s()" % (currentContext, callingFunction)
	elif currentContext[0] == 'c':        # if it's the class
		print "--- for %s  ==> running: %s()" % (currentContext, callingFunction)

class TestFlowTraceFixtures(unittest.TestCase):

	## Class Fixtures
	@classmethod
	def setUpClass(cls):
		traceFlow('class: %s' % cls.__name__)

	@classmethod
	def tearDownClass(cls):	
		print ''
		traceFlow('class: %s' % cls.__name__)

	## Method Fixtures
	def setUp(self):
		print''
		self.traceFlow()
		

	def tearDown(self):
		self.traceFlow()

	## Tests
	def test_a(self):
		self.traceFlow()
		assert 'a' == 'a'

	def test_b(self):
		self.traceFlow()
		self.assertEqual(1, 1)
		self.assertEqual(0, 0)

	def test_c(self):
		self.traceFlow()
		self.assertTrue(1)

	def traceFlow(self):

		# Get current test by spliting the string into a list and removing the last element
		currentTest = self.id().split('.')[-1]
		# Get calling function (3rd index from the tuple found at list index 1)
		callingFunction = inspect.stack()[1][3]

		#return (callingFunction, currentTest)
		print "---- for: %s  running ==> %s()" % (currentTest, callingFunction)



if __name__ == '__main__':

	unittest.main()
