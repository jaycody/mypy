#! /usr/bin/python -tt

'''
Towers of Hanoi solution using dual recursive calls inside a single recursive function
Steps:
 1. solve a simpler version (move stack of n-1 to temp)
 2. solve the base case     (move disk to destination)
 3. solve a simpler version (move stack of n-1 back start)

 label the pegs A B C
 let n = total number of disks
 number the disks 1 (smallest, top-most) to n (largest, bottom-most)

 begin:
    - assume there are 'm' top disks on a source peg and that all other pegs are bigger
    - to move 'm' disks from source peg to a target peg using a spare peg

NOTE: (from wikipedia)
The following code highlights an essential function of the recursive solution,
which may be otherwise misunderstood or overlooked.
That is, with every level of recursion,
the first recursive call inverts the target and auxiliary stacks,
while in the second recursive call the source and auxiliary stacks are inverted.
'''

from __future__ import print_function

import sys

if len(sys.argv) > 1:
    disks = int(sys.argv[1]) + 1
else:
    disks = 6

A = range(1, disks)
A = A[::-1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n >= 1:
        # move n-1 from source to auxiliary so that they're out of the way
        # so from this crew, auxiliary IS the target
        move(n-1, source, auxiliary, target)

        # move the nth disk from source to target
        # pop the nth disk from the stack of disks on source
        #   and append it to the target peg
        target.append(source.pop())

        # print progress
        #print (A, B, C, '##########', sep = '\n')
        show_progress()
        # then move the disks currently waiting on auxiliary to target via source
        move(n-1, auxiliary, target, source)

def show_progress():
    print (A, B, C, '##########', sep = '\n')

# show starting position
show_progress()

# initiate call from source A to target C
move(len(A), A, C, B)
