#!/usr/bin/env python -tt

"""jstephen - pyfu - edx MIT.600 (intro to cs via py) 2014 july

Use Recursion To.....
A single location for all edxMIT600 python exercises involving Recursion.
Each exercise has its own function.

usage:
	--test  Runs doctests only

"""

import sys


def lenRecur(aStr):
	"""Use recursion to:  Compute the length of the input argument 
	by counting the number of characters in the string.
	----
	aStr:  a string
	returns:  int, the length of a string
	----
	>>> lenRecur('')
	0
	>>> lenRecur('stupendously')
	12
	"""	

	# Base Case
	if aStr == '':
		count = 0
		return count
	
	# n = n + (n-1)
	else:
		count = 1 + lenRecur(aStr[:-1])
		return count

def isIn(char, aStr):
	"""Use bisection search to recursively 
	determine if a specific letter exists in a string.
	----
	char: character to find
	aStr: string in which to search
	returns: boolean
	----
	1. Alphabatize the string
	2. test if char is in the middle of string :  if yes, then return
	3. test if char is above or below the middle of string.
	4. if above, check if char is halfway between middle and end.  repeat
	5. if below, check if char is halfway between middle and beginning.  repeat
	----
	>>> isIn('a', 'Jason')
	True
	"""


	###########################################################
	# base case
	aStr = sorted(aStr)
	n = int(len(aStr)/2)
	print "n = %d" % n

	if char == aStr[n]:
		return True

	if char == aStr[len(aStr)/2]:
		return True

	elif char != aStr[len(aStr)/2]:
		# if char is greater than center point, then divide upper half and repeat
		if char > aStr[len(aStr)/2]:
			# then the new list of chars to search is from half way to the end
		
			return isIn(char, aStr[len(aStr)/2:])

		elif char < aStr[len(aStr)/2]:
			return isIn(char, aStr[:len(aStr)/2])

		else:
			return False
	else:
		return False

	sys.exit(0)
	###########################################################




def main():
	"""Main function for handling all recursive functions in this script
	"""

	if len(sys.argv) < 3:
		print "usage:  ./recursion.py function_name input"
		print "====functions:"
		print "      lenRecur(aStr)"
		print "      isIn(char, aStr)"
		sys.exit(1)
	
	function = sys.argv[1]

	if function == 'lenRecur':
		lenStr = lenRecur(sys.argv[2])
		print "Length of string: '%s' = %d" % (sys.argv[2], lenStr)
	#elif function == '_______':
	if function == 'isIn':
		if len(sys.argv) == 4:
			resultsIsIn = isIn(sys.argv[2], sys.argv[3])
			print resultsIsIn
		else:
			print 'usage:  ./recusion.py isIn char aStr'
	else:
		print 'unknown function: ' + function


if __name__ == '__main__':	
	
	main()

