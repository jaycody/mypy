### Excercises from the book, Python Testing:    
An Easy and Conveniant Approach to Testing Your Python Projects  
by Daniel Arbuckle (2010)  
____________________________

####Part I:  Doctest - The Easiest Testing Tool
- uses .txt file
- anything that can be expressed in python is valid in doctest
- from command line  
```$ python -m doctest foo.txt```

#####Doctest syntax:
```
>>> def startsWithPrompt():
...    print "continues with ellipsis"
...    print "blank line is for expected answer"
... startsWithPrompt()
continues with ellipsis  
blank line is for expected answer  
```

#####Expecting Exceptions
