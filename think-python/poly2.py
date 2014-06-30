#! /usr/bin/env python

"""j.stephens  ==> mypy gongfu
Think Python - Allen Downey
Chpt 4: Case Study - Interface Design"""

from swampy.TurtleWorld import *

import math

world = TurtleWorld()
bob = Turtle()



### DEFINE Functions##########

def drawSquare(t, length):
	'''Draw square with edge length.
	Turtle instance, edge length ===> square 
	'''
	for i in range(4):
		fd(bob, 20)
		rt(bob)

##############################


### CALL Functions
drawSquare(bob, 50)


wait_for_user()