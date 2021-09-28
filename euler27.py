import math

def isPrime(num):
    prime = True
    if num < 2: 
        return False
    if num == 2: 
        return True
    for factor in range(3,int(math.sqrt(num)),2):
        if num % factor == 0: 
            prime = False
    return prime

def testEquation(a,b):
    n = 0
    while True:
        test = n**2 + a*n + b
        if isPrime(test): 
            n += 1
        else: break
    return n


c1 = 0
a1 = 0
b1 = 0
for a in range (-1000,1001):
    for b in range (-1000,1001):
        c = testEquation(a,b)
        if c > c1: 
            c1, a1, b1 = c, a, b

print (a1*b1)
