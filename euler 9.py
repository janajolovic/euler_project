#we go through 3 for loop, for each number one loop
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            #these are the conditions
            if a+b+c == 1000 and a**2+b**2==c**2 and a < b < c:
                #we print the pythagorean triplet
                print(a, b, c)
                break