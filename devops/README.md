# devops
> gettin' Pythonic up in this mug
__

## Unit testing with nose2 and green
- [green](https://github.com/CleanCut/green)
- [nose2 docs](http://nose2.readthedocs.io/en/latest/usage.html)  
### Run all tests in a project
- from project root ```green -vvv --run-coverage```
- from project root: ```nose2```
### Run individual tests
- to run individual test script, pass in test script name using dot notation
     - ```nose2 calculator_app.test.unit.test_calculate_this```
- to run individual test cases, use ':' and specify the index of the test case (NOTHING YET)
     - ```nose2 calculator_app.test.unit.test_calculate_this:1```

### nose2 options
```
nose2 -v  #verbose
nose2 -h  #help
nose2 -s  #start directory
nose2 -t  #top directory
```
_____    

### direct from green's awesome documentation:

### External Structure ###

This is what your project layout should look like with just one module in your
package:


    proj                  # 'proj' is the package
    ├── __init__.py
    ├── foo.py            # 'foo' (or proj.foo) is the only "real" module
    └── test              # 'test' is a sub-package
        ├── __init__.py
        └── test_foo.py   # 'test_foo' is the only "test" module

Notes:

1. There is an `__init__.py` in every directory.  Don't forget it.  It can be
   an empty file, but it needs to exist.

2. `proj` itself is a directory that you will be storing somewhere.  We'll
   pretend it's in `/home/user`

3. The `test` directory needs to start with `test`.

4. The test modules need to start with `test`.


When your project starts adding code in sub-packages, you will need to make a
choice on where you put their tests.  I prefer to create a `test` subdirectory
in each sub-package.

    proj
    ├── __init__.py
    ├── foo.py
    ├── subpkg
    │   ├── __init__.py
    │   ├── bar.py
    │   └── test              # test subdirectory in every sub-package
    │       ├── __init__.py
    │       └── test_bar.py
    └── test
        ├── __init__.py
        └── test_foo.py


The other option is to start mirroring your subpackage layout from within a single test directory.

    proj
    ├── __init__.py
    ├── foo.py
    ├── subpkg
    │   ├── __init__.py
    │   └── bar.py
    └── test
        ├── __init__.py
        ├── subpkg            # mirror sub-package layout inside test dir
        │   ├── __init__.py
        │   └── test_bar.py
        └── test_foo.py


### Skeleton of Test Module ###

Assume `foo.py` contains the following contents:

```python
def answer():
    return 42

class School():

    def food(self):
        return 'awful'

    def age(self):
        return 300
```

Here's a possible version of `test_foo.py` you could have.

```python
# Import stuff you need for the unit tests themselves to work
import unittest

# Import stuff that you want to test.  Don't import extra stuff if you don't
# have to.
from proj.foo import answer, School

# If you need the whole module, you can do this:
#     from proj import foo
#
# Here's another reasonable way to import the whole module:
#     import proj.foo as foo
#
# In either case, you would obviously need to access objects like this:
#     foo.answer()
#     foo.School()

# Then write your tests

class TestAnswer(unittest.TestCase):

    def test_type(self):
        "answer() returns an integer"
        self.assertEqual(type(answer()), int)

    def test_expected(self):
        "answer() returns 42"
        self.assertEqual(answer(), 42)

class TestSchool(unittest.TestCase):

    def test_food(self):
        school = School()
        self.assertEqual(school.food(), 'awful')

    def test_age(self):
        school = School()
        self.assertEqual(school.age(), 300)
```

Notes:

1. Your test class must subclass `unittest.TestCase`.  Technically, neither
   unittest nor Green care what the test class is named, but to be consistent
   with the naming requirements for directories, modules, and methods we
   suggest you start your test class with `Test`.

2. Start all your test method names with `test`.

3. What a test class and/or its methods _actually test_ is entirely up to you.
   In some sense it is an artform.  Just use the test classes to group a bunch
   of methods that seem logical to go together.  We suggest you try to test one
   thing with each method.

4. The methods of `TestAnswer` have docstrings, while the methods on
   `TestSchool` do not.  For more verbose output modes, green will use the
   method docstring to describe the test if it is present, and the name of the
   method if it is not.  Notice the difference in the output below.

   ### Running Green ###

   To run the unittests, we would change to the parent directory of the project
   (`/home/user` in this example) and then run `green proj`.

   **In a real terminal, this output is syntax highlighted**

       $ green proj
       ....
       Ran 4 tests in 0.000s

       OK (passes=4)

   Okay, so that's the classic short-form output for unit tests.  Green really
   shines when you start getting more verbose:

   **In a real terminal, this output is syntax highlighted**

       $ green -vv proj
       proj.test.test_foo
         TestAnswer
       .   answer() returns 42
       .   answer() returns an integer
         TestSchool
       .   test_age
       .   test_food

       Ran 4 tests in 0.001s

       OK (passes=4)

   Notes:

   1. Green outputs clean, heirarchical output.

   2. Test status is aligned on the _left_ (the four periods correspond to four
      passing tests)

   3. Method names are replaced with docstrings when present.  The first two tests
      have docstrings you can see.

   4. Green always outputs a summary of statuses that will add up to the total
      number of tests that were run.  For some reason, many test runners forget
      about statuses other than Error and Fail, and even the built-in unittest runner
      forgets about passing ones.

   5. Possible values for test status (these match the `unittest` short status characters exactly)
    - `.` Pass
    - `F` Failure
    - `E` Error
    - `s` Skipped
    - `x` Expected Failure
    - `u` Unexpected pass

_____



## Exercises
### as they come to mind:
- [x] helloworld, oh yeah
- [ ] recreate cat
- [ ] modulus something something

## Pythonic notes

## Sources
- Think Python
- Google Python class
- PEP 8 & PEP 20
