from eulerlib import Divisors


def cantidadDivisores(n):
	mydiv = Divisors(n)
	div84 = mydiv.divisors(n)
	cantidadDiv = len(div84)
	return cantidadDiv

def firstTriagularNum():
	i=1
	xi= int(i*(i+1)*(1.0/2))
	while cantidadDivisores(xi)<500:
		i+=1
		xi= int(i*(i+1)*(1.0/2))
		print (i,xi,cantidadDivisores(xi))
firstTriagularNum()


