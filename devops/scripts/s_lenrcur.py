#! /usr/bin/python -tt

"""Recursively computes the length of an input string. Returns int.
"""

def lenrecur(count_this):
    """Accepts a string. Recursively counts its length. Returns length as int.
    """
    #total = 0
    def initialize(count_this):
        total = 0
        return recursive_count(count_this,total)

    def recursive_count(count_this, total):
        print "Counting chars in string: '{}'".format(count_this)
        print 'Current count = {}'.format(total)

        # base case if string is empty
        if not count_this:
            print 'string is empty'
            print "\n Final char count: {}\n".format(total)
            return total
        else:
            total += 1
            return recursive_count(count_this[1:], total)




    return initialize(count_this)

    #return 'Final count: {}'.format(total)





#print "Test 1: ", lenrecur('test Pass')


#print lenrecur('all')
test_string = 'Dada, I told my class the story about how I took your bishop this weekend when we played chess'
calculated_length = lenrecur(test_string)

print "Calculated length of:'{}' is {}".format(test_string, calculated_length)
print "Expected: {}\n".format(len(test_string))

if len(test_string) == calculated_length:
    print "\t---->PASS<----"
else:
    print "\t---->FAIL<----"

#print "Test 1: ", lenrecur('')

#print "Test 2: ", lenrecur(('test Pass',))
