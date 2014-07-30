#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july

Script containing functions for edx chapter on objects
"""

import sys
import random



def oddTuples(aTup):
	"""Find and return the odd indexed entries in tuple arguments.
	Write a procedure called oddTuples, 
	
	aTup --> input tuple
	returns --> tuple
	
	where every other element of the input tuple is copied, 
	starting with the first one. 
	-------------
	>>> oddTuples(('I', 'am', 'a', 'test', 'tuple'))
	output tuple =  ('I', 'a', 'tuple')
	"""

	#print aTup
	newTup = ()

	lenTup = len(aTup)

	for i in range(lenTup):
		if i % 2 == 0:
			# create a singleton
			newTup = (newTup + (aTup[i],))
	print "output tuple = ", newTup

	## How are tuples poputlated?  Via iteration?

	return newTup



def findDivisors(n1, n2):
    """assumes n1 and n2 positive ints!
    returns tuple containing!
    common divisors of n1 and n2
    """

    # find all divisors of smallest int, then check if divides into other int.
    small = min(n1, n2)
    large = max(n1, n2)
    tupCommon = ()

    smallDivisors = []
    commonDivisors = []
    for i in range(small+1):
    	if i != 0:
    		if small % i == 0:
    			smallDivisors.append(i)
    			commonDivisors.append(i)
    #print smallDivisors 

    
    for num in smallDivisors:
    	if large % num != 0:
    		commonDivisors.remove(num)
    print ""
    print small, "is divisible by: ", smallDivisors
    print small, "and", large, "share the following divisors:", commonDivisors


    for item in commonDivisors:
    	tupCommon = tupCommon + (item,)

    print "tupCommon = ", tupCommon

def tryExcept():
	"""Print a reminder list of the essentials for try, exception, else, finally
	"""

	listToTry = ['try:', 'except', 'else:', 'finally:']

	for item in listToTry:
		print item

def testExceptions():
	"""Test exercises using try/except
	"""
	
	"""
	try:
		print d
	except:
		raise Exception("check var types")
	"""	
	
	try: 
		print d
	except NameError, e:
		print "raised NameError.  Setting d to new string\n" + str(e)
		d = raw_input('enter new string:  ')
	else:
		print "unreachable code, because 'try' here will always fail"
	finally:
		print "\nand finally, FINALLY always gets the last word"
	print "\nprinting new string:  ", d




def main():
	"""Process the command line arguments.
	"""

	function = sys.argv[1]
	aTup = ('I', 'am', 'a', 'test', 'tuple')

	if function == '--oddTuples':	
		oddTuples(aTup)

	if function == '--findDivisors':
		for i in range(10):
			n1 = random.randint(1, 1000)
			n2 = random.randint(1, 2000)
			findDivisors(n1, n2)

	if function == '--testExceptions':
		testExceptions()

	if function == '--tryExcept':
		tryExcept()

if __name__ == "__main__":

	main()


