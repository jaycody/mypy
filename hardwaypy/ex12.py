# ex12:  Prompting People

'''
-> STRING FORMATTING OPERATIONS -->  "%s, %s" % (x, y)
-> raw_input()  
		- prompts for input, returns string
		- add prompt:  yourName = raw_input("Name? ")
-> pydoc <python function>  [type 'q' to quit]
		- similar to man in terminal
		ex: pydoc raw_input
-> pydoc (open, file, os, sys)

-> file(object) -> modes 'r', 'w', 'a' (reading, writing, appending)
'''

age = raw_input("How old are you? ")
height = raw_input("How tall are you? (include units) ")
weight = raw_input("How much do you weigh? (include units ")

print "So you're %s years old, you are %s tall, and you weigh %s." % (age, height, weight)



