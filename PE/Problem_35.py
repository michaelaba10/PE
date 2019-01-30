from eulerlib import prime_numbers,primes

def isCircular(number):
    number_string = str(number)
    number_digits = len(number_string)
    number_circular_rotations = 0
    while(prime_numbers.is_prime(int(number_string))):
        number_circular_rotations = number_circular_rotations+1
        first_digit = number_string[0]
        number_string = number_string[1:] + first_digit
        if number_circular_rotations == number_digits:
            break
    if number_circular_rotations == number_digits:
        return True
    else:
        return False


def circular_primes_less_than(number):
    primes_to_check = primes(number)
    number_circular = 0
    for i in primes_to_check:
        if isCircular(i):
            number_circular = number_circular+1
    return number_circular
