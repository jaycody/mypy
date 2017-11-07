#! /usr/bin/python -tt

"""Recursively computes the length of an input string. Returns int.
"""

def lenrecur(count_this):
    """Accepts a string. Recursively counts its length. Returns length as int.
    """

    if isinstance(count_this, basestring):
        return 1

    else:
        return "Expted string! Received {}".format(type(count_this))










print lenrecur('test Pass')

print lenrecur(('test Pass',))
