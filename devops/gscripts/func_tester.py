#! /usr/bin/python -tt

"""Function tester adapted from exercies in Google's Python class"""

def donuts(x):
    return 'Number of donuts: {}'.format(x)

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '{} got: {} expected: {}'.format(prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print 'donuts'
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
