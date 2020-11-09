
final_sum = 0
#we go through the for loop
for x in range(1,10001):
    #we create two empty list, where we will add divisors
    divisors = []
    divisors1 = []
    #if first number x can devide with i, then we append i to list
    for i in range(1,x):
        if x % i == 0:
            divisors.append(i)
    #the second number y take the value of sum of divisors of first number (x)
    y = sum(divisors)
    #if y can devide with i, then we append i to list divisors1
    for i in range(1,y):
        if y % i == 0:
            divisors1.append(i)
    #these are some conditions to calculate amicable numbers
    if sum(divisors1) == x and sum(divisors) == y and x!=y and x<y:
        print(x)
        print(y)
        final_sum += (x+y)
    #x increases every time
    x+=1
#we print the final sum of all the amicable numbers under 10000
print(final_sum)

