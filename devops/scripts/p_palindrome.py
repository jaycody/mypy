#! /usr/bin/python -tt

'''
Determines if a given string is a Palindrome
'''

def isPalindrome(s):
    return s

def toChar(s):
    '''
    Removes all whitespace and punctuation from a string
    Returns a squeeky clean version of the string in lowercase
    '''

    ans = ''

    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans += c


    return ans + ' (cleaned version)'




print isPalindrome(toChar('can you see me'))
