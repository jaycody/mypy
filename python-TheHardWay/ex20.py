# ex20:  Functions and Files


'''


'''

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First, let's print the entire file: \n"

print "To print the entire file, select ENTER", raw_input('>  ')
print_all(current_file)

print "To REWIND, select ENTER", raw_input('>  ')
rewind(current_file)

print "To print 3 lines, select ENTER", raw_input('>  ')

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file_data = current_file.read()
print "Length of doc:  %d" % len(current_file_data)
print "Current file position : %d" % current_file.tell()
print ""
print "Specify new file position between 0 and %d" % len(current_file_data)
toLocation = raw_input('>  ')

print""
print "You entered location %s" % toLocation
current_file.seek(int(toLocation))
print "Current file position : %d" % current_file.tell()

print ""
print "To print from this point on, select ENTER.", raw_input('>  ')
print ""
print_all(current_file)

