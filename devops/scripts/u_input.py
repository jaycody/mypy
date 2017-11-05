#! /usr/bin/python -tt

'''
Asks for input and returns your answer.
'''


def get_answer(question):
    '''Prints your question to the console and returns your answer'''
    print question
    return raw_input()

def get_input():
    '''Prints 'enter:' to the console and returns your answer'''
    print 'enter:'
    return raw_input()



if __name__ == '__main__':
    print get_answer("answer me this:")

    print get_input()
