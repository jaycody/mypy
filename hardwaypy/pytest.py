#!/usr/bin/env python 	-tt

# pytest.py			 (file by mk.py)

"""
Fruit stand 20131111

covers: 
dictionaries

"""

import sys

# Define a main() function
def main():
	
	if len(sys.argv) >=2:
		filename = sys.argv[1]
	else:
		filename = "twoColumnWebLog.txt"
	
	#create / oepn a new file and fill with key value pairs
	refFile = open(filename, 'w')
	for n in range (50):
		refFile.writelines("%d" % (n*10))
		#refFile.writelines("\t\tValueForKey%d-->%04d \n"% (n, n * (50-n)))
		refFile.writelines("\t\t %04d \n" % ( n * (50-n)))
		
	for n in range (50):
		refFile.writelines("%d" % (n*10))
		#refFile.writelines("\t\tValueForKey%d-->%04d \n"% (n, n * (50-n)))
		refFile.writelines("\t\t %04d \n" % ( n * n))
		
		
		#print refFile
	refFile.close()	
	
	
	entries = {}
	for line in open(filename, 'r').readlines():
		#print line,
		splitLeft, splitRight = line.split()
		#print splitLeft, type(splitLeft),
		#print "\t", splitRight, type(splitRight)
		
		try:
			entries[splitLeft].append(splitRight)
		except KeyError:
			entries[splitLeft] = [splitRight]
			#print "now splitRight type = ", type(splitRight)
	for (splitLeft, splitRights) in entries.items():
			print "Key: %r  has %04d items.\tValues => %r" % (splitLeft, len(splitRights), splitRights)
	


# This is the standard boilerplate that calls the main() function.
#This indefinite loop will not run when the script is called as a module by another script.
if __name__ == '__main__':
	main()
	
	
	
	
'''
entries = {}
for line in open(sys.argv[1], 'r').readlines():
    left, right = string.split(line)    
    try:                                
        entries[right].append(left)
    except KeyError:
        entries[right] = [left]
 
for (right, lefts) in entries.items():
  print "%04d '%s'\titems => %s" % (len(lefts), right, lefts)
  
'''