# Code to verify the number of single-bit z-numbers

n = 10000000
level = 0

while (n > 2):
	triplets = n / 3
	leftovers = n % 3
	n = (2*triplets) + leftovers
	level += 1
	print "n=" + str(n)
	print "level=" + str(level)
