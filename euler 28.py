#num is also the first terms of spiral
num = 1
x = 2
final_sum = 0
for i in range(500):
    #for each for number in one circle (four numbers on diagonals), the numbers increases by the same numbers (x)
    #in first circle it is 3,5,7,9, increases by 2
    #in second it is 13,17,21,25, increases by 4...
    for i in range (1,5):
        num += x
        final_sum += num
    x += 2
#we print the final sum
print(final_sum+1)