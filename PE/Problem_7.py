'''
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

from tictoc import tic,toc

def sieve_Eratosthenes(n):

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
print(sieve_Eratosthenes(1500000)[10000])
toc()
 

'''
This is not optimal, becuase I am generating a lot of primes, and choosing number 10001,
still fast enough 1/3 of sec
'''