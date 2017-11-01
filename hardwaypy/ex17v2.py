# ex17v2:  More Files

'''

'''

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r')  # bring file into python and save it as a file object
indata = in_file.read()  		# 1. read the contents of the file object and 
								# 2. save the contents so I can reread it anytime
								
print "The input file is %s bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

print""
print indata
print""
print "Hit ENTER to continue", raw_input('<  ')


out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."


# now close the virtual FILE objects
out_file.close()  # 'virtual' file object's new info is saved to the actual file on the drive
in_file.close()