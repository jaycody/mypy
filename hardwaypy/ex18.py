# ex18:  Names, Variables, Code, Functions

'''
FUNCTIONS:
	1. They name pieces of code the way variables name strings and numbers
	2. They take arguments
	3. Use #1 and #2 to create 'mini-scripts' or 'tiny-commands'

Create with 'def'	for DEFINE FUNCTION
START by INDENTING
END a function by DEDENTING

*args --> 'asterisk args' tells Python to take all the arguments to the function
			and then put them in args as a list.
			similar to argv from command line requires exact number of args
'''

# similar to argv from sys in command line.  
# '*argv' (asterisk args) means the number of arguments required varies depending on the functions needs.
		# but using *args requires the arguments are assigned before use
def print_two(*args):
	arg1, arg2 = args
	print "arg1 = %r, arg2 = %r" % (arg1, arg2)
	
	
def print_two_again(arg1, arg2):
	print "arg1 = %r, arg2 = %r" % (arg1, arg2)


# take one argument
def print_one(arg1):
	print "arg1 = %r" % arg1
	
#  takes NO arguments
def print_none():
	print "No argument, no value"
	



print_two("Alpha", "Beta")
print_two_again("AlphaBeta", "BetaBeta")
print_one("AlphaUNO")
print_none()


