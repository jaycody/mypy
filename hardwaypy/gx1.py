#!/usr/bin/env python -tt

# gx1:  Hello argv World			 (file by mk.py)

"""
- Use the 'standard boilerplate that calls the main.
- use argv with dot syntax but as a list accessed by index with format sys.argv[1]
	sys.argv[0] --> refers to the argv script itself 
	sys.argv[1] --> refers to the first argument passed in from the command line
- use help(importedModuleFoo)
- use dir(importedModuleFoo)

"""

import sys

# Define a main() function
def main():
	"""documentation comment here"""
	
	#get the name from the command line using sys.argv
	if len(sys.argv) == 1:
		print"\n---------No argv added from command line when running this script"	
	elif len(sys.argv) == 2:
		argv1 = sys.argv[1]
		print "\n--------%r was entered as the single command line argument for this script" % argv1
	else:
		print "\n--------More than one argv was entered at the command line.--------"
	
	##repeat the if structure using google design patterns
	if len(sys.argv) >= 2:   # asks if at least one argv was added at command line
		argv1 = sys.argv[1]
		print "\n\t%r = argv1 entered on command line" % argv1, "\n"
		print "\tHello " + argv1 + "\n"
	else:
		name = 'World'
		print"Hello", name
		
	print sys.path





# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()