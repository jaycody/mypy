# ex16:  Reading and Writing Files

'''
FILE OBJECT METHODS TO REMEMBER:
	* close  -- Closes the file, acts like File->Save in the editor
	* read		Reads and returns the files contents. assignable 
	* readline  reads just one line of the text file
	* truncate  empties the file. watch out if you care about the file
	* write(stuff) writes stuff to the file. yeah boyeee

'''

from sys import argv

script, filename = argv



print ""
print "		Here are the current contents of file: %s" % filename
print""
target = open(filename, 'r') 
print target.read()
print""
print "The contents of %s are about to be erased." % filename
print "To stop this process, hit CTRL-C."
print "To proceed with truncation of %s, hit ENTER." % filename
raw_input("?  ")


print "      Truncating Now......"
target = open(filename, 'w')  
target.truncate()

print ""
print "To proceed with content production, select ENTER", raw_input('>  ')
print ""
print "Please enter 3 new lines:"
newLine1 = raw_input("Line 1:  ")
newLine2 = raw_input("Line 2:  ")
newLine3 = raw_input("Line 3:  ")

print "Press ENTER to write the new lines to %s" % filename, raw_input('>  ')
target.write(newLine1 + "\n" + newLine2 + "\n" + newLine3 + "\n")
#target.write("\n")
#target.write(newLine2)
#target.write("\n")
#target.write(newLine3)
#target.write("\n")

print ""
print "      New Lines successfully added!!!"
print ""
print "Press ENTER to view the new content for file: %s" % filename, raw_input('>  ')
print ""
# seems like we have to open the file everytime before reading or writing to it.
target = open(filename, 'r')
print target.read()
print ""
print "Press ENTER to close file: %s" % filename, raw_input('>  ')

target.close()
