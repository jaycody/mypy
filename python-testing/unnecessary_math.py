#!/usr/bin/env python -tt

"""jstephens - pyfu - mutliply module for nose examples

"""



def multiply(x, y):
	"""multiply args and return results.
	>>> multiply(4, 3)
	12
	"""
	return x * y



def test_multiply():
	"""test the multiply function"""
	ans = multiply(5, 6)
	assert ans == 30

	

