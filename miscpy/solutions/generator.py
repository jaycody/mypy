#!/usr/bin/env python -tt

"""jstephens - pyfu - v.tutorial - 2013

Generates list of numbers.
Prints to console or output to text file as follows

Usage: $ python ./generator.py > numbers.txt
"""

n = 0
while True:
	print n
	n = n+1
	if n > 200:
		break