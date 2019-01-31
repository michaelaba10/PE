'''
Sum square difference

Find the difference between the sum of the squares of the first one
 hundred natural numbers and the square of the sum.
'''


from tictoc import tic,toc
def sumSquares(n):
	return n*(n+1)*(2*n+1)*(1.0/6)

def squareOfSum(n):
	x= (n)*(n+1)*(0.5)
	return x**2

tic()
result = sumSquares(100)-squareOfSum(100)
print(result)
toc()


