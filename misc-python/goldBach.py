#!/usr/bin/env python -tt

"""Vs Tuesday Tutorials : 20130306 

Test the GoldBach Conjecture

Assignment:
	1. Write a python script that will test the GoldBach conjecture for all integers 4-100
		Clues:
		'every even number greater than 2 can be expressed as a sum of two primes
		print the primes in each case
		generate a list of primes and then add each one to each other one 

	2. Use big o notation to report on the time complexity of the script
		O(someExpression)

	3. Install python debugger module into [sublime text 2](https://pypi.python.org/pypi/PdbSublimeTextSupport)

	4. Please read the presentation that uncle V gave me re: interface''
"""


import math, pdb


def isPrime (possibleDivisor, n):
	"""Determine if input n is prime.
	"""

	if n < 2:
		return False
	if possibleDivisor == n:
		return True
	if n % possibleDivisor == 0:
		return False
	if possibleDivisor >= math.sqrt(n):
		return True
	return isPrime(possibleDivisor + 1, n)
	

fileRef = open('numbers.txt')
allLines = fileRef.readlines()
for line in allLines:
	n = line.rstrip('\n')
	n = int (n)	
	if isPrime(2, n):
		print n
fileRef.close()

