# factorial

import sys
from sys import argv

def factorialNOT(valToCalculate):
	print "\n\t-----> Calculate factorial for: %d" % valToCalculate, "\n"
	
	#Accumulators:
	listToHoldTheDigits = []
	currentVal = 1
	totalValue = 0
	
	#Convert to string and prep for slicing
	strOfVal = str(valToCalculate)
	
	#Look at each value in the string and convert to int
	for num in strOfVal:
		intValOfNum = int(num)
		listToHoldTheDigits.append(num) 
		currentVal += currentVal * intValOfNum	
	
	totalValue = currentVal  					#hand of the accumulated results from forloop
	
	# Make it look like: "a * b * c * d * ...n
	strOfFactorialExpression = " * ".join(listToHoldTheDigits)
	print "\t", strOfFactorialExpression, " = \n\t"
	
	print "\t", totalValue
	
	sys.exit()

def factorial(x):

	# factorial of n = n*n-1
	
	for num in range (x,0,-1):
		print num
		
		if num <= 1:
			return 1
		else:
			return num * (factorial(num-1))
		
	
	
	



def main():
	if len(sys.argv) >= 2:
		factorThis = int(sys.argv[1])
		ans = factorial(factorThis)
		print ans
	else:
		print"\n ---- enter value to caluclate:   ",
		userDefinedVal = raw_input('>    ')
		userDefinedVal = int(userDefinedVal)
		ans = factorial(userDefinedVal)
		print ans
		
		
		
		sys.exit()
	
	
	
	
main()


'''if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)
    
'''