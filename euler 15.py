from math import factorial

#we define function which will return the binomial coefficient of n,k
def Routes(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

#Number of lattice paths from (0,0) to (n,k) is given by binomial coefficient C(a+b,a)
#we print the number of routes through a 20×20 grid
print(int(Routes(20+20,20)))