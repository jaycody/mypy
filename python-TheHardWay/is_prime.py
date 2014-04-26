#!/usr/bin/env python 	-tt

# is_prime.py			 (file by mk.py)

"""


"""

import sys
import random
#from random import randint

def is_prime(x):
  for num in range (2,x):
    if x % num == 0:
    	print x
    	print num
      	print "\n\t--> %d is Not Prime:  %d is divisilbe by %d" % (x, x, num), "\n"
      	return False
    else:
      	print "\n\t--> %d IS Prime:  %d is divisilbe only by 1 and %d" % (x, x, x), "\n"
     	return True
            

# Define a main() function
def main():
	"""documentation comments here"""
	
	if len(sys.argv) >=2:
		argvToTest = int(sys.argv[1])
		ans = is_prime(argvToTest)
	else:
		#ans = is_prime(sys.argv[1])
		checkPrime = random.randint(2, 100000)
		ans = is_prime(checkPrime)
		#print ans






# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()