# Printing Printing

# create variable and assign it a format string composed of only format characters
formatter = "%r %r %r %r"

# print the format string and use a list of ints to inform the format variables
print formatter % (1, 2, 3, 4)

# print the format string and use a list of strings to inform the format variables
print formatter % ("one", "two", "three", "four")

# print the format string and use a list of BOOLEANS to inform the format variables
print formatter % (True, False, False, True)

# print the format string and use a list of VARIABLES to inform the format variables
print formatter % (formatter, formatter, formatter, formatter)


# print the format string and use a list of strings to inform the format variables
# use line breaks at the commas to adhere to the 80 character width 'best practice' of python
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing",
	"So I said goodnight."
)


'''
the output of the last print command contains strings with double and single quotes
even thought all the strings in the list used to inform the format variables
are all double quoted.  Why?
b/c double quotes are used in the string that contains a single quote used an apostrophe.
'''
