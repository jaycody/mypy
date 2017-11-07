#! /usr/bin/python -tt

""" Determines if a given string is a Palindrome.
"""

def isPalindrome(string_to_check):
    #print "steps:"
    #print "\t0: isPalindrome() gets called with string: " + string_to_check
    #print "\t1: string '" + string_to_check + "' arrives inside isPalindrome function."
    #print "\t2: isPalindrome passes this string toChar, which munges it and passes to isPal "
    #print "\t3: isPal compares first and last chars in the string. Returns true if Palindrome"

    def toChar(chars_to_clean):
        """ Removes all whitespace and punctuation from a string.
        Returns a squeeky clean version of the string in lowercase.
        """

        ans = ''

        for c in chars_to_clean:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        #print '\n Original string converted from ' + chars_to_clean + ' to ' + ans + '\n'
        return ans


    def isPal(s):
        """ Recursively checks the first and last letters of a string.
        Returns True if string is palindrome.
        """

        # base case
        ## MAKE PEP 8 COMPLIANT: EMPTY SEQUENCES EVALUATE TO FALSE. USE: if not mylist:
        if len(s) == 0 or len(s) == 1:
            print '\nYES! String: ' + string_to_check + ' is a Palindrome\n'
            return True

        # compare first and last chars:
        #### MAKE PEP8 COMPLIANT BY REPLACING SLICES WITH STRING METHODS startswith(), endswith
        if s.startswith(s[-1]):
        #if s[0] == s[-1]:
            #print 'recursive case! String is now: ' + s
            return isPal(s[1:-1])
        else:
            print '\nNO! String: ' + string_to_check + ' is NOT a Palindrome\n'
            return False

    result = toChar(string_to_check)
    result = isPal(result)
    return result
    #return isPal(toChar(string_to_check))


isPalindrome('bcdefggfedcb')
isPalindrome('bcdefgtyfffytgfedcb')
isPalindrome('bcdefggfedc56yfa4   234b')
isPalindrome('bcdefgrhsthsjgfedcb')
#print isPalindrome('c')
