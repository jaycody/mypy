# open file and read contents to the console

# use: f = open(filename, 'rU')
# use: for line in f:  print line,
# use: s = f.read() 				--> return entire file to single string 
# use: l = f.readlines()			--> return list with each element a list of each line
# use: f.close
# use: .split


import sys

def practice():
	f = open('today.txt', 'rU')

	'''
	# iterate:
	for line in f:
		print line
	'''

	# read()
	s = f.read()
	#print s
	
	# readlines()
	#l = f.readlines()
	#print l
	
	#.split()
	#lOfS = s.split()  # called with no arguments, splits on white space
	#print lOfS

	
def WordCount():
	wordCountDict = {}
	f = open('today.txt', 'rU')
	#for line in f: print line
	
	s = f.read()
	#print s
	
	lOfS = s.split()
	#print lOfS
	
	for word in lOfS:  
		if not word in wordCountDict: #if this is the first time
			wordCountDict[word] = 1
			#print word
		else:
			wordCountDict[word] = wordCountDict[word] + 1
	
	
	return wordCountDict
	f.close()
		


	




def main():
	#practice()
	
	wordCount = WordCount()
	dItems = wordCount.items()
	dValues = wordCount.values()
	dKeys = wordCount.keys()
	
	dItemsSorted = sorted(dItems, reverse = True)
	for items in dItemsSorted:
		print items
	
	
	
main()
