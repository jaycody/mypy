#!/usr/bin/env python -tt

"""jstephens - pyfu - 2014 july

Variety of number manipulations
"""

import sys

# my home made module
import file_reader


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

def odds():
	"""Use a list of numbers from an external file to create a list of odd nums
	"""

	fileRef = file_reader.get_fileRef('numbers.txt')

	allLines = fileRef.readlines()
	for line in allLines:
		n = line.rstrip('\n')
		n = int(n)
		if n % 2 == 1:
			print n
	fileRef.close()

def generator(maxNum):
	"""Prints a list of numbers of specified length
	"""
	#fileRef = open('morenums.txt', 'r+')
	n = 0
	while True:
		print n
		n = n +1
		if n > maxNum:
			break

def isPrime(n):
	"""Determine if n is prime
	"""

	'''
	# Hhahahahah === the wrong way
	for n in range(maxNum):
		for divisor in range(n):
			if divisor != 0:
				if divisor != 1:
					if divisor != n:
						if n % divisor == 0:
							print "%d is prime " % (n)
							#print '%d is not prime.  Dividable by %d' % (n, divisor)
							break
						else:
							print '%d is not prime.  Dividable by %d' % (n, divisor)

	'''
	if n < 2:
		print "%d is not prime" % n
		return False

	possibleDivisor = 2

	# One number of the 2 multiples needs to be less than the square root
	#while possibleDivisor <= math.sqrt(n)
	#isPrime = True
	for i in range(possibleDivisor):
		if n % possibleDivisor == 0:
			print "%d is not prime.  Divisible by %d" % (n, possibleDivisor)
			return False

		possibleDivisor += 1
	print "%d is prime." % n
	return True
	#fileRef = file_reader.get_fileRef('numbers.txt')

	# Define Prime:  divisible by 1 and by itself only.
	#for i in range(100):


def main():
	"""Handle command line args.
	"""
	lenInput = len(sys.argv)
	if lenInput != 3:
		print "usage:  ./math_exercises.py [--function name] [--input filename | NULL]"
		sys.exit(1)

	function = sys.argv[1]
	filename = sys.argv[2]

	# Create a file object from specified file containing list of numbers
	fileRef = create_fileRef('numbers.txt')
	

	if function == '--evens':
		evens(fileRef)

	if function == '--odds':
		odds()	

	if function == '--generator':
		generator(int(sys.argv[2]))

	if function == '--isPrime':
		isPrime(int(sys.argv[2]))
	else:
		print "unknown function: " + function
		sys.exit(1)


if __name__ == '__main__':

	main()