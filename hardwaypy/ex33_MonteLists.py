#!/usr/bin/env python 	-tt

# ex33:  While Loops			 (file by mk.py)

"""
Flags argv:
- argv[0] is script itself  
- argv[1] is MaxListCount  
- argv[2] is Increment 
- argv[3] Display Options
	set to null then 1
	set to 1 = single value displayed per line at random starting point
	set to 2 = List appended inside list. all elements printed
	set to 3 = single value displayed per line at random tabbed point with arrows printed


In this exercise:
- main() calls other functions
- create a list
- append the list with increasing values
- append the list randomly with random sized whitespace:
  - Monte Carlo method used to determine frequency of list.append(whiteSpace)
  - whitespace size skewed toward lower range of randrange(0,maxWhiteSpaceLength)
    - skew algorithm: 
      (result of random in MaxRange) 
         [multiplied by] (result of random in MaxRange) / (maxRange) = %
         or whiteSpace = randX * (randX/maxX)

"""

import sys
import random

#############################CONTROLS###########################
###monte carlo ranges for easy control
#ex x = random from range(0,100); x must be LESS than thresholdValue {MonteCarlo}
thresholdMonte = 10  # if monte < maxMonte (out of MaxRandRange) then white space added
maxRandRange = 100 # for max possibilities of monte

maxRandWhiteSpaceRange = 50 # max possible bytes of white space to append
#############################CONTROLS###########################

# Define a main() function
def main():
	"""main calls the functions : central"""
	
	whileTest()
	



# Define function for practiving the while loop:
def whileTest():
	
	#declare and initialize globals
	
	#create argvs for range and increment
	if len(sys.argv) == 2:
		rangeArgv = int(sys.argv[1])
		increment = 1
	elif len(sys.argv) >= 3:
		rangeArgv = int(sys.argv[1])
		increment = int(sys.argv[2])
	else:
		rangeArgv = 10
		increment = 1
	
	i = 0
	numbers = [] 
	
	#define some globals
	incrementSkewed = 0
	#argvIncrement = increment #in case we need it lateer
	
#--debug:
	print "\n"
	print " rangeArgv = ", rangeArgv, "\tdata = %r" % type(rangeArgv)
	print " increment = ", increment, "\tdata = %r" % type(increment)
	print " len(sys.argv) = ", len(sys.argv)
	print " 'numbers' list = ", numbers
	print " i = ", i
	raw_input("\n\t-->Hit ENTER to continue ----------->")
	
	while i < rangeArgv:
		#print "\nLoops starts (again) ::: 'i' = %d :::" % i
		#print "Append the current value of i ('%d') to the 'numbers' list." % i, "\n"
		numbers.append(i)
		
		monte = random.randrange(0,maxRandRange)
		if monte < thresholdMonte:
			
			#reset increment to original value 
			#increment = argvIncrement
	
			#maxRandWhiteSpaceRange = 50
			
			#skew results toward low end
			whiteSpaceSize = float(random.randrange(0,maxRandWhiteSpaceRange))
			#print "\n\t-----initial whiteSpaceSize random value = ", whiteSpaceSize
			randRangeFloat = float(maxRandWhiteSpaceRange)  #weird things happening
			skewedRange = whiteSpaceSize/randRangeFloat
			skewedResult = whiteSpaceSize * skewedRange
			whiteSpaceBytesToInject = int(skewedResult)
			
###__Debug Skewed Behavior
			'''			
			print "Increase the likelihood of lower numbers in range %d" % randRange 
			print "\n\t-----initial whiteSpaceSize random value = ", whiteSpaceSize
			print "\n\t-----skewedRange Scalar = result/randRange  = ", skewedRange
			#skewedResult = whiteSpaceSize * skewedRange
			print "\n\t-----skewedResult = whiteSpaceSize * skewedRange  = ", skewedResult
			#whiteSpaceBytesToInject = int(skewedResult)
			print "\n\t---> whiteSpaceBytesToInject = ",whiteSpaceBytesToInject, "\n"
			'''
			
			#randomly append the numbers list with strings of varying white space
			strOfVaryingLength = " " *whiteSpaceBytesToInject
			numbers.append(strOfVaryingLength)
			lenOfListNumbers = len(numbers)
			
			
#			########################################################
			# MODES
			
			# displays as actual values if Flag is set to '1'
			if len(sys.argv) >= 4:
				if sys.argv[3] == '1':		
					print strOfVaryingLength,  numbers[lenOfListNumbers-2]
			if len(sys.argv) < 4:
					print strOfVaryingLength,  numbers[lenOfListNumbers-2]
			# displays as elements in a list (nested)
			if len(sys.argv) >= 4:
				if sys.argv[3] == '2':			
					print numbers

#			##############################################################

			
			#change the increment randomly.
			incrementSkewed = increment * (random.randrange(1, 100)/100)
			#Puts a break in the crazy loop list in list
			##raw_input('<------Hit ENTER to continue ------>')
		
		iCurrent = i
		i += increment
		
		#print "Add 1 to the current value of i (%d), such that" % iCurrent 
		#print "\n\tnew value of i (%d) = previous value of i (%d) + 1" % (i, iCurrent)
		
		################
		#list 'numbers' inside itself
		#print "\n\t-->Numbers Now in List:", numbers #cause big 0 to go
		################
		
	#print "/n------------------The list --->", numbers
	#print "/n------------------The numbers:  "
	#for num in numbers:
		#randTab = random.randrange(1,5)
	if len(sys.argv) >= 4:
		if sys.argv[3] == '3':
			for num in numbers:
				randTab = random.randrange(0,7)
				print "\t"*randTab, "--->", num#, "\n"


# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()