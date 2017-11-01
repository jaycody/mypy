#!/usr/bin/env python

'''
Exercise 3-4:  Function Objects
can be assigned to variables
or passed as an argument.
1. write and test the example script
2. modify do_twice so that it:
	- takes two arguments, a function object and a value
	- passing the value as an argument.
'''

'''
#1
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)
'''

#2
def do_twice(f, strArg, valArgument):
	f(strArg, valArgument)

def print_spam(strArg, valArgument):
	print (strArg)*valArgument

do_twice(print_spam, 'What is this ' ,10)





