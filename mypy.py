#!/usr/bin/env python

""" jstephens  - 2014.07 - mypy gongfu

This script opens and reads text files
"""
# Get access to argv
import sys

# Get access to operating system interface and file system
import os



def openAndPrintTextFile(textFile):
	"""Opens a text file, reads and prints each line
	"""

	f = open(textFile, "r")
	for line in f:
		print line,

def findTotalNumberOfSpecifiedString(textFile, stringToFind):
	"""Opens a text file, searches for all instances of specified string.
	Counts total number of specified string.  Returns total number of specified string
	"""

	totalNumberOfSpecifiedString = 0

	fileObjectToSearch = open(textFile, "r")
	for eachLine in fileObjectToSearch:
		if stringToFind in eachLine:
			totalNumberOfSpecifiedString += 1
			print "Found %d instances of '%s' in %s" % (totalNumberOfSpecifiedString, stringToFind, textFile)
	print ""
	print "Total instances of '%s' in %s = %d" % (stringToFind, textFile, totalNumberOfSpecifiedString)


def getCommandLineInstructions():
	"""Analyze user input from command line.
	If only textfile present, then print the text file.
	If textfile and string present, then call the function to count the number
	of instances this string appears
	"""

	# Command line contains name of textfile to analyze  but no search term string
	if len(sys.argv) == 2:
		openAndPrintTextFile(sys.argv[1])
	# command line contains two arguments 
	elif len(sys.argv) == 3:
		openAndPrintTextFile(sys.argv[1])
		# and count the instances of specified string
		findTotalNumberOfSpecifiedString(sys.argv[1], sys.argv[2])
	else:
		print "\n-------Command Line Instructions for mypy.py----------"
		print ""
		print "==============={ ./mypy.py { "textFileFoo", "stringToFind" } "
		print ""

if __name__ == "__main__":
	"""If running as a main program, then do the following.
	Otherwise, if running as a module, do not call the following functions
	"""

	getCommandLineInstructions()

	openAndPrintTextFile(sys.argv[1])
	




