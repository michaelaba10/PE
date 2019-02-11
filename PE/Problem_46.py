'''
It was proposed by Christian Goldbach that every odd composite number can be
 written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from math import floor,sqrt
from tictoc import tic,toc


def num_divisors(n):
    if n % 2 == 0:
        n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


tic()


n = 6000
list_numbers = list(range(1,n,2))
list_numbers = [x for x in list_numbers if num_divisors(x)>2]


for number in range(1,n,2):
    if num_divisors(number)>2:  
        for  power in range(1,floor(sqrt(number/2))+1):
            even_number = number - 2*(power**2)
            if num_divisors(even_number) == 2:
                list_numbers.remove(number)
                break

print(list_numbers)
toc()
