
n = n2 = 1000000
counter = 1
max_counter = 0
#we just need variable k to break the while loop
k = 1
n1 = 1
while k == 1:
    counter = 0
    #we go through the for loop and if number is odd then we multiple it with 3 and add 1
    #counter increases by 1
    for i in range(1, int(n)):
        if n % 2 != 0:
            n = 3*n + 1
            counter += 1
            #if number is even then we devide it with 2 and counter increses by 1
        if n % 2 == 0:
            n = int(n/2)
            counter += 1
        #when the n reaches 1 the chain is interrupted
        if n == 1:
            break
    #if counter is greater than max counter
    #then max counter take the value of counter
    #and variable n3 take value of n2
    #n3 is the starting number that we will print in the end
    if counter > max_counter:
        n3 = n2
        max_counter = counter
    #each time n take value of n2-1 so we can check for all numbers below 1000000 (n) 
    n = n2 - 1
    #and each time n2 decreases by 1
    n2 -= 1
    #when n reaches 1 then we break the while loop
    if n == 1:
        k = 0

#we print the starting number and the chain with the most terms
print(n3, max_counter)
    
