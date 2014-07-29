#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july

Variety of number manipulations
"""

import sys

def create_fileRef(filename):
	"""Create and return a file object
	"""
	fileRef = open(filename)
	return fileRef

def evens(fileRef):
	"""Create a list of even numbers from 0 - n.
	fileRef:  file object passed from main()
	"""
	
	# Make a list where each element is a single line from file object
	allLines = fileRef.readlines()
	# extract the number n from each line of the text
	for line in allLines:
		# strip white space
		n = line.rstrip('\n')
		### what's the difference between foo.rstrip() and foo.strip()??"
		#print type(n)
		n = int(n)
		# only print the evens
		if n % 2 == 0 or n == 0:
			print n

		fileRef.close()


def main():
	"""Handle command line args.
	"""
	lenInput = len(sys.argv)
	if lenInput != 3:
		print "usage:  ./math_exercises.py [--function name] [--input filename]"
		sys.exit(1)

	function = sys.argv[1]
	filename = sys.argv[2]

	# Create a file object from specified file containing list of numbers
	fileRef = create_fileRef(filename)
	
	if function == '--evens':
		evens(fileRef)


	else:
		print "unknown function: " + function
		sys.exit(1)


if __name__ == '__main__':

	main()