#Largest palindrome product
#Problem 4
#Find the largest palindrome made from the product of two 3-digit numbers.

def palindromosProductoNumeros3Digitos():
	palindrome = []
	for i in range(100,1000):
		for j in range(100,1000):
			if str(i*j)==str(i*j)[::-1]:
				palindrome.append(i*j)
	return palindrome

print max(palindromosProductoNumeros3Digitos())