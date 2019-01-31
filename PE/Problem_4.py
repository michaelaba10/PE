'''
Largest palindrome product
Find the largest palindrome made from the product of two 3-digit numbers.
'''

from tictoc import tic,toc

def palindromesProduct3DigitsNumbers():
	palindrome = []
	for i in range(100,1000):
		for j in range(100,1000):
			if str(i*j)==str(i*j)[::-1]:
				palindrome.append(i*j)
	return palindrome

tic()
print(max(palindromesProduct3DigitsNumbers()))
toc()