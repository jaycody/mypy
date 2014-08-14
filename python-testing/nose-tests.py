#!/usr/bin/env python -tt

""" jstephens - pyfu - nose tests

nose - unit test discovery and test execution package

to run this test from outside the working directory:

$ nosetests -vv -w python-testing nose-tests.py:test_b

$ nosetests -vv -w /jayjaycody/mypy/python-testing nose-tests.py:test_b

$ nosetests -vv -w /jayjaycody/mypy/python-testing nose-tests.py:testExampleTwo.test_example2
"""


import nose


def test_b():
	"""simplest test possible"""
	assert 'b' == 'b'



class testExampleTwo:
	def test_example2(self):
		"""class format nose test
		- unlike unittest format, nose assert does not require 'self.assert'
		"""
		assert 'c' == 'c'




nose.run()
