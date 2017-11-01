# ex14:  Prompting and Passing

'''
argv  -> argument variables

raw_input()  -> user input

prompt string assigned to 'prompt' variable and used in raw_input(<prompt>) position
'''

from sys import argv # give me argv feature of sys module

script, user_name = argv
prompt = '-->  '

print "Hi %s, I'm the %s." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me?"
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have %s?" % user_name
computer = raw_input(prompt)

print """
Alright, to sum this up, %r:
You said %r about liking me.
You live in %r.  Not sure where that is.
And you have yourself a %r.
""" % (user_name, likes, lives, computer)