#Sum square difference
#Problem 6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumSquares(n):
	return n*(n+1)*(2*n+1)*(1.0/6)

def squareOfSum(n):
	x= (n)*(n+1)*(0.5)
	return x**2
print sumSquares(100)-squareOfSum(100)


