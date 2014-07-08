#! /usr/bin/env python

"""j.stephens  2014 june ==> mypy gongfu - Think Py - Chpt 4: Interface Design

topics:  
	encapsulation:  wrapping a piece of code in a function
	generalization:  adding a parameter to a function
	keyword arguments:  for clarity, include name of parameters in argument list when calling function
		ex  polygon(bob ,length=50 ,n=5)
	interface:  summary of how the function is used.  what are the parameters?
FLOW:
	polygon() calls polyline()
	circle() calls polygon() calls polyline()
	arc() calls polyline()
"""

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
jay = Turtle()

bob.delay = 0.01
jay.delay = 0.01

world.ca_width = 700
world.ca_height = 700
world.canvas = world.ca(world.ca_width, world.ca_height, bg='white')


def drawSquare(d, t, length):
	'''Draw square with edge length 'length'.
		Turtle instance, edge length ===> square 

		d: turn direction (either 'rt' or 'lt')
		t: Turtle object
		length:  edge length
	'''

	for i in range(4):
		fd(t, length)
		d(t)

def polygon(t, length, n):
	'''Draw n-sided regular polygon with edge length 'length'. (vertices of n-sided polygon = 360/n)
	IN:  Turtle instance, edge length, num of sides.  OUT: n-sided polygon 
	'''
	
	iteratorN = int(n)
	vertexTheta = 360.0/n

	## OUTSOURCE THE DRAW
	polyline(t ,n=iteratorN ,length=length ,angle=vertexTheta)

def circle(t, r):
	"""Draw a circle with radius r using polygon() to approximate a circle
	IN:  Turtle t, radius r.   OUT: circle
	"""

	# A circle is just an arc whose angle is 360
	arc(t ,r=r, angle=360)

	""" REFACTOR THIS ENTIRE PIECE so that circle() calls arc()
		### Calculate Circumference of polygon and the length of each side when given r
		# c = 2 * PI * r
		circumference = 2 * math.pi * r 

		''' THIS IS VERY INEFFICIENT method for calculating n-sides and length
		# Let length of each side = 10% of the radius 
		length = .1 * r

		### Now solve for number of sides ('n') using polygon circumference and length of each side 
		# where (length * n) = circumference,
		n = circumference / length 
		'''

		# THIS IS MORE EFFICIENT method of calculating the numbers of sides and length of each
		n = (circumference / 3 )+ 1
		length = circumference/n

		# now call the polygon to draw the circle
		polygon(t, length, n)
	"""

def arc(t, r, angle):
	"""Draw a section of a circle whose degree of arc = 'angle'.
		A **generalized** version of circle() with added argument for angle to determine length of arc

		1. What percentage of the circle must be drawn to make an arc with given angle?
			percentage of circle to draw = given angle to draw / total degrees of a circle 
		2. How many sides of a total circle must be drawn to draw that percentage of a circle from #1?
			- number of sides to draw for given arc = total sides required * fraction of circle to draw
			- To draw 50 percent of a circle, you'd need 50 percent of the sides required for full circle
				THUS, when angle to draw = 360, the percentage of circle to draw is 100 
					--> requiring 100 percent of the sides
				and when angle to draw is 90, the percentage to draw is 90/360 * 100 (25 percent)
					--> requiring 25 percent of the sides.	
		Such that:  fraction of circle to draw = desired angle / 360 degrees
	"""

	circumference = 2.0 * math.pi * r 		# calculate the circumference of circle
	length = .1 * r 					# set length to 10% of the radius

	# Number of sides for complete polygon of 360 degrees
	n = circumference / length 

	# Calculate the angle the turtle must turn between every edge at the vertex
	rotateAtEachVertexBy = 360.0/n

	##	Calculate the number of sides to actually draw and use the int of that number as for loop range 
	if angle == 360.0:					# when drawing a circle, all the nSides are required
		nSides = int(n)  				# assuming angle to draw is 360
	
	## then use given angle of arc to determine number of sides that are required
	else:
		nSides = int(n * (angle/360.0))		
	print "==>Where the arc is an approximation of a curve created from a polygon with"
	print " Num of Sides = %d \n Side Length = %f \n Vertex Angle = %f" % (nSides, length, rotateAtEachVertexBy)
	print ""

	### Now call polyline() to draw the ARC!
	polyline(t ,n=nSides ,length=length ,angle=rotateAtEachVertexBy)

def polyline(t, n, length, angle):
	"""Refactors forloop common to arc() and polygon() who now share and call this function. 
	Draws the full or partial polygon and/or arc
	"""
	for side in range(n):
		fd(t, length)
		rt(t, angle)

def rotateTurtle(t, rotateDirection, rotateAngle):
	"""Rotate the drawing point either left or right by a specified amount
	
	t: turtle instance
	rotateDirection:  {'rt' | 'lt'}  #either right turn or left turn
	rotateAngle: amount of rotation specified in degress (not radians)
	"""

	if rotateDirection == "rt":
		print "Right Turn by %f degrees" % (rotateAngle)
		rt(t, rotateAngle)
	elif rotateDirection == "lt":
		print "Left Turn by %f degrees" % (rotateAngle)
		lt(t, rotateAngle)
	else:
		print "input was neither 'rt' nor 'lt' -- so turning right"
		rt(t, rotateAngle)
		
if __name__ == '__main__':
	"""True if poly2.py is called directly from command line.
	False if poly2.py is used only as a module in another scropt
	"""

	numSided = 5
	lengthSide = 50
	angle = 180
	radius = 100

	numShapes = 5

	arc(t=bob, r=radius, angle=angle)

	"""
	for shape in range(numShapes):
		#draw polygon
		polygon(t=bob ,length=shape*4 ,n=(shape+2))
		#move cursor over
		pu(bob)
		fd(bob, shape*4)
		lt(bob)
		pd(bob)
		#draw another polygon
		polygon(t=bob ,length=50 ,n=8)
		arc(t=bob, r=radius, angle=angle)
	"""

	wait_for_user()





###########################################################
