# factorial function
def factorial(x):
   
   for n in range(x,0,-1):
        if n < 2:
           return 1
        else:
            return n * (factorial(n-1))

   
 
 
 
x = 6
factorialOfNum = factorial(x)
print factorialOfNum