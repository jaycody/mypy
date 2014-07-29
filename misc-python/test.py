#!/usr/bin/env python -tt

"""jstephens - pyfu - 2013


Harrison tutorial covering commands, functions and classes
written in the form of printing techniques.
"""

#____
print "script"
#----

#____
def print_stuff():
	print "method"

print_stuff()
#----

#____
class DontPrintStuff(object):
	def __init__(self):
		print "dont do it"

	def meth_a(self):
		print "method a"
#----


#____
class PrintMoreStuff(DontPrintStuff):
	def __init__(self):
		super(PrintMoreStuff, self).__init__()
		print "Im printing stuff"

	def meth_a(self, msg):
		print msg


pms = PrintMoreStuff()
pms.meth_a("SUP")




DontPrintStuff()

dps = DontPrintStuff()
dps.meth_a()
