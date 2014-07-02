#! /usr/bin/env python


"""j.stephens  ==> mypy gongfu - Think Python - Chpt 4: Draw 2D shapes of n-fold symmetry
Dependencies:  poly2.py

command line arguments:

drawShape.py { number of polygon sides , length of each side , number of iterations}

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

# Defaults in no command line arg
defaultShapeSides = 2
defaultShapeLength = 50
defaultShapeIterations = 10
defaultShapeRadius = 10
defaultShapeAngle = 120


# argv tests
"""
	#########################################################
	def getDimension(argvIndex):
		'''takes command line arg for number of sides of polygon.
		When no input present, uses default num of sides
		'''

		#
		if argvIndex+1 > len(sys.argv):
			return 5  	#default to pentagon
			
		else:
			dimension = int(sys.argv[argvIndex])
			#print dimension
			return dimension

	'''  TEST ARGV ##############
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
	'''
	##########################################################
"""

"""
## Get argv and make simple shape
	# get argvs
	getN = getDimension(1)
	getLength = getDimension(2)
	numShapes = getDimension(3)

	for shape in range(numShapes):
		polygon(t=bob ,length=getLength*3 ,n=getN+shape)
		drawSquare(lt, bob, shape*5)
		#polygon(t=bob ,length=(numShapes-shape)*3 ,n=numShapes-shape+3)
		#arc(bob, radius*(shape*.5)+1, angle*shape+1)
		drawSquare(rt, bob, shape*20)
"""

def drawDefaultShape():
	"""Draw a default shape when no command line arguments are used"""
	
	print ""
	print "-----------Drawing Default Shape-----------"
	print "\n"
	print "***To draw polygons or arcs, use command line input as follows:"
	print "=====> [poly | arc], [num of sides (for polygon) | theta (for arc)]"
	print "\n", "\n" 
	
	for shape in range(defaultShapeIterations):
		polygon(t=bob, n=(defaultShapeSides + shape),
				length=defaultShapeLength+(defaultShapeLength*(shape/defaultShapeIterations)))

def drawDefaultPoly():
	"""Draw the default polygon when only 'poly' is detected in commmand line"""
	print ""
	print "-----------Drawing Default Polygon-----------"
	print "\n"
	print "***To draw polygons or arcs, use command line input as follows:"
	print "=====> [poly | arc], [ 'n= ' (num of sides for polygon) | 'theta= '(for arc)]"
	print "_____________>>> example:  $ ./drawShape.py poly n=6"
	print "\n", "\n" 
	polygon(t=bob, n=5, length=60)


def checkArgv():
	"""Process command line arguments.  Act accordingly."""

	# If no cmd line args, draw default shape
	if len(sys.argv) < 2:
		drawDefaultShape()

	# If the only argument is 'poly', then draw the default polygon	
	if "poly" in sys.argv and len(sys.argv) == 2:
			drawDefaultPoly()


if __name__ == '__main__':

	checkArgv()
	
	"""
	if argvIndex+1 > len(sys.argv):
		return 5  	#default to pentagon
		
	else:
		dimension = int(sys.argv[argvIndex])
		#print dimension
		return dimension
	"""


	wait_for_user()

