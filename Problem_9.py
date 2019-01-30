#Special Pythagorean triplet
#Problem 9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def sumanN():
	lista=[]
	for i in xrange(1,1000):
		for j in xrange(1,1000-i) :
			if 1000-i-j!=j and i**2==(1000-i-j)**2+j**2:
				lista.append((j,1000-i-j,i))
	print lista
sumanN()



