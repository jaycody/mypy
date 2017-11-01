# ex13:  Parameters, Unpacking, Variables

'''
from sys import argv   # ask for argv (command line argument) method from the sys module

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
'''

from sys import argv # make ready the Argument Variable feature (argv) of the sys module


script, location, velocity, acceleration = argv

print ""
print "Command line Argument Variables (argv) ACCEPTED"
print "Force type still unknown."
print ""
force = raw_input("       Enter Force type to proceed: ")
print ""
print "List of Current Values:"
print "\t*Current position =", location
print "\t*Trajectory Vector =", velocity
print "\t*Velocity Delta vector =", acceleration
print "\t*Force type =", force
print ""
