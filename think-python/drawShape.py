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


# Defaults in no command line arg
defaultShapeSides = 2
defaultShapeLength = 50
defaultShapeIterations = 10
defaultShapeRadius = 10
defaultShapeAngle = 120

# Defaults for Polygon when no arguments are presented in the command
defaultPolygonSides = 5
defaultPolygonLength = 100

# Defaults for Arcs
defaultArcRadius = 100
defaultArcAngle = 180


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
def commandLineInstructions():
	"""Print to console the arguments for shape drawing.  Include specifics
	from command line arguments
	"""
	print ""
	print "-----------Drawing Shape-----------"
	print "\n"
	print "---------To draw polygons or arcs, use command line input as follows:"
	print ""
	print "=====> [poly | arc], [ 'n= ' (num of sides for polygon) | 'angle= '(for arc)]"
	print ""
	print "_____________>>> example:  $ ./drawShape.py poly n=6"
	print "_____________>>> example:  $ ./drawShape.py arc angle=180"
	print "\n", "\n" 

def drawDefaultShape():
	"""Draw a default shape when no command line arguments are used"""

	for shape in range(defaultShapeIterations):
		polygon(t=bob, n=(defaultShapeSides + shape),
				length=defaultShapeLength+(defaultShapeLength*(shape/defaultShapeIterations)))

def drawDefaultPoly():
	"""Draw the default polygon when only 'poly' is detected in commmand line"""
	
	polygon(t=bob, n=defaultPolygonSides, length=defaultPolygonLength)

def drawDefaultArc():
	"""Draw the default Arc when only 'arc' is detected in commmand line"""
	
	arc(t=bob, r=defaultArcRadius, angle=defaultArcAngle)
	print "drawing arc"
	print "default Arc Radius = ", defaultArcRadius
	print "default Arc Angle = ", defaultArcAngle



def checkArgv():
	"""Process command line arguments.  Act accordingly."""

	# If no cmd line args, draw default shape
	if len(sys.argv) < 2:
		drawDefaultShape()

	# Draw the default polygon or arc as specified, otherwise draw default shape
	elif "poly" in sys.argv and len(sys.argv) == 2:
		drawDefaultPoly()
	elif "arc" in sys.argv and len(sys.argv) == 2:
		drawDefaultArc()
		print "if statement verfication"
	else:
		drawDefaultShape()

	commandLineInstructions()

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

