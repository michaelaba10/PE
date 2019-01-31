'''
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


from tictoc import tic,toc

'''
20=2^2*5
19=19
18=2*3^2
17=17
16=2^4
15=3*5
14=2*7
13=13
12=2^2*3
11=11
10 = 2*5
9 = 3^2
8 = 2^3
7 = 7
6 = 3*2
5 = 5
4 = 2^2
3 = 3
2 = 2
1 = 1
'''


# We multiply all the primes less than 20, with hightest power presented in prime 
# factorization for numbers in 1-20, so we  are sure it is divisible by all of them

tic()
number = (2**4)*(3**2)*(5)*(7)*(11)*(13)*(17)*(19)
print(number)
toc()