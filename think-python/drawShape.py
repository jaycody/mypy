#! /usr/bin/env python


"""j.stephens  ==> mypy gongfu - Think Python - Chpt 4: Draw 2D shapes of n-fold symmetry
Dependencies:  poly2.py


"""

from swampy.TurtleWorld import *
from poly2 import *


world = TurtleWorld()
bob = Turtle()
jay = Turtle()

bob.delay = 0.0001
jay.delay = 0.0001

length = 50
n = 5
radius=10
angle=39




##############################
#### Iterated Draw 
##############################


#circle(t=bob ,r=400)				# using KEYWORD ARUGMENTS

numShapes = 25
for shape in range(numShapes):
	drawSquare(lt, bob, shape*5)
	#polygon(t=bob ,length=(numShapes-shape)*3 ,n=numShapes-shape+3)
	#arc(bob, radius*(shape*.5)+1, angle*shape+1)
	drawSquare(rt, bob, shape*20)


#drawSquare(rt, bob, 40)


wait_for_user()