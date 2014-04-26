#!/usr/bin/env python 	-tt

# openAndReadFiles.py			 (file by mk.py)

"""
- write a script that opens a file and reads it line by line
- the file entered should come frm the command line argv

"""

import sys





# Define a main() function
def main():
	"""documentation comments here"""
	f = open(sys.argv[1], 'r')   				# --> open the file foo designated in command line

	oneListForFile = []									#  --> create the accumulatr list

	for line in f:											#  --> iterate through each line in the file f
		print "Line in f", line
		strippedLine= line.strip()				# --> remove the white space from each line at the beginning and save as new string
		print "line in f, stripped", strippedLine								# --> print each new line
		print type(strippedLine)
		listOfStrippedLine = strippedLine.split(" ")
		for element in listOfStrippedLine:
			oneListForFile.append(element)
		print listOfStrippedLine
		print type(listOfStrippedLine)
		
	print oneListForFile
	oneStringForFile = " ".join(oneListForFile)
	print oneStringForFile
	f.close()




# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()