'''
Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''

from tictoc import tic,toc

def cribaErastotenesII(n):
    primes = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
        if (primes[p] == True):
            for i in range(p * 2, n+1, p):
                primes[i] = False
        p+=1
    for num in range(n+1):
        if primes[num]:
            primes[num]=num

    return sorted(list(set(primes)))[2:]

tic()
print(sum((cribaErastotenesII(2000000))))
toc()