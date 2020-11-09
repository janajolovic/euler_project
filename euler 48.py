sum_num = 0
#we go through the for loop from 1 to 1001
for i in range(1,1001):
    #sum_num increases each time by i**i
    sum_num += i**i
#we turn sum_num into string and then print last 10 digits
print(str(sum_num)[-10:])
