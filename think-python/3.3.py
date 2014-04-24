#!/usr/bin/env python


'''
Write a function name 'right_justify' 
that takes a string named 's' as a parameter 
and prints the string with enough leading spaces 
so that the last letter of the string is in column 70 of the display.
'''


def right_justify(s):
	lengthStringS = len(s)
	emptySpaces = ' '*(70-lengthStringS)
	totalPrinted = emptySpaces + s

	print emptySpaces + s

	print "Last letter of " + s + " falls on column #" + str(len(totalPrinted))


right_justify('hello world')



