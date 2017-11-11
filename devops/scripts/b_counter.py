#! /usr/bin/python -tt


def count(from_where='from default val, yo'):
    print '\nHere, {}'.format(from_where)

    total = 0
    for i in from_where:
        #print i
        total += 1
    return from_where, total

if __name__ == '__main__':

    from_where = 'from da main in da b_counter function'

    print '\ncall count()', count(from_where)
    for i in xrange(10):
        print (from_where)
