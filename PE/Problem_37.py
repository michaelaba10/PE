from eulerlib import prime_numbers,primes

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

primes = primes(1000000)
truncable_primes = []
for i in primes:
    if truncable_right(i) and truncable_left(i):
        truncable_primes.append(i)
print len(truncable_primes)





