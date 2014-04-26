#ex17:  More Files

'''
os.path module  -->  exists

'''


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r') # open the file and make it readable

in_file_data = in_file.read()

print "The input file is %d bytes long." % len(in_file_data)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("?  ")




#take data from a file, hold it in a variable, 
#then tell the other file object to write to itself the first file's data held in the variable
#create file object for the file to which we write
out_file = open(to_file, 'w')

#to this file object just opened, call the write function
#then pass as an argument the fromFileData to which the fromFileObject was read.
out_file.write(in_file_data)


print out_file

out_file.close()
in_file.close()

