'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
 Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


from tictoc import tic,toc


    
def collatz(n):
    if n%2==0:
        n = n/2
    else:
        n = 3*n+1
    return n
   
def numberSteps(n):
    i=0
    while n!=1:
        n = collatz(n)
        i+=1         
    return i

    

number_longest_chain = 0
size_longest_chain = 0


## 33s answer, not bad, 152 steps taken
tic()
for i in range(2,1000001):
    number_steps = numberSteps(i)
    if number_steps > size_longest_chain:
        size_longest_chain = number_steps
        number_longest_chain = i
print((number_longest_chain, number_steps))
toc()
        
        




