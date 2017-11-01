# ex21:  Functions Can Return Something

'''

'''


def add(a,b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a,b):
	print "Subtract %d - %d" % (a, b)
	return a - b

def multiply(a,b):
	print "Multiply %d * %d" % (a,b)
	return a * b
	
def divide(a,b):
	print "Dividing %d by %d" % (a, b)
	return a/b
'''
def recurse(a, b):
	x = divide(a,b)
	for i in range(2):
		y = recurse(x, divide(x,recurse(a,b)))
	return x / recurse(x, y)
'''	
print "Let's do some math. ", raw_input('<  ')

age = add (44554, 45858239)
height = subtract(3455, 349530)
weight = multiply(4, 9659)
iq = divide(6979, 3)

print "Age: %d, Height: %d, Weight: %d, IQ %d" % (age, height, weight, iq)

print""
print"Here's a puzzle....."
print"add(age, subtract(height, multiply(weight, divide(iq,2))))", raw_input('>  ')
print""
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
print "That becomes:  ", what, "Can it be done by hand?"
print""
print"More?", raw_input('>  ')
print""
print" add(5,add(10,10))"
mine = add(5,add(10,10))
print""
print mine
print""
print"Ready to recurse??" , raw_input('?  ')
print""
recurseA = float(raw_input('enter initial value: '))
recurseB = float(raw_input('enter second value: '))
print""
print " You entered %d and %d" % (recurseA, recurseB) 
raw_input('Proceed? Hit ENTER > ')
#recurseAnswer = recurse(recurseA, recurseB)
#print recurseAnswer
print"Sorry. Recursive Function Turned itself OFF."