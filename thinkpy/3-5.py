#!/usr/bin/env python

'''
exer 3-5  More functions

1. write a funciton that draws an ascii graphic

'''

# gets argv from command line
import sys

# helps loops through argvs
import fileinput

def drawASCII(vertex, horzEdge, verticleEdge, numHorzEdges, numVerticleEdges, widthHorizontals, widthVerticles):
	for i in range (numHorzEdges):
		printHorizontalSide(vertex, horzEdge, widthHorizontals)
	
	for i in range (numVerticleEdges):
		printVerticalEdge(verticleEdge, widthVerticles)

	for i in range (numHorzEdges):
		printHorizontalSide(vertex, horzEdge, widthHorizontals)

	for i in range (numVerticleEdges):
		printVerticalEdge(verticleEdge, widthVerticles)

	for i in range (numHorzEdges):
		printHorizontalSide(vertex, horzEdge, widthHorizontals)

def printHorizontalSide(vertex, horzEdge, widthHorizontals):
	print (vertex),
	print (horzEdge)*widthHorizontals,
	print (vertex),
	print (horzEdge)*widthHorizontals,
	print (vertex)


def printVerticalEdge(verticleEdge, widthVerticles):
	print (verticleEdge),
	print (" ")*widthVerticles,
	print (verticleEdge),
	print (" ")*widthVerticles,
	print (verticleEdge)

def getDimension(argvIndex):
	'''takes commnad line arg for number of sides of polygon.
	When no input present, uses default num of sides
	'''

	if argvIndex+1 > len(sys.argv):
		return 25
		
	else:
		dimension = int(sys.argv[argvIndex])
		#print dimension
		return dimension




#drawASCII('x' ,'-' ,'|', 50, 9, 49, 14)

d = getDimension(1)
print d
print "variable type = ", type(d)

drawASCII('x' ,'-' ,'|', getDimension(1), getDimension(2), getDimension(3), getDimension(4))





# vertex, horizontal edge, verticle edge, num of horizontal lines, num of verticle lines, widthHorizontals, widthVerticles)
#tupleInput = ('x' ,'-' ,'|', 50, 9, 49, 14)


#for tupleIndex in tupleInput:




'''
for i in range(len(sys.argv)):
	print sys.argv[i]


lengthArgsArray = len(sys.argv)
'''




