# ex15:  Reading Files

'''
open(fooFileName) --> returns a file object
	example:   txt = open(filename) #where 'txt' variable stores the file object
	- creates a new file if one does not already exist
	
fileObject.read() -> calling functions on the file object!!!! 
	txt.read() -> dot syntax
	print txt.read()

fileObject.close() -> because it's important to close the file after your done.

'''

from sys import argv # make available the argument variables from the sys module

#declare the argument variables and set the value of argv from command line input
script, filename = argv  # these are required at the command line
# create a string to hold the prompt to be used in the raw_input(<prompt> field)
prompt = '>  '

'''
Use the argv for the filename entered at the command line.
Use the 'open' function to create a file object from the file of that name
The 'open' method returns a FILE OBJECT.  
Assign the FILE OBJECT to object variable.  now we have an actual version of
The file loaded and accessible by a variety of methods functions made available 
	by the file object (ex:  dot read, accessible by dot syntax)
'''  # comment a comment?  nice

txt = open(filename)

#remind the user what's actually going on here using actual file name
print "Here is your file: %r" % filename #where formatter %r is raw everything
# print the results of the call to the file object's read command

print txt.read()
#txt.write("Oh yeah, just added another line for you, btw")
print txt.readlines(6)

'''
User enters file name again, this time during the running of the script.
Now we have filename information entered before and during the script run
	- an argv from command line and while script is running
'''

print ""
print "Please type the filename again:"
file_again = raw_input(prompt)


'''
use the string containing the filename to inform the 'open' command
the open command returns a file object. 
the object variable is declared and assigned here with the object
returned from the open command function.
'''

txt_again = open(file_again)

# remind the user what's going on here.  we're about to display the file again
print""
# use the formatted string to incorporate the filename into the interaction
print "  Here's the text again for file: %s" % file_again

# call the read function on the file object stored in the object data type
# print the results of the read function call
print txt_again.read()
print txt_again.readlines(6)

print ""
print "Anything else we can help you with today, sir?"

# close the files now that I'm done.  important to n clearnup aftermyself
txt.close()
txt_again.close()

