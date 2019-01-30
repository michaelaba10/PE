from eulerlib import prime_numbers,primes

def consecutive_primes_forward_starting_zero(a,b):
    iPrimes = 0
    n = 1
    while (prime_numbers.is_prime(n**2+a*n+b)):
        iPrimes = iPrimes +1
        n = n+1
    return iPrimes+1

posibles_b = primes(1000)
tuplas = []
consecutivos = []
for a in range(-999,1000,1):
    for b in posibles_b:
        consecutivos0 = consecutive_primes_forward_starting_zero(a,b)
        consecutivos.append(consecutivos0)
        tuplas.append([a,b])
        consecutivos0 = consecutive_primes_backwards_starting_zero(a, b)
        consecutivos.append(consecutivos0)
        tuplas.append([a, b])


indice = consecutivos.index(max(consecutivos))
tupla_final = tuplas[indice]
consecutivos_final = consecutivos[indice]
print(tupla_final, consecutivos_final)


