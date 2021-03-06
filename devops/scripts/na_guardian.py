#! /usr/bin/python -tt

'''
The Guardian protects us from unwanted inputs.
'''

def approve_of(input_as_list):
    '''
    Accepts a list.
    Returns true if all vars in list are positive integers.
    '''
    ## if it's a list
    if isinstance(input_as_list, list):
        print 'Guardian received your list of inputs...'
        ## and if all items in the list are ints
        ## GENERATOR 
        if all(isinstance(item, int) for item in (input_as_list)):
            ## and if all ints are positive
            ## GENERATOR!!!
            if all(item > 0 for item in (input_as_list)):
                print '\t...and has verified inputs as positive ints. \n   You may proceed'
                return True
            print '\t...but your inputs contain negative ints. Guardian expects only positive. Try again!'
            return 0
        print '\t...but your inputs contain non ints. Try again!'
        return 0
    else:
        print 'Guardian received your input... \n\t...but Guardian expects a list of positive integers. Try again!'
        return 0


def is_pos_int(input_as_int):
    '''
    Returns true for a positive int.
    '''
    if isinstance(input_as_int, int):
        if input_as_int > 0:
            return True

    return False


if __name__ == '__main__':
    print '1 is a postive int.', is_pos_int(1)
    print '-1 is a postive int.', is_pos_int(-1)
    print "'1' is a postive int.", is_pos_int('1')


    #my_list = [1,2,-3,'my']
    my_list = 'oops'
    my_int  = 1
    #guardian_approves_of(my_list)
