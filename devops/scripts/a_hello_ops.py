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
        print 'hello devops... for the {}th time!'.format(i+1)
    return repeat_print

def get_input(x=None):
    """return int version user inputs from CLI or prompt
    """
    if x is not None:
        return x
    else:
        return int(raw_input('How many?: '))

if __name__ == '__main__':

    # get argv in this block to avoid collecting
    #     avoid collecting CLI input when runing
    if len(sys.argv) == 2:
        print_hello_devops_to_console(int(sys.argv[1]))
    else:
        print_hello_devops_to_console(int(get_input()))
