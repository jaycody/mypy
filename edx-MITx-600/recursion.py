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
	>>> isIn('n', 'Bodhi')
	False
	"""


	# DEBUG BOOLEAN ('--test')
	DEBUG = False
	if len(sys.argv) > 4:
		if sys.argv[4] == '--test':
			DEBUG = True
		elif sys.argv[4] != '--test':
			print "\n unknown option: " + sys.argv[4]
			print "-------->>> usage for 5th param: ./recursion isIn char aStr { --test | NULL }"
			sys.exit(1)
		
	# SORT the string FIRST:  (returns a list)
	if DEBUG:
		print "\n-------> char to find: '%s'    \n---> string to search:  %s" % (char, aStr)

	aStr = sorted(aStr)
	# convert the sorted list back to a string by joining on empty spaces
	aStr = ''.join(aStr)

	# Caclulate the string's midpoint index in order to find the midway character
	midwayIndex = len(aStr)/2
	midwayChar = aStr[midwayIndex]
	
	# DEBUG (sys.argv[4] == '--test')
	if DEBUG:
		print ""
		print "---> SORTED string to search = ", aStr
		print "midwayIndex = ", midwayIndex
		print "midwayChar = ", midwayChar

		print ""
		print "-> start of string to midway point ===> \n      aStr[:midwayIndex] = ", aStr[:midwayIndex]
		print "\n-> midway point to end of string  ===> \n     aStr[midwayIndex:] = ", aStr[midwayIndex:]
		print ""



	###### base cases ############################

	# Base Case 1:  Char is not the final letter
	if len(aStr) == 1:
		if char != aStr[0]:
			# DEBUG
			if DEBUG:
				print "length of string is 1 and char: '%s' is NOT '%s'" % (char, aStr[0])
				print "-----Returning False"
			return False

	# Base Case 2:  Zero chars remain in string
	if len(aStr) == 0:
		return False

	# Base Case 3:  Char IS in the string
	if char == aStr[len(aStr)/2]:

		## DEBUG ('--test') ##########################
		if DEBUG:
			print "is '", char, "' midway in string", aStr, "?"
			print "yes:", char, "=", midwayChar
		#############################################
		#print 'return true'
		return True

	#########################################


	###### Recursive Calls ###########################
	
	if char > aStr[len(aStr)/2]:
		if DEBUG:
			print char, "is greater than", midwayChar
			print "\n reduce searchable string from:  ", aStr
		aStr = aStr[len(aStr)/2:]
		if DEBUG:
			print "to:  ", aStr
			print " ------ and repeat ------"
		return isIn(char, aStr)

	if char < aStr[len(aStr)/2]:
		if DEBUG:
			print char, "is less than", midwayChar
			print "\n reduce searchable string from:  ", aStr
		aStr = aStr[:len(aStr)/2]
		if DEBUG:
			print "to:  ", aStr
			print " ------ and repeat ------"
		return isIn(char, aStr)

def palindrome(str1, str2):
	"""Determine (recursively) if two strings are palindromes of each other.

	# Does the first letter of str1 == first letter of str2?

	# Write a recursive function that does this::: ====>
	if str1 == str2[::-1]:
		return True
	else:
		return False
	##---------------------
	"""

	# if first letter of str1 == first char of str2, then call recursively,
	#   else, return falst

	if len(str1) > 1 and len(str2) > 1:

		if str1[0] == str2[-1]:
			str1 = str1[1:]
			str2 = str2[:-1]
			return palindrome(str1, str2)
		else:
			return False
	else:
		return True
		

	sys.exit(0)

def palindrome_wrapper(str1, str2):
	"""Assist the palindrome function by handling the initial check of str1 and str2.
	A wrapper function to handle the global scope of the first iteration
		Where to use the wrapper function:
			1. a str of len 1 is a palindrome 
			2. equal strings cannot be (meaningful palindromes of each other)
	Base Case 1. Are str1 and str2 equal?  
	Base Case 2. Are the strings of length 1?
	3. If we can proceed, then  call the palindrome function.
	
	>>> palindrome_wrapper('god', 'dog')
	True
	>>> palindrome_wrapper('tact', 'cat')
	False
	"""
	str1 = str1.lower()
	str2 = str2.lower()

	if str1 == str2:
		return False

	elif len(str1) != len(str2):
		return False
	elif len(str1) == 1 or len(str2) == 1:
		return False 

	else:
		return palindrome(str1, str2)

def recurs_exponent(base, exponent):
	"""Recursively calculate the product when the base is raised to the given exponent.
	>>> recurs_exponent(5, 2)
	25
	"""
	## Non-recursively looks like this:
	"""
	total = base
	for i in range (exponent-1):
		total = total * base
	print total
	"""

	if exponent == 0:
		return 1
	if exponent == 1:
		return base
	if exponent > 1:
		return base * recurs_exponent(base, exponent-1)




def main():
	"""Main function for handling all recursive functions in this script
	"""

	if len(sys.argv) < 3:
		print "usage:  ./recursion.py function_name input"
		print "====functions:"
		print "      lenRecur [aStr]"
		print "      isIn [char] [aSt]"
		print "      palindrome [str1] [str2]"
		print "      recurs_exponent [base] [exponent]"
		sys.exit(1)
	
	function = sys.argv[1]

	if function == 'lenRecur':
		lenStr = lenRecur(sys.argv[2])
		print "Length of string: '%s' = %d" % (sys.argv[2], lenStr)

	if function == 'isIn':
		if len(sys.argv) >= 4:
			#resultsIsIn = isIn(sys.argv[2], sys.argv[3])
			char = sys.argv[2]
			aStr = sys.argv[3]
			resultsIsIn = isIn(char, aStr)
			print "\n ====>   Is '%s' in string: %s  ??\n" % (char, aStr)
			if resultsIsIn:
				print "-------- YES:  '%s' IS in string: %s \n" % (char, aStr)
			else:
				print "-------- NO:  '%s' is NOT in string: %s \n" % (char, aStr)
			
		else:
			print 'usage:  ./recusion.py isIn char aStr'
	
	if function == 'palindrome':
		if len(sys.argv) != 4:
			print "usage:  ./recursion.py palindrome str1 str2"
		elif len(sys.argv) == 4:
			str1 = sys.argv[2]
			str2 = sys.argv[3]
			isPalindrome = palindrome_wrapper(str1, str2)
			print isPalindrome

	if function == 'recurs_exponent':
		if len(sys.argv) != 4:
			print "usage: ./recursion.py recurs_element [base] [exponent]"
		else:
			base = int(sys.argv[2])
			expo = int(sys.argv[3])
			ans = recurs_exponent(base, expo)
			print ans
	
	else:
		print 'unknown function: ' + function


if __name__ == '__main__':	
	
	main()

