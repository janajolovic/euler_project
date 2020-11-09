#we create counter for sum 
sum_num = 0
#we go through the for loop to 1000
for i in range(1,1000):
    #if number is multiples of 3 or 5
    if i % 3 == 0 or i % 5 == 0:
        #then sum_num increases by 1
        sum_num += i
        #we print the sum of all the multiples of 3 or 5 below 1000
print(sum_num)