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

#we define the function 
#this function will check whether number which we remove digits prime (from left to right)
def LeftToRight(num):
    for i in range(len(str(num))):
        #if number is not prime function will return False
        if not prime(int(str(num)[i:])):
            return False
    #else it will return True
    return True
#this function will check whether number which we remove digits prime (from right to left)
def RightToLeft(num):
    for i in range(len(str(num)),0,-1):
        #if number is not prime function will return False
        if not prime(int(str(num)[:i])):
            return False
    #else it will return True
    return True


counter = 0
#we start from 8 because 2, 3, 5, and 7 are not considered to be truncatable primes
i = 8
sum_num = 0
#we go through the while loop
while True:
    #and if both function LeftToRight and RightToLeft return value True
    if LeftToRight(i) and RightToLeft(i):
        #then we print i
        print(i)
        #counter increses by 1
        counter += 1
        #and sum of numbers increases by i
        sum_num += i
    #if counter is equal or greater than 11
    if counter >= 11:
        #then we break
        break
    #i increases each time by 1
    i += 1
#we print the sum_num
print(sum_num)
