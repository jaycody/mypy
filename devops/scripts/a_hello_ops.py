#! /usr/bin/python -tt

import sys

def print_hello_devops_to_console():
    if len(sys.argv) > 1:
        repeat_print = int(sys.argv[1])
    else:
        repeat_print = 100

    for i in xrange(repeat_print):
        print 'hello devops ', i


if __name__ == '__main__':
    print_hello_devops_to_console()
