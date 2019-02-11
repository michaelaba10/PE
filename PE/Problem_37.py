'''
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, and remain prime at each stage: 
    3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


from eulerlib import prime_numbers,primes
from tictoc import tic,toc

def truncable_left(number):
    string_number = str(number)
    digits_number = len(string_number)
    number_truncates = 0
    truncable_left = True
    while (prime_numbers.is_prime(int(string_number))) and int(string_number)>=10:
        number_truncates = number_truncates +1
        string_number = string_number[1:]
    if (len(string_number)<10) and (prime_numbers.is_prime(int(string_number))):
        number_truncates = number_truncates + 1
    if (number_truncates < digits_number) or (digits_number == 1) :
        truncable_left = False
    return truncable_left

def truncable_right(number):
    string_number = str(number)
    digits_number = len(string_number)
    number_truncates = 0
    truncable_right = True
    while (prime_numbers.is_prime(int(string_number))) and int(string_number)>=10:
        number_truncates = number_truncates +1
        string_number = string_number[:-1]
    if (len(string_number)<10) and (prime_numbers.is_prime(int(string_number))):
        number_truncates = number_truncates + 1
    if (number_truncates < digits_number) or (digits_number == 1) :
        truncable_right = False
    return truncable_right

# 9 seconds search, not bad.
tic()
primes = primes(1000000)
truncable_primes = []
for i in primes:
    if truncable_right(i) and truncable_left(i):
        truncable_primes.append(i)
print(( 'The sum of the primes is: ' + str(sum(truncable_primes)),truncable_primes))
toc()




