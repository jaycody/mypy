#! /usr/bin/python -tt

""" Iterative function that calculates and returns the length of an input string.
Validates data type first.
"""


def fast_string_length(s="requires input"):
    """Counts and returns the elements in a string.
    Walks throught the string with a for in each iteratior
    """

    count = 0
    for i in s:
        count += 1

    return count


## Add these to the test script
test_string = "blammmmooooh"
print "\nTest_string: '" + test_string + "' has element count of ", fast_string_length(test_string)

test_string = "ba;alsdjga;jga;jga;jgajgajgdjrj"
print "\nTest_string: '" + test_string + "' has element count of ", fast_string_length(test_string)
print 'Verified length: ', len(test_string)


print '\nTest Default value for fast_string_length function:'
print 'Default string, ' + fast_string_length.func_defaults[0] + "', has element count: ", fast_string_length()

print '\nFunction name: ', fast_string_length.func_name
#print fast_string_length.func_code
print '\nDefault values: ',  fast_string_length.func_defaults
#print fast_string_length.func_globals

print '\nFunction id=', id(fast_string_length())

print '\nFunction id={}'.format(id(fast_string_length()))
