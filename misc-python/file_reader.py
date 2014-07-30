#!/usr/bin/env python -tt

"""jstephens - pyfu - 2024 july

Generic file reader intended for list of numbers.
For main: read_file()
As module: get_fileRef(filename)
"""

import sys

def read_file():
	"""Creates a file object and reads through the content of a file
	"""
	defaultFile = 'numbers.txt'

	if len(sys.argv) == 2: 
		filename = sys.argv[1]
		try:
			fileRef = open(filename)
		except IOError, e:
			print "\nunkown file: ", filename, "\n --> Switching to default file: ", defaultFile
			print str(e)
			filename = defaultFile
			ans = raw_input("y/n?")
			if str(ans) != 'y':
				print "\nexiting"
				sys.exit(0)


	#else:
	#	filename = ('numbers.txt')

	
	fileRef = open(filename)

	allLines = fileRef.readlines()	

	for line in allLines:
		print line.rstrip('\n')

	fileRef.close()


def get_fileRef(filename):
	"""Use as module for reading and returning a list of numbers from a file
	"""
	filename = str(filename)
	if filename != 'numbers.txt':
		print "use: numbers.txt"
		sys.exit(1)
	fileRef = open(filename)
	
	return fileRef

	"""
	allLines = fileRef.readlines()

	for line in allLines:
		line = line.rstrip('\n')
		
	"""

if __name__ == '__main__':
	read_file()


#export_refFile()





