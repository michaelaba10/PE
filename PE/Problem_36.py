from numpy import binary_repr

binary_repr
def sum_number_palindromes_both_repr_less_than(number):
    number_good_cases = []
    for i in range(0,number+1):
        binary = str(binary_repr(i))
        number = str(i)
        if (number == number[::-1]) and(binary == binary[::-1]):
            number_good_cases.append(i)
    return sum(number_good_cases)
sum_number_palindromes_both_repr_less_than(10)
