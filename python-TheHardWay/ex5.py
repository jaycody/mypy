# ex5:  More Variables and Printing

''' 
format string:  
	specialized format string for adding variables into the string
	by placing special characters at the end of the string.

format characters (aka formatters)
	the characters used as stand-ins for variables inside a string
	where '%' modulo is the 'formatting operator' or 'interpolation operator' and marks the start of the specifier
	ex. of Conversion Types:
		%s  string by converting any pyton object using str()
		%d  integer decimal
		%r  string by converting any pyton object using repr() (including the results of expressions)
				- use the %r for debugging since it displays the 'raw' data of the variable
		%f  floating point
	
'''

name = 'Jason C. Stephens'
age = 42 # seriously
height = 72 #inches
heightInCentimeters = height * 2.54
weight = 180 #pounds
weightInKilos = weight * .453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
rFormatterExample = 5-999

print "Let's talk about %s." % name
print ''
print "He's %d inches tall." % height
print 'According to the metric system, he\'s %r centimeters tall.' % heightInCentimeters
print "He's %d pounds heavy." % weight
print "Actually, he's %d pounds 'lite.'" % weight
print ''
print 'In kilos, he weighs %r.' % weightInKilos
print ''
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the the coffee." % teeth

#this is tricky, try to get it EXACTLY
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)

#use the 'r' formatter
print "If this works, it will read: %r" % rFormatterExample