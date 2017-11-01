#! /usr/bin/env python


"""j.stephens  ==> mypy gongfu - Think Python - Chpt 4: Draw 2D shapes of n-fold symmetry
	Dependencies:  poly2.py

	command line arguments:

	drawShape.py { number of polygon sides , length of each side , number of iterations}

	TODO:
	[x] Add variable values to the console print (ex nSides = Foo).
		- use the method that looks some like print "nSides = %1, length = %2", (n, length)
"""

# gets argv from command line
import sys
# helps loops through argvs
import fileinput

from swampy.TurtleWorld import *
from poly2 import *


# Defaults in no command line arg
defaultShapeSides = 2
defaultShapeLength = 50.0
defaultShapeIterations = 10
defaultShapeRadius = 10
defaultShapeAngle = 120

# Defaults for Polygon when no arguments are presented in the command
defaultPolygonSides = 4
defaultPolygonLength = 50

# Defaults for Arcs
# !!!! Make sure the arc angle is a float!
defaultArcRadius = 49.75
defaultArcAngle = 500.0

def commandLineInstructions():
	"""Print to console the arguments for shape drawing.  Include specifics
	from command line arguments
	"""

	print "\n"
	print "======> To draw polygons or arcs, use command line input as follows:"
	print ""
	print "-----------> [poly | arc], [ (for polygon, enter num of sides) | (for arc, enter angle in degrees)]"
	print ""
	print "_______________>>> example:  $ ./drawShape.py poly 6"
	print "_______________>>> example:  $ ./drawShape.py arc 180"
	print "\n", "\n" 

def getShapeType(nSides):
	"""Figure out the name of a polygon when given the number of sides.
	Return the polygon type as a string (ex "Square")"""

	# Name that shape
	n = nSides
	if n == 3:
		pType = "Triangle"
	elif n == 4:
		pType = "Square"
	elif n == 5:
		pType = "Pentagon"
	elif n == 6:
		pType = "Hexagon"
	elif n == 7:
		pType = "Heptagon??  (7 sided)"
	elif n == 8:
		pType = "Octagon"
	elif n == 9:
		pType = "Uh, 9 sided shape is called a????"
	else:
		pType = "shape of unknown type"
	return pType

def drawDefaultShape():
	"""Draw a default shape when no command line arguments are used"""
	
	print ""
	print "=======> Without a command line argument, draws default image.....an iterated polygon"
	print ""
	print "=====>  Drawing %d iterations of the default shape" % (defaultShapeIterations)
	for shape in range(defaultShapeIterations):
		# Create a float version of changing iteration * length thing
		changingLength = defaultShapeLength+(defaultShapeLength*(float(shape)/float(defaultShapeIterations)))
		
		polygon(t=bob, n=(defaultShapeSides + shape),
				length=changingLength)

		print "Iteration # %d, Number of Sides = %d [%s], Length of Each Side = %d" % (shape, (defaultShapeSides + shape), getShapeType((defaultShapeSides + shape)), changingLength)
		
def drawDefaultPoly():
	"""Draw the default polygon when only 'poly' is detected in commmand line"""
	
	# get the name of that shape
	pType = getShapeType(defaultPolygonSides)
	
	print ""
	print "Drawing the default polygon:  a %s" % (pType)
	print "_________> Number of Sides = %d,  Length of Each Side = %d" % (defaultPolygonSides, defaultPolygonLength)
	print ""
	polygon(t=bob, n=defaultPolygonSides, length=defaultPolygonLength)

def drawDefaultArc():
	"""Draw the default Arc when only 'arc' is detected in commmand line"""
	
	arc(t=bob, r=defaultArcRadius, angle=defaultArcAngle)
	print "drawing arc"
	print "default Arc Radius = ", defaultArcRadius
	print "default Arc Angle = ", defaultArcAngle

def drawPolygon(nSides, sideLength):
	"""Draw a polygon with specified number of sides, each side a specified length
	>>> from drawShape import drawPolygon
	>>> drawPolygon(5, 9)
	<BLANKLINE>
	----->Drawing a polygon of 5 sides 
	 Type: Pentagon 
	 Side length = 9
	<BLANKLINE>
	"""
	print ""
	print "----->Drawing a polygon of %d sides \n Type: %s \n Side length = %d" % (nSides, getShapeType(nSides), sideLength)
	print ""
	polygon(t=bob, length=sideLength, n=nSides)

def drawArc(radiusOfCircleForThisArc, arcAngle):
	print ""
	print "---->Drawing:  Arc \n angle = %f \n from a circle with radius = %f" % (arcAngle, radiusOfCircleForThisArc)
	print ""
	arc(t=bob, r=radiusOfCircleForThisArc, angle=arcAngle)

def drawFlower():
	""".drawShape.py flower[1] {angle in degrees[2]} {radius of circle[3]} {pedals[4]}
	"""

	arcAngle = float(sys.argv[2])
	radiusOfCircleForThisArc = float(sys.argv[3])
	pedals = int(sys.argv[4])
	
	# calculate total angle of 185 degrees to return to starting point
	# Now Draw as many of these arc as needed


	# Iterate pedals
	for pedal in range(pedals):
		# Draw Left Edge of Pedal, then turn back and draw other edge
		for iteration in range(2):
			drawArc(radiusOfCircleForThisArc, arcAngle)
			rotateTurtle(t=bob, rotateDirection="rt", rotateAngle=180.0-arcAngle)
		# Now rotate to the next dedal
		rotateTurtle(t=bob, rotateDirection="lt", rotateAngle=(360.0/(pedals+1)))


def checkArgv():
	"""Process command line arguments.  Act accordingly."""

	# If no cmd line args, draw default shape
	if len(sys.argv) < 2:
		drawDefaultShape()

		# Print the instructions when inadequate instructions are added to the command line
		commandLineInstructions()

	# If arc or poly AND no other argument to specify sides or angle
	# Otherwise draw the default shape and print the instructions to console
	elif len(sys.argv) == 2:
		if "poly" in sys.argv:
			drawDefaultPoly()
		elif "arc" in sys.argv:
			drawDefaultArc()
		else:
			drawDefaultShape()
			commandLineInstructions()
	# If arc or poly have only one argument (ie angle or nSides)
	elif len(sys.argv) == 3:
		if "poly" in sys.argv:
			############
			## FIGURE OUT HOW TO CONTEND WITH INVALID LITERALS FOR int() base 10
			##    - added from the command line (ex ./drawShape.py poly what?)
			nSides = int(sys.argv[2])
			print nSides
			sideLength = defaultPolygonLength
			drawPolygon(nSides, sideLength)
		elif "arc" in sys.argv:
			arcAngle = float(sys.argv[2])
			print arcAngle
			print "from checkArgv function, defaultArcRadius = %f" % (defaultArcRadius)
			radiusOfCircleForThisArc = float(defaultArcRadius)
			drawArc(radiusOfCircleForThisArc, arcAngle)
		else:
			drawDefaultShape()
			commandLineInstructions()

	elif len(sys.argv) == 4:
		if "poly" in sys.argv:
			############
			## FIGURE OUT HOW TO CONTEND WITH INVALID LITERALS FOR int() base 10
			##    - added from the command line (ex ./drawShape.py poly what?)
			nSides = int(sys.argv[2])
			print nSides
			sideLength = float(sys.argv[3])
			drawPolygon(nSides, sideLength)
		elif "arc" in sys.argv:
			arcAngle = float(sys.argv[2])
			print arcAngle
			print "from checkArgv function, defaultArcRadius = %f" % (defaultArcRadius)
			radiusOfCircleForThisArc = float(sys.argv[3])
			drawArc(radiusOfCircleForThisArc, arcAngle)
		else:
			drawDefaultShape()
			commandLineInstructions()

	# {Poly | Arc}, {Sides | Angle}, {Length | Radius}  and now {ITERATTIONS}
	elif len(sys.argv) == 5:
		if "poly" in sys.argv:
			############
			## FIGURE OUT HOW TO CONTEND WITH INVALID LITERALS FOR int() base 10
			##    - added from the command line (ex ./drawShape.py poly what?)
			nSides = int(sys.argv[2])
			print nSides
			sideLength = float(sys.argv[3])
			# now draw iterations of the polygon
			for iteration in range(int(sys.argv[4])):
				drawPolygon(iteration+1, sideLength)
				#drawPolygon(nSides, sideLength)
		elif "arc" in sys.argv:
			arcAngle = float(sys.argv[2])
			print arcAngle
			print "from checkArgv function, defaultArcRadius = %f" % (defaultArcRadius)
			radiusOfCircleForThisArc = float(sys.argv[3])

			# calculate total angle of 185 degrees to return to starting point
			# Now Draw as many of these arc as needed
			for iteration in range(int(sys.argv[4])):
				drawArc(radiusOfCircleForThisArc, arcAngle)
		
		# now draw the flowers
		elif "flower" in sys.argv:
			drawFlower()
			
		else:
			drawDefaultShape()
			commandLineInstructions()

	# If something sneaks by, the draw the default and print instructions
	else:
		print "printed from else: line 162 in checkArgv()"
		drawDefaultShape()
		commandLineInstructions()



# getDimensions Algorithm
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

