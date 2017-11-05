#! /usr/bin/python -tt

'''
Towers of Hanoi solution using dual recursive calls inside a single recursive function
Steps:
 1. solve a simpler version (move stack of n-1 to temp)
 2. solve the base case     (move disk to destination)
 3. solve a simpler version (move stack of n-1 back start)
'''
