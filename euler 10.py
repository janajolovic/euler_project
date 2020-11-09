import math

#we define the function that will check whether the number is prime or not
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


sum_num = 0
#we go through the for loop
for i in range(1,2000000):
    #we call the function
    #and if number is prime
    if prime(i): 
        #counter for sum of numbers will increases by than prime number(i)
        sum_num += i
#we print the sum of numbers
print(sum_num)
       