#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    """Remove adjacent equivalent elements and return as list"""

    consolidated = []

    # If incoming list is empty, send back an empty list
    if not nums:
        return consolidated

    # Find and consolidate adjacent duplicates
    for i, val in enumerate(nums):
        # Stop! You've reached the end of the list.
        #   Do not compare val to index+1! Avoid 'out of range boundary' error. Return the consolidate list
        if i >= len(nums)-1:
            consolidated.append(val)
            return consolidated

        elif nums[i] is not nums[i+1]:
            consolidated.append(val)


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    """Consolidate 2 lists, then sort and return the results.
    1. zip two lists together
    2. custom sort on iteration?
    """
    # waaay over thought this one.
    ## previous to this: used izip, then zip,
    # I guess the l1 + l2 concatenation is cheating and inefficient
    #return sorted(list1 + list2) # reverse=True

    ### ahh, the list are already sorted before we start!
    ###     which means the remainder in either list can be tacked on
    ###     because they'll already be sorted.

    ## so, new solution:
    ## while neither list is empty:
    ##     compare the first items from both lists
    ##     pop the smallest out of its list
    ##          and append it to a result list
    ##     repeat until 1 or both lists are empty
    ##     than extend both lists to results list,
    ##          (one of the 2 lists will be empty so order doesn't matter)
    result = []
    while list1 and list2:              # while run until 1 list is empty
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    result.extend(list1)
    result.extend(list2)
    return result

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])



if __name__ == '__main__':
  main()
