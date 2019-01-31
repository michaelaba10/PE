'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143
'''

from eulerlib import primes
from tictoc import tic,toc


tic()
number = 600851475143;
bound_divisor = (number)**(0.5)+1

primes_less_than_number = primes(bound_divisor+1)

divisors = []
for i in primes_less_than_number:
    if (number % i ==0): 
        divisors.append(i)
        number = number/i
        if (number == 1):
            break
if len(divisors) == 0:
    divisors.append(number)
print(max(divisors))
toc()