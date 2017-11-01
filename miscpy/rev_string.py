#!/usr/bin/env python 

"""jstephens - py-fu  2014 july 23
==> script that reverses string without cheating with s[::-1]
Solving now a question I missed in the interview with RadiumOne
"""

import sys

def rev_string(s):
	"""Reverse the string without cheating
	"""
	#print "string passed from command line  = %s" % s
	lenStr = len(s)
	revStr = ''

	for index in range(lenStr):
		curLastLetter = s[lenStr-index-1]
		revStr = revStr + curLastLetter
	print revStr

def main():
	"""Prcoess the command line arguments
	and call required functions
	"""
	if len(sys.argv) != 2:
		print "usage: ./rev_string.py <string to reverse>"
	else:
		rev_string(sys.argv[1])



if __name__ == '__main__':
	
	main() 
