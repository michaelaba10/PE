#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_until(multiple,until):
    if until % multiple == 0:
        superior_limit = until/multiple-1
    else:
        superior_limit = until/multiple
    result = [i*multiple for i in range(1,superior_limit+1)]
    return result


## We add the multiples of 3 and 5 belowm 1000, but the multiples of 15 are added up twice.
sum(multiples_until(3,1000)) + sum(multiples_until(5,1000))-sum(multiples_until(15,1000))



