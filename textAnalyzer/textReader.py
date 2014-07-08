#!/usr/bin/env python

""" jstephens  - 2014.07 - mypy gongfu

This script opens and reads text files

TODO:
[ ] create the following functions:

word_count_dict(filename)
print_words(filename)
get_count(word_count_tuple)
print_top(filename)

[ ] update the getCommandLineInstructions
      - to sys.exit(1) when unknown inputs are detected
      - decision tree utilizing flags '--count' or '--string' etc

[ ] create a textAnalyzer class
"""

getattrTest = 109.1
#############################
## HOMEWORK SECTION
##########################################################################
              														#
# Get access to argv												#
import sys  														#
                      												#
# Get access to operating system interface and file system			#
import os    													    #
   																  #####
    															   ### 
    															    #  
def word_count_dict(filename):
	"""Returns a word/count dict for this filename"""

	#Magik Here


def print_words(filename):
	"""Prints one per line '<word> <count>' sorted by word for the given filename"""

	#Magik Here


def get_count(word_count_tuple):
	"""Returns the count from a dict word/count tuple  -  used for custom sort."""

	#Magik Here

																   #																
def print_top(filename):										  ###
	"""Prints the top count listing for the given file"""        #####
																   #
	#Magik Here													   #
#														           #
#       												           #
####################################################################


def openAndPrintTextFile(textFile):
	"""Opens a text file, reads and prints each line
	"""

	f = open(textFile, "r")
	for line in f:
		print line,

	f.close()

def findTotalNumberOfSpecifiedString(textFile, stringToFind):
	"""Opens a text file, searches for all instances of specified string.
	Counts total number of specified string.  Returns total number of specified string
	"""

	totalNumberOfSpecifiedString = 0

	fileObjectToSearch = open(textFile, "r")
	for eachLine in fileObjectToSearch:
		if stringToFind in eachLine:
			totalNumberOfSpecifiedString += 1
			print "==> Finding %d instances of the string '%s' in %s" % (totalNumberOfSpecifiedString, stringToFind, textFile)
			print eachLine
	print ""
	print "=============================================================="
	print "Total instances of '%s' in %s = %d" % (stringToFind, textFile, totalNumberOfSpecifiedString)
	print ""

	fileObjectToSearch.close()

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
		#openAndPrintTextFile(sys.argv[1])
		# and count the instances of specified string
		findTotalNumberOfSpecifiedString(sys.argv[1], sys.argv[2])
	else:
		print ""
		print "============>>> usage: ./mypy.py { 'textFileFoo', 'stringToFind' } "
		print ""

if __name__ == "__main__":
	"""If running as a main program, then do the following.
	Otherwise, if running as a module, do not call the following functions
	"""

	getCommandLineInstructions()

	#openAndPrintTextFile(sys.argv[1])
	




