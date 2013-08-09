# Code to verify the number of single-bit z-numbers

n = 16

two_n_3 = (2*n)+3

print "two_n_3= " + str(two_n_3)
print "two_n_3^2= " + str(two_n_3**2)

single_count = 0

total_count = 0

range_set = range(1,n+2)
range_set.extend(range_set)
range_set.append(0)

print "len(range_set)= " + str(len(range_set))

print "range_set= " + str(range_set)

for i in range_set:
	i_count = 0
	for j in range_set:
		#print "i= " + str(i)
		#print "j= " + str(j)
		if (i+j < n):
			#print "i+j= " + str(i+j)
			single_count += 1
			i_count += 1
		total_count += 1
	print "count for i=" + str(i) + ": " + str(i_count)

print "single_count= " + str(single_count)
print "total_count= " + str(total_count)

assert(two_n_3**2 == (4*(n**2))+(12*n)+9)
assert(two_n_3**2 == total_count)

#print "4n^2 + 12n + 9= " + str((4*(n**2))+(12*n)+9)
print "4n^2 - 4n + 1= " + str((4*(n**2))-(4*n)+1)
print "2n^2 - 2n + 1= " + str((2*(n**2))-(2*n)+1)

print "16n + 8= " + str((16*n)+8)

print "two_n_3^2 - single_count= " + str((two_n_3**2) - single_count)