#! /usr/bin/python -tt

"""Function tester - simplest version"""


def check_if(x=None):
    return x


def test(got=None, expected=None):
    return got, expected



def main():
    #print check_if('to check'),

    print test(check_if('sent_to_test'), 'sent_as_expected')



if __name__ == '__main__':
    main()
