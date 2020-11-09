#sum of the squares
sum_sq = 0
#square of the sum
sq_sum = 0
#we go through the for loop to 101
for i in range(1,101):
    #we add i**2 tosum of the squares
    sum_sq += i**2
    #we find sum of all numbers (we add i to sq_sum)
    sq_sum += i
    #then we calculate the final square sum
    sq_sum_final = sq_sum**2
#we print the difference between the sum of the squares and the square of the sum
print(sq_sum_final-sum_sq)