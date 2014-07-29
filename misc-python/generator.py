#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july

Tool for generating a list of numbers.

usage: 
	print to console:  $ ./generator [max num]
	write to file:     $ ./generator [max num] > numbers.txt
"""


import sys

lengthArg = len(sys.argv)
if lengthArg != 2:
	print "creates a list of numbers \nusage: ./generator.py [max num]"
	sys.exit(1)

maxNum = int(sys.argv[1])
print maxNum





n = 0
while True:
	print n
	n = n+1
	if n > maxNum:
		break



