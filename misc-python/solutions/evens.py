
fileRef = open('numbers.txt')
allLines = fileRef.readlines()
for line in allLines:
	n = line.rstrip('\n')
	#print type(n)
	n = int (n)	
	#print type(n)
	if n % 2 == 0:
		print n
fileRef.close()


 