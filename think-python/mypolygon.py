#! /usr/bin/env python

from swampy.TurtleWorld import *

import math

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.001
world.ca_width = 700
world.ca_height = 700
world.canvas = world.ca(world.ca_width, world.ca_height, bg='white')

# function to draw a square
def square(t, length, turn, degree):
	for i in range(4):
		turn(t, degree)
		fd(t, length)
		

def polygon(t, length, turn, n):
	angle = 360/n
	polyline(t, n, length, angle, turn)

	'''
	for i in range(n):
		fd(t, length)
		turn(t, angle)
	'''	

def circle(t, r):
	'''
	Draws a circle of radius r.  1st calculates circumference 2PI*r.  then divides the circumference
	by the number of step_length required to approximate a circle
	'''
	circum = 2*math.pi*r
	numSides = r * 1.0
	length = circum/numSides

	polygon(t, length, lt, r)



def arc(t, r, angle, turn):
	circum = 2 * math.pi * r
	arcLength = circum*angle/360
	n = int(arcLength/r) + 1
	step_length = arcLength/n
	step_angle = float(angle)/n

	polyline(t, n, step_length, step_angle, turn)
	

def polyline(t, n, length, angle, turn):
	for i in range(n):
		fd(t, length)
		turn(t, angle)
	
'''
singleStart = 150 
for i in range(singleStart):
	if i % 2 == 0:
		either = rt
	elif i%3 ==0:
		either = lt
	elif i%7 ==0:
		either = rt
	else: 
		either = lt

	#polygon(bob, length = (singleStart-i*.9), n = (2+int((i+1)*.1)), turn=either)
	
	arc(bob, r = 1+int(i*.9), angle = (i+1)*2, turn=either)
'''

def keeper():
	"""Nested Polygon with sweet spot for variables
	"""
	singleStart = 100
	previousEither = lt
	for i in range(singleStart):
		if i % 2 == 0:
			either = lt
		elif i%3 ==0:
			either = lt
		elif i%7 ==0:
			either = lt
		elif i%11 ==0:
			either = rt
		else: 
			either = lt

		polygon(bob, length = (singleStart-i*.7), n = (1+int((i+1)*.01)), turn=either)

		polygon(bob, length = (2+i*5), n = (2+int((i+1)*.1)), turn=previousEither)

		

		arc(bob ,r=4*i+1 ,angle = 137 ,turn = either) 
		arc(bob ,r=3*i+1 ,angle = 45 ,turn = previousEither) 

		previousEither = either
		#circle(bob ,r = singleStart-i+1)
	###########################################


################
## Function Calls
################
keeper()	

wait_for_user()
