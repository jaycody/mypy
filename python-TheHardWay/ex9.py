# ex9:  Printing, Printing, Printing

# Here's some new strange stuff, remember type it exactly.

# declare variable and assign string of days of the week
days = "Mon Tue Wed Thu Fri Sat Sun"

# declare variable and assign string of months.  Add new line using the backslash escape '\n'
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# concatenate string using comma and variable string
print "Here are the days: ", days

# concatenate by adding string variable to string.
# prints new lines for every month after Jan
print "Here are the months: %s " % months

'''
similar to the triple single quotes that create a block of comments,
the triple double quotes allow for a block of string.
ex:
'''

print """
There's something going on here.
With the trhee double-quotes.
We'll be able to type as muchas we like.
Even 4 lines if we want, or 5, or 6.
"""