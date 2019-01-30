#Summation of primes
#Problem 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

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

def sumaLista(l):
	x=0
	for i in l:
		x+=i
	return x

print sumaLista((cribaErastotenesII(2000000)))