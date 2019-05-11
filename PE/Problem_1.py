'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

from math import floor
from tictoc import tic,toc

def sum_multiples_until(multiple,limit):
    # This function sum all the multiples of a number that are strictly less than certain limit.
    if limit % multiple == 0:
        superior_limit = floor(limit/multiple-1)
    else:
        superior_limit = floor(limit/multiple) 
        
    result = [i*multiple for i in range(1,superior_limit+1)]
    
    return sum(result)


## We add the multiples of 3 and 5 belowm 1000, but the multiples of 15 are added up twice.
tic()
value = sum_multiples_until(3,1000) + sum_multiples_until(5,1000) - sum_multiples_until(15,1000)
toc()
print(value)
