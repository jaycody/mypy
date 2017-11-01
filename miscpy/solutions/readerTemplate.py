fileRef = open('numbers.txt')
allLines = fileRef.readlines()
for line in allLines:
	print line.rstrip('\n')
fileRef.close()


