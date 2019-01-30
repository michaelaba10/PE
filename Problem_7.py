#10001st prime
#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

 

def cribaErastotenesII(n):

    primos = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
        if (primos[p] == True):
            for i in range(p * 2, n+1, p):
                primos[i] = False
        p+=1
    for num in range(n+1):
        if primos[num]:
            primos[num]=num

    return sorted(list(set(primos)))[2:]


print cribaErastotenesII(1500000)[10000]
 

