#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143

from eulerlib import primes

numero = 600851475143;
cota_aproximacion_divisores = (numero)**(0.5)+1

primos_menores = primes(cota_aproximacion_divisores+1)

divisores = []
for i in primos_menores:
    while (numero % i ==0):
        divisores.append(i)
        numero = numero/i
        if (numero==1):
            break
if len(divisores) == 0:
    divisores.append(numero)
print(max(divisores))