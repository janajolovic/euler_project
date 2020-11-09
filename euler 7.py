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


counter = 0
#we go through the for loop
#we begin with 2 because 1 is not prime
for i in range(2,100000000):
    #we call the function and if number is prime 
    #then counter increases by 1
    if prime(i): 
       counter += 1
       #if counter is equal to 10001 then we print 10001st prime number
       if counter == 10001:
           print(i)
           break

