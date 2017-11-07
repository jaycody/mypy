# practice practice practice
> Actually, to get to Carnegie Hall, go up to Houston St, head west 1/2 block and make a right on 1st Ave. Go up to 4th St and make a left. Head west on 4th, cross Broadway and keep going until you hit Washington Square Park. Cut across the park, go through the arch then head uptown on 5th Ave. Stay on 5th Ave until you pass Madison Square Garden, then make a left onto West 29th. Go up 1/2 block and stop at the Ace Hotel for a cup a coffee.  From there, continue west on 29th for 2 more blocks, make a right on 7th Ave, and head straight for Times Square (don't let those jaded New Yorkers deter you, either!). March right on through Time Square and keep going until you get to within a few blocks of Central Park. There you'll find Carnegie Hall on the east side of 7th Ave between West 56th and West 57th.

______________

## my py exer-sy ...zez
Pulling problem sets and insights from various places, como:
- [MIT 600x via edX][1] (the archived course from 2015)
- Think Python text
- Google Python class

## PEP8 NOTES
- default param assignments have no space
```
myfunction(space=None)
```
- use string methods over slice to query string elements
```
# returns booleans
str.startswith('char') # or ('char', startIndex, endIndex)
str.endswith('char')
# not
if str[0:3] == 'char'
```
- check type with isinstance(var, type)
```
# this
if isinstance(myvar, int):
# not
if type(var) == type(int):
```
- check for string type with ***basestring***
  - basestring accounts for both ASCII and unicode, whereas ***string*** accounts only for ASCII in Python 2, and will return false if the string is in unicode
```
if isintance(mystrin, basestring)
```
- check if length == 0 WITHOUT using len(mylist)
  - the trick: an empty list return false
```
# YES
if mylist:      # Returns false if len 0
if not mylist:  # Returns true if len 0

# NO
if len(mylist) == 0:
```
- don't add extra white space to align assignments
  - for the record, I disagree with this
```
# NO
myvar         = 10
qb            = 'Paul Crewe'
mylongestvard = 'Mean Machine'
film          = 'The Longest Yard'
```
- check for existence of ALL types (because some types may be hiding (eg container))
```
# accounts for existing 'x' of type that returns false
if x is not None:

# NOT
if x:
```

## what I learned today:
### Printing with str.format()  !!!!
>
```
print '\nFunction id={}'.format(id(fast_string_length()))
```

### Default Parameters for Functions
```
myfunction(default_value=100)
```

### Query your function!:
```
# get name and defaults
name = myfunc.func_name
values = myfunc.func_defaults

# get other cool stuff
code = myfunc.func_code
these = myfunc.func_globals
```

### GET ID
```
objectID = id(object)

functionID = id(function())
```






[1]:https://courses.edx.org/courses/course-v1:MITx+6.00.1x_7+3T2015/course/
