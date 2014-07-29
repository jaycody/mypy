#primeGenerator
import math

def isPrime(n):
	if n < 2:
		return False
	possibleDivisor = 2
	while possibleDivisor <= math.sqrt(n):
		if n % possibleDivisor == 0:
			return False
		possibleDivisor += 1
	return True

fileRef = open('numbers.txt')
allLines = fileRef.readlines()
for line in allLines:
	n = line.rstrip('\n')
	n = int (n)	
	if isPrime(n):
		print n
fileRef.close()



