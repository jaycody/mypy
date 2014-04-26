# ex6:  Strings and Text

# assign strings (some of which contain format characters)
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# in this string, use the previous variables as formatted variables
y = "Those who know %s and who %s." % (binary, do_not) ### 2 strings inside string

#print the strings
print x
print y

# create compound format strings by making a format string itself a formatted variable 
print "I said: %r." % x  ### string inside a string
print "I also said: '%s'." % y  ### string inside string inside string

# create a boolean and assign it the FALSE value
hilarious = False
# create a string variable and assign to it a formatted string (without the formatted variable
# use a boolean as the formatted variable
joke_evaluation = "Isn't that jok so funny?! %r"  ###boolean inside string

# use the boolean as the formatted variable for a format string 
print joke_evaluation % hilarious

#print the format string without the use of the format variable 
print joke_evaluation  # results in the printing of the format character 

# declare string variables and assign values
w = "This is the left side of..."
e = "a string with a right side."

# concatenate strings by combining their variables using the arithmetic operator
print w + e

# compare concatenation methods
# concatenate strings:
print w + e

# concatenate a formatted string with a formatted variable
print joke_evaluation % hilarious


# find where strings are placed inside strings

# '+' concatenates the strings