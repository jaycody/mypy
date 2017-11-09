#! /usr/bin/python -tt

with open ('csm.txt') as f:
    for line in f:
        print line

        for char in line:
            print '{}'.format(char)
