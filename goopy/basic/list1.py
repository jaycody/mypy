#! /usr/bin/env python -tt
"""j stephens - mypy gongfu
use doctest for all functions
$ python -m doctest -v list1.py
"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
  """Determine how many strings from the list are longer than 2 chars 
  and also share first and last chars.
  >>> match_ends(['jose', 'jokej', 'jecklerj', 'noten', 'jalj'])
  4
  """
  count = 0

  for word in words:
    if len(word) >= 2:
      if word[:1] == word[-1:]: 
        count += 1

  return count
  



# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
  """Sort lists such that x leads the sort order before alphanumeric.
  >>> front_x(['alpha', 'charli', 'beta', 'xanadu'])
  ['xanadu', 'alpha', 'beta', 'charli']
  """
  xList = []
  otherList = []
  combinedList = []
  for item in words:
    if item[:1] == 'x':
      xList.append(item)
    else:
      otherList.append(item)
  
  xList = sorted(xList)
  otherList = sorted(otherList)
  # Debug
  combinedList = xList + otherList
  #print "xlist = ", xList
  #print "otherList = ", otherList
  #print "combinedList = ", combinedList
  return combinedList

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
  """Sort a list of tuples according to the last element of each tuple
  >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
  [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
  """

  sortedList = sorted(tuples, key=custom_key)
  return sortedList

def custom_key(tupleKey):
  """Find and return the last element of a tuple
  >>> custom_key((1, 7))
  7
  """
  return tupleKey[-1]


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  """
  >>> 's' == 's'
  True
  """
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
