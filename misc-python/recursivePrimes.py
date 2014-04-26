#recursively solving for primes
import math, pdb


def isPrime (possibleDivisor, n):
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