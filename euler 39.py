
max_counter = 0
#we go through the for loop from 1 to 1001
for i in range(1,1001):
    counter = 0
    #now we go through the 3 for loops (for each side one loop)
    for a in range(1,i-2):
        for b in range(1,i-a-1):
            for c in range(1,i-a-b+1):
                #first condition is that sum of 3 side must be equal to perimeter(i)
                if a+b+c == i:
                    #second condition is that sum of two side must be greater than third side
                    #and a<b<c
                    if a+b>c and a<b<c:
                        #the last condition is application of the pythagorean theorem
                        if a**2 + b**2 == c**2:
                            #if all conditions are met then we print perimeter and sides of triangle
                            print(i,a,b,c)
                            #counter increases each time by 1
                            counter += 1
    #if counter is greater than max_counter
    if max_counter < counter:
        #max_counter take value of counter
        max_counter = counter
#we print perimeter and max_counter
print(i,max_counter)
    