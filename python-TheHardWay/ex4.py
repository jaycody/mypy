# ex4:  Variables and Names


'''types of python operators:
arithmatic operator:: + - / * % ** //{floor division}
comparison operator:: == != <> < > <= >=
assignment operators:: = += -= *= **= /= //= %=
logical operator:: and or not
bitwise operator:: works on bits and performs bit operations & | ^ ~ << >> 
membership operator:: in  not in   eg.  x in y  x not in y
identity operator:: is   is not
'''

# declares and sets the variables
# variable, assignment operator, comment
cars = 100 # assignment operator
# variable, assignment operator, float value
space_in_a_car = 4.0
# variable, assignment operator, int value
drivers = 30
# variable, assignment operator, int value
passengers = 90

# calculates 
#variable, assignment operator, variable, arithmatic operator, variable
cars_not_driven = cars - drivers
cars_driven  = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#prints  the readable and injects the variables 
#print command, string, comma, variable(int), comma, string
print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We need to put about", average_passengers_per_car, "in each car."

 