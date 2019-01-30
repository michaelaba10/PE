from eulerlib import numtheory

greater_one_million = 0
for n in range(23,100+1):
    for r in range(1,n):
        if (numtheory.nCr(n, r)>1000000):
        greater_one_million = greater_one_million+1
print(greater_one_million)
