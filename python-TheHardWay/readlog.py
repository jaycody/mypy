#!/usr/bin/python
#
# Read a specified log file from where it was last read.  Output to stdout
# the latest entries.  Log may have been logrotated.  
# -s is a seek file that keeps the seek offset from previous run
# -f is the log file to read
# If the seek value is larger than the file size, it's been rotated and seek
# is reset to 0
#
import sys, getopt, os, re

# Usage help message
def Usage():
	print "readlog -s <seek file> -f <log file>"
	sys.exit(0)

# Initializations
seekfile = None
logfile = None

# Get Options
try:
	optlist, list = getopt.getopt(sys.argv[1:], ':hs:f:')

except getopt.GetoptError:
	Usage()

# Options are
#  -h help
#  -s seek file
#  -f log file

for opt in optlist:
    if opt[0] == '-h':
        Usage()
    if opt[0] == '-s':
		seekfile = opt[1]
    if opt[0] == '-f':
		logfile = opt[1]

if seekfile == None:
	Usage()
if logfile == None:
	Usage()

# open the seek file, or create it if it [a] doesn't exist or [b] is corrupt
seekfileShouldCreate = True
if os.path.exists(seekfile):
	try: 
		sf = open(seekfile, 'r+')
	except IOError, err:
		print("Can't open seek file %s for reading : %s" %
							(seekfile, err.strerror))
		sys.exit(1)
	# read last seek position
	seekfileContents = sf.read()
	isInt = re.search('^\d+$', seekfileContents)
	if isInt:
		seekpos = int(seekfileContents)
		sf.seek(0)
		seekfileShouldCreate = False
	else:
		print 'Corrupt seekfile contained [%s], will seek at 0' % seekfileContents
		sf.close()

if seekfileShouldCreate:
	# File didn't exist, create it
	try: 
		sf = open(seekfile, 'w')
	except IOError, err:
		print("Can't open seek file %s for writing : %s" %
							(seekfile, err.strerror))
		sys.exit(1)
	seekpos = 0

# Open the log file
#	raise AssertionError("Can't open log file %s for reading : %s" %
try: 
	lf = open(logfile, 'r')
except IOError, err:
	print("Can't open log file %s for reading : %s" % (logfile, err.strerror))
	sys.exit(1)

# seek the end and get the position
lf.seek(0,2)
logend = lf.tell()

# if seek position is great then file size, it rotated
if seekpos > logend:
	seekpos = 0

# Set offset for reading
lf.seek(seekpos)

# print to stdout without \n
for line in lf:
	print line,

# save last read position to file
sf.write("%d" % lf.tell())

# Clean up
sf.close()
lf.close()

sys.exit(0)
