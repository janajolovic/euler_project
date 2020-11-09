sum_num = 0
#we go through the for loop from to some large number
for i in range(2,1000000000000):
    number = 0
    #we go throuh the second for loop
    #j takes value of every digit in i
    for j in str(i):
        #number take value of the sum of fifth powers of digits
        number += int(j)**5
    #if i is equal to number then we add it to sum_num
    if i == number:
        sum_num += number
        print(i)
    #we print the sum of numbers that can be written as the sum of fifth powers of their digits
        print("sum is",sum_num)
