#ex10:  What Was That?

'''
- STRING FORMATTING OPERATIONS
	%s uses the str() function. {use for DISPLAYING}
	%r uses the repr() function. {use for DEBUGGING}
		- aka 'RAW REPRESENTATION'
		- when used with strings, %r displays quotes and special chanacters
"""
- escape sequences:  inserting commands into strings  
	\n -> new line
	\\ -> double back slash escapes the escape
	\'  \"  -> escaping single and double quotes
	\t -> tab
	\a -> ASCII bell
	\b -> backspace
	\f -> formfeed (in english please)
	\n -> linefeed (aka newLine)
	\r -> carriage return
	\t -> horizontal tab
	\v -> vertical tab
'''

tabby_cat = "\tI'm tabbed in."  # append the string with tab spaces
persian_cat= "I'm split\non a line." # creates a new line inside the string
backslash_cat = "I'm \\ a \\ cat."  # double back slashes escape the escape

# make an list outline with tabbed entries !!!!
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
'''
print "\n"
print tabby_cat
print "\n"
print persian_cat
print "\n"
print backslash_cat
print "\n"
print fat_cat
'''
'''
while True:
	for framesToDisplay in range(0,3):
		for i in ["\\O/", " O",]:
			print "%s\r" % i,
		for i in [" |", "/|\\",]:
			print"",
			print "%s\r" % i,
'''
'''
#while True:
for duration in range (10000):
	for i in range(10):
		print "\t\\O/\r",
	for i in range(10):
		print "\t_O_\r",
		#print tabby_cat
	##if duration > 999:
	##	break
'''
print "\n"
print "*****STRING FORMATTING OPERATIONS**********"
print "\n"
print "If I'm tabbed, then: %s" % tabby_cat, " --> USES %s formatter"
print "If I'm tabbed, then: %r" % tabby_cat, " --> USES %r formatter"
print """
\t--> %s uses the str() function. {use for DISPLAYING}
\t\t*displays actual string, and DOES recognize escape backslash
\t--> %r uses the repr() function. {use for DEBUGGING}
\t\t*when used with strings, %r displays quotes and special chanacters
"""

