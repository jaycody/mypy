#! /usr/bin/env python


"""j.stephens  ==> mypy gongfu - Think Python - Chpt 4: Draw 2D shapes of n-fold symmetry
Dependencies:  poly2.py


"""
# gets argv from command line
import sys

# helps loops through argvs
import fileinput


from swampy.TurtleWorld import *
from poly2 import *


world = TurtleWorld()
bob = Turtle()
jay = Turtle()

bob.delay = 0.0001
jay.delay = 0.0001

length = 50
n = 6
radius=10
angle=39



#########################################################
def getDimension(argvIndex):
	'''takes command line arg for number of sides of polygon.
	When no input present, uses default num of sides
	'''

	if argvIndex+1 > len(sys.argv):
		return 5  	#default to pentagon
		
	else:
		dimension = int(sys.argv[argvIndex])
		#print dimension
		return dimension

"""  TEST ARGV ##############
## TEST ARGV value and type
# Acquire argv value at index 1
d = getDimension(1)
print d
print "variable type = ", type(d)


# TEST argv values at each index
for i in range(len(sys.argv)):
	print sys.argv[i]

# TEST length of argv array
lengthArgsArray = len(sys.argv)
print "length of arvg Array =", lengthArgsArray
"""
##########################################################


# get argvs
getN = getDimension(1)
getLength = getDimension(2)
numShapes = getDimension(3)

##############################
#### argv Draw 
##############################


polygon(t=bob ,length=getLength ,n=getN)

#############################
## Direct DRAW
#############################

#drawSquare(rt, bob, 40)
#circle(t=bob ,r=400)				# using KEYWORD ARUGMENTS

##############################
#### Iterated Draw 
##############################

for shape in range(numShapes):
	drawSquare(lt, bob, shape*5)
	#polygon(t=bob ,length=(numShapes-shape)*3 ,n=numShapes-shape+3)
	#arc(bob, radius*(shape*.5)+1, angle*shape+1)
	drawSquare(rt, bob, shape*20)



wait_for_user()