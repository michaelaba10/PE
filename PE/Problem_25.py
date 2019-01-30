


def primerFIbconNdigitos(n):
	x=[1,1]
	i=2
	while len(str(x[-1]))<n:
		x.append(x[-1]+x[-2])
		i+=1
	print (x[-1],i)
primerFIbconNdigitos(1000)