#we create two sets for pentagonal and hexagonal numbers
p = set()
h = set()
i = 1
#we go through the while loop
while True:
    #we add pentagonal numbers to pentagonal set
    p.add(i*(3*i-1)//2)
    #we add hexagonal numbers to hexagonal set
    h.add(i*(2*i-1))
    #we calculate triangle number
    t = i*(i+1)//2
    #if that triangle number is in set of pentagonal and hexagonal numbers
    if t in p and t in h and t>40755:
        #then we print that triangle number
        print(t)
        #and break
        break
    #i increases by 1 each time
    i += 1









