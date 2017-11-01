#!/usr/bin/env python  -tt
# ex32: Loops and Lists			 (file by mk.py)

'''
Lists:
	'['  --> the left bracket OPENS the list
	','  --> the comma SEPARATES the list items
	']'  --> the right bracket CLOSES the list
	- are MUTABLE (mutationable)

For-Loops:
	Definite steps
	through a list	
'''


the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'peers', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#for-loop through a list with a definite range
for number in range(5):
	print "this loop the count = %d" % the_count[number]
	
	
#loop through a list using the numberr of itmes in the list as the range:
for count in the_count:
	print "the count now is %d" % count

#loop through a llist of strings
for fruit in fruits:
	print "the current fuit is %s." % fruit


#loop throuh a combo of strings and digits
for stuff in change:
	print "I got %r." % stuff
	
#build a list:
elements = []

# populate a list using .append()
for i in range (0, 6):
	print "Adding %d to the list." %i
	elements.append(i)  #important to note here!! what 'i' is:
	# 'i' is the value for a particular index.
	# 'i' is NOT the index itself.  the for loop iterate through the indices
	# then 'i' is assigned the value at each index to
	# to use elements.append[] is wrong because we don't append based on index, we just
	# use .append(VALUE) to add the value to the end of the list 
	
# iterate through the new list 'elements' and print each item
for i in elements:
	print "Element add:  %d" % i
	
	
#populate the list with a for loop
for i in range(100): 
	elements.append(i)
print elements
	
	
#display the list with a flor loop:
for i in elements:
	print "this is the current value %d" % i
	
	



