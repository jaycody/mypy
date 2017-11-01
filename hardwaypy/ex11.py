# ex11:  Asking Questions

'''
standard software flow pattern:
	- take input, change it, show it

raw_input() # returns input as a STRING.  strips the newline	
int(raw_input()) # converts string to int before returning
'''

print "How old are you?",
age = int(raw_input())
#ageVarType = type(age)

print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input('pounds here ')

print "So, you're %s years old, %r tall, and you weigh %r? (y/n)___" % (age, height, weight),
answer = raw_input()
if answer == 'y':
	print "then we did something right."
if answer == 'n':
	print """
	NO??? wtf?
	
	Daisy, Daisy, give me your answer true.
	I'm so crrrraaaazzzyy
	thinking thoughts of youuuuuuuu.
	"""