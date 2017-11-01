# ex31:  Making Decisions			 (file by mk.py)

'''


'''

print "door #1 or #2??"

door = raw_input('<  ')

if door == '1':
	print "bear #3 or #4"
	bear = raw_input('<  ')
	if bear == '3':
	 	print "bear 3"
	elif bear == '4':
		print "bear #4"
	else:
		print "neither bear 3 nor bear 4"
elif door == '2':
	print " fate 1 - 3"
	fate = raw_input('<  ')
	if fate == '1':
		print 'fate 1'
	elif fate =='2':
		print 'fate 2'
	elif fate =='3':
		print 'fate 3'
	else:
		print 'no fate at all'
else:
	print "that's neither door, g"
	
	

	