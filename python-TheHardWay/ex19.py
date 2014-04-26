# ex19:  Functions and Variables

'''


'''


def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "You have %d + %d total cheese crackers" % (cheese_count, boxes_of_crackers)
	print "Which is this many:  %d" % (cheese_count + boxes_of_crackers)
	print "word. \n"



print "Give the function numbers directly:"
cheese_and_crackers(20, 30)


print "Or pass variables"
amount_of_cheese = 1000000
amount_of_crackers = 500000000

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even pass an expression"
cheese_and_crackers(2200+5593, 11*35)


print "And combine the two"
cheese_and_crackers(amount_of_crackers+amount_of_cheese*234, 1)

