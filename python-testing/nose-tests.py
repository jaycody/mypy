#!/usr/bin/env python -tt

""" jstephens - pyfu - nose tests

nose - unit test discovery and test execution package
"""


def test_b():
	"""simplest test possible"""
	assert 'b' == 'b'



class testExampleTwo:
	def test_example2(self):
		"""class format nose test
		- unlike unittest format, nose assert does not require 'self.assert'
		"""
		assert 'c' == 'c'





