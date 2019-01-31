'''
Special Pythagorean triplet
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

from tictoc import tic,toc



def triplets():
	list0 = []
	for i in range(1,1000):
		for j in range(1,1000-i) :
			if i**2==(1000-i-j)**2+j**2:
				list0.append((j,1000-i-j,i))
	return list0[0] # Unique until permutations of triplets, so we take first.
tic()   
result = triplets()
print(result)
toc()



