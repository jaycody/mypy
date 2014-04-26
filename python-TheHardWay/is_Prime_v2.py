def is_prime(x):
	if x < 1:
		return False
	if x == 1 or 2:
		return True
	
	for n in range (1, x):
		if x % n == 0:
			print "modulo = 0 for %d" % x
	else:
		return True

'''
def is_prime(x):
	if x == 1 or 2:
		return True
	if x < 1:
    	return False
    for num in range (1,x):
        if x % num == 0:
            return False
    else:
        return True
'''            

checkForPrime = 12
print "\n\t---> You entered:  ", checkForPrime
ans = is_prime(checkForPrime)
print "\n\t---> %d is PRIME: %r "% (checkForPrime, ans), "\n"