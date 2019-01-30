def collatz(n):
	if n%2==0:
		return n/2
	else:
		return 3*n+1

def numberSteps(n):
	i=1
	x=n
	while n!=1:
		n=collatz(n)
		i+=1
	return i-1

def longestChain(i,n):
	x=0
	y=0
	while i<n:
		m= numberSteps(i)
		if x<m:
			x=numberSteps(i)
			y=i
		i+=1
	print(y,x-1)

longestChain(1,1000000)

