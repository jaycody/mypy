from swampy.TurtleWorld import *

import math

world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

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
	circum = 2*math.pi*r
	numSides = r * 1.0
	length = circum/numSides
	polygon(t, length, lt, r)
	'''
	arc(t, r, 360, rt)



def arc(t, r, angle, turn):
	"""Draws portion of a circle determined by angle of size radius of that circle
	"""
	circum = 2 * math.pi * r
	arcLength = circum*angle/360
	n = int(arcLength/r) + 1
	step_length = arcLength/n
	step_angle = float(angle)/n
	polyline(t, n, step_length, step_angle, turn)	


def polyline(t, n, length, angle, turn):
	"""Draws n line segments with the given length and angle
	in degrees between them.  t is the turtle
	"""
	for i in range(n):
		fd(t, length)
		turn(t, angle)
	
def flower():
	polygon(bob, 25, rt, 5)


flower()



	#arcLength = int(arcLength)
	#polygon(t, step_length, turn, n)

#square(bob, 100, lt, 45)
#square(bob, 100, rt, 100)

#square(bob, 100, lt, 90)

# include keyword arguments  !! CAN BE ANY ORDER
#arc(bob, 50, 190, lt)
#circle(bob, 100)



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

	polygon(bob, length = (singleStart-i*.9), n = (2+int((i+1)*.1)), turn=either)
'''

'''
polygon(bob,  n=11, length=50, turn=rt)
polygon(bob, 50, lt, 5)
polygon(bob, 50, rt, 9)
polygon(bob, 50, lt, 4)
polygon(bob, 50, rt, 6)
polygon(bob, 50, lt, 3)
'''

'''
circle(bob, 20)
circle(bob, 50)
circle(bob, 100)
circle(bob, 75)
circle(bob, 30)
circle(bob, 10)
'''


wait_for_user()
