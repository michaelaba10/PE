"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the
right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""



'''
 (m+n)Cn=(m+n)Cm, and this counts the number of ways to choose the horizontal and vertical
 moves
'''

from tictoc import tic,toc


def factorial(n):
	factorial=1
	for x in range(1,n+1):
		factorial*=x
	return factorial

def number_paths_grid(m,n):
	return factorial(m+n)/(factorial(m)*factorial(n))

tic()	
print(number_paths_grid(20,20))
toc()