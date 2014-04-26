#!/usr/bin/env python
# mk.py:  Make Python File

'''
write a script that will: 
	1. create a .py file for a given assignment (w/o overwriting existing files)
	2. load that file into Text Wrangler

ToDo:
- [] ADD the env path to python as the first line  #!/usr/bin/env python
- [] make file executable
- [] create default setting with NO argv from command line.  If no argv, the create
		file name based on time stamp	
'''

from sys import argv
from os.path import exists
import os

script, new_Script_Name = argv

#*********************************************************
'''
Test if name already exists to avoid overwriting existing file.
	- if file does NOT exist, then: 
			--> return that name and proceed to make that file
	- if file DOES exist, then:
	 		--> ask for a new name, and 
	 		--> recursively call avoidOverWrite function on new name
'''
def avoidOverWrite(f):
	newName = f #create an empty string to contend with issues of scope
	doesExist = exists(newName)
	if doesExist == True:
		print ""
		print ""
		print ""
		print "-----File: %r already exists!-------" % f
		print""
		print "   Enter new name or CTRL-C to quit"
		newName = str(raw_input('    --->  '))
		#print""
		#print"\t(Inside Function)You Entered %r" % newName
		#newNameType = type(newName)
		#print "It's data type = ", newNameType
		#print"Hit ENTER to proceed or CTRL-C to quit", raw_input('>  ')
		approvedName = avoidOverWrite(newName)
		return approvedName
	else:
	#if doesExist == False:
		return newName
#*********************************************************	
		
		
#tests whether it exists to avoid overwriting file
new_Script_Name_Approved = avoidOverWrite(new_Script_Name) 

print""
print""
print "Hit ENTER to create new script: ", new_Script_Name_Approved,; 
raw_input('   > ')
#new_Script_Type = type(new_Script_Name_Approved)
#print "It's data type = ", new_Script_Type


#opening a non-existent file creates a FILE OBJECT
new_Script_FileObject = open(new_Script_Name_Approved, 'w') 

#write the basic setup for the python script including the main function
new_Script_FileObject.write(
"#!/usr/bin/env python \t-tt\n\n# " + new_Script_Name_Approved + "\t\t\t (file by mk.py)"
+ "\n\n\"\"\"\n\n\n\"\"\"\n\nimport sys\n\n# Define a main() function\ndef main():\n"
+ "\t\"\"\"documentation comments here\"\"\""
+ "\n\n\n\n\n\n\n# This is the standard boilerplate that calls the main() function.\n"
+ "#This indefinite loop will not run when the script is called as a module by another script.\n"
+ "if __name__ == '__main__':\n\tmain()")



print""
print"CREATED FILE:  %r" % new_Script_Name_Approved
#print "Hit ENTER to verify the creation of: %s" % new_Script_Name_Approved, raw_input('>  ')
#print"Does file: %s exist? [%r]" % (new_Script_Name_Approved, exists(new_Script_Name_Approved)),;
#raw_input('    -> Hit ENTER to proceed')
print""
print"Hit ENTER to open %s in Text Wrangler" % new_Script_Name_Approved,; 
raw_input('>  ')

os.system("open -a /Applications/TextWrangler.app " +new_Script_Name_Approved)




