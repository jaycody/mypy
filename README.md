###python gongfu  ==>  'work + time/effort'

- Kung fu/Kungfu or Gung fu/Gongfu (Listeni/ˌkʌŋˈfuː/ or /ˌkʊŋˈfuː/; 功夫, Pinyin: gōngfu) is a Chinese term referring to any study, learning, or practice that **requires patience, energy, and time to complete.**  

- In its original meaning, kung fu can refer to any **skill achieved through hard work and practice,** not necessarily martial arts. The Chinese literal equivalent of "Chinese martial art" would be 中國武術 zhōngguó wǔshù.

- In Chinese, Gōngfu (功夫) is a compound of two words, combining 功 (gōng) meaning "work", "achievement", or "merit", and 夫 (fū) which is alternately treated as being a word for "man" or as a particle or nominal suffix with diverse meanings (the same character is used to write both). A literal rendering of the first interpretation would be "achievement of man", while the second is often described as "work and time/effort". 

- the connotation is that of an accomplishment **arrived at by great effort of time and energy.**

- Originally, to practice kung fu did not just mean to practice Chinese martial arts. Instead, it referred to the **process of one's training - the strengthening of the body and the mind, the learning and the perfection of one's skills** - rather than to what was being trained. 

- It refers to excellence achieved through **long practice in any endeavor.**  This meaning can be traced to classical writings, especially those of Neo-Confucianism, which emphasize the importance of effort in education.

- In the colloquial, one can say that a person's kung fu is good in cooking, or that someone has kung fu in calligraphy; saying that a person possesses kung fu in an area implies skill in that area, which they have worked hard to develop. 

- Someone with "bad kung fu" simply has not put enough time and effort into training, or seems to lack the motivation to do so

export PS1='\[\033[0;34m\][\[\033[0;31m\]\H \[\033[1;35m\]\u \[\033[0;32m\]\w\[\033[0;34m\]]\[\033[0m\] '


______________________

###py notes:

####Docstring Conventions:
- from [PEP 257 Docstring Conventions]
- "A universal convention supplies all of maintainability, clarity, consistency, and a foundation for good programming habits too..."
- if a method, function, or class begins with a string literal, it is stored in the object's __doc__ attribute
- a phrase ending in a period that PRESCRIBES the function or method's effect AS A COMMAND
	- eg """Do FOO!  Return Bar!"""
	- write as a PRESCRIPTION, not as a DESCRIPTION!
	- eg not, """Returns a BAR"""  but """Return Bar"""
- multi-line docstrings are one-line summaries followed by blank line then multi-line descriptions
	- eg 
	```python
	"""Multi-Line docstring starts with one-line summary

	Followed by a blank line, then a more general description
	requiring as many lines as required
	"""
	```
	- all lines of the multi-line docstring are indented to same indent as the first quotes

_________________

####the help utility ==> help()
- to start the help utility:
	- type help() in the interpreter
- enter the name of any module 
- **to call help on a function from the interpreter**
>
```
help(moduleFoo.functionFoo)
```

_________________

####MISC
- **encapsulation**:  wrapping a piece of code in a function
- **generalization**:  adding a parameter to a function
- **keyword arguments**:  for clarity, include name of parameters in argument list when calling function
	- ex   
	```polygon(t=bob ,length=50 ,n=5)```
- **interface of a function**:  summary of how the function is used.  
	- what are the parameters?, what is the return value?, etc.
	- an **interface** is like a contract between a function and a caller.
		- The CALLER agrees to provide certain parameters (PRECONDITIONS)
		- The FUNCTION agrees to do certain work  (POSTCONDITIONS)
- **BOOLEANS**
	- Do NOT compare boolean values to True or False using ==
```
Yes:    if greeting:
No:     if greeting == True:
Worse:  if greeting is True:
```

	- For sequences (strings, lists, tuples) use the fact that empty sequences are false  

```
Yes:    if not seq:
        if seq:
No:     if len(seq):
        if not len(seq):
```
__________________

####Generic Development Plan
1. Start by writing a small program with no function definitions
2. Once the program is working, **encapsulate** it in a function and give it a name
3. **Generalize** the function by giving it appropriate parameters
4. Repeat steps 1-3 until you have a set of working functions
5. Refactor

___________________

####Running a script as SCRIPT or as MODULE ==> a self-check
- the following tests whether the code is running on it's own or if it's being imported.  
- if running as a script, then the code in the conditional (the test code) will run.
- if imported, then the test script remains dormant  

>
```
if __name__ == '__main__':
	"""test whether code is running as script or as import.
	Remains silent if being imported.  Instanciates the following code if running as script
	"""
	world = NasWorld()
	nas = rapper()
	nas.delay = 0.0001
	numSided = 5
	wait_for_user()
```

_______________________

####Adding Command Line Arguments with argv
- ex

```
# gets argv from command line  
import sys  
# helps loops through argvs  
import fileinput  
 
def getDimension(argvIndex):  
	'''takes commnad line arg for number of sides of polygon.  
	When no input present, uses default num of sides  
	'''  
  
	if argvIndex+1 > len(sys.argv):  
		return 25  
		
	else:  
		dimension = int(sys.argv[argvIndex])  
		#print dimension  
		return dimension  
  
d = getDimension(1)  
print d  
print "variable type = ", type(d)  

#check the range  
for i in range(len(sys.argv)):
	print sys.argv[i]
lengthArgsArray = len(sys.argv)
print lengthArgsArray

```





[PEP 257 Docstring Conventions]:http://legacy.python.org/dev/peps/pep-0257/
