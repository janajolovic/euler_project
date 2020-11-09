counter = 0
#we go through two for loops
#first is for power
for i in range(1,50):
    #and second is for number
    for j in range(1,50):
        #we turn j**i into string
        #and if lenght of that string is equal to i (power)
        if len(str(j**i)) == i:
            #then counter increases by 1
            counter += 1
#we print counter
print(counter)