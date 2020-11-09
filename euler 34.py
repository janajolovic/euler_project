import math
#we start with 3, because 1 and 2 aren't included
i = 3
#sum_num is sum of all numbers which are equal to the sum of the factorial of their digits
sum_num = 0
while True:
    f_sum = 0
    #we go through the for loop
    #j takes value of each digit in i
    for j in str(i):
        #we add factorial of j to sum of factorial (f_sum) 
        f_sum += math.factorial(int(j))
    #if f_sum is equal to i then we print f_sum
    #we add f_sum to sum_num
    if f_sum == i:
        print(f_sum)
        sum_num += f_sum
        print("sum is:",sum_num)
    #each time i increases by 1
    i += 1 


    