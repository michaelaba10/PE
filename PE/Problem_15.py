## (m+n)Cn=(m+n)Cm, y eso me cuenta la cantidad de maneras de distribuir mis bajas o movimiento horizontales

def factorial(n):
	factorial=1
	for x in xrange(1,n+1):
		factorial*=x
	return factorial

def cantidadCamniosTableroMxN(m,n):
	return factorial(m+n)/(factorial(m)*factorial(n))

	
print cantidadCamniosTableroMxN(20,20)