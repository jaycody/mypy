#! /usr/bin/python -tt

"""Prints 'hello ops' to the console.

- Takes either CLI argument or prompt input
- Fails to fail safe when inputs are not ints
"""

import sys

def print_hello_devops_to_console(repeat_print=1000):
    """Print to console as many times as input or default dictates.
    """

    for i in xrange(repeat_print):
        print 'hello devops... for the {}th time!'.format(i)

def get_input():
    """return the user inputs from CLI or prompt
    """

    # use console input, otherwise use default
    if len(sys.argv) > 1:
        return int(sys.argv[1])

    else:
        return int(raw_input('How many?: '))

if __name__ == '__main__':

    print_hello_devops_to_console(get_input())
