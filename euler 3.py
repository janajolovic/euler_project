import math

#we define function that will check whether the number is prime or not
def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisors = math.floor(math.sqrt(n))
    for j in range(3, 1+max_divisors, 2):
        if n % j == 0:
            return False
    return True


number=600851475143

#we go through for loop from 2 to number+1
for i in range(2,number+1):
    #if number can be devided with i, and that quotient is prime 
    if number % i == 0 and prime(i):
        #then we print i
        #the last number that is printed is is the largest prime factor of the number
        print(i)

