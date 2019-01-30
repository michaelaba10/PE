def cumpleProbiedad(n):
	y=0
	x=[int(d) for d in str(n)]
	for i in x:
		y+= i**5
	if n==y:
		return True
	else:
		return False
#d1....dn=d1!^5+...+dn^5=> 10^(n-1)<=(9^5)n, y de aqui el numero no puede tener mas de 6 digitos
def TodosQueCumplenEnRango():
	l=[]
	for x in xrange(2,999999):
		if cumpleProbiedad(x):
			l.append(x)
	print sum(l)
TodosQueCumplenEnRango()
