#!/usr/bin/env python 	-tt

# ex35:  Branches and Functions			 (file by mk.py)

"""
exit(0)  --> shuts down w/o error
exit(1)  --> shuts down with error

search a string with an if statement:
	if "stringFoo" in stringVariable

compound search inside a string with if statement:
 	if "stringFoo" in stringVariable or "stringBar" in stringVariable:


"""

from sys import exit

# Define a main() function
def main():
	"""documentation comments here"""
	gold_room()
	
	
def gold_room():
	print "more of the same.  choose"
	next = raw_input('> 0 or 1  ')
	
	if "0" in next or "1" in next:
		print " one or the other were found in the string"
		
	else:
		print "nope, couldn't find it"
		dead("You failed to find what you were looking for")

def dead(why):
	print why, "And that's that"
	exit(0)

def start():
	print "You're at Au Coquelet, coding"
	print "You see a tutorial."
	print "What do you do?"
	
	doNext = raw_input('>   ')
	
	if doNext == 'Focus':
		gold_room()
	elif doNext == 'Do it':
		print "you must focus"
		start()
	else:
		dead("Because it's the Fruit Stand guys, and now is the time")

start()
		




# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()