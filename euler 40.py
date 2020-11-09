fraction = '0.'
adder = 1
#we go through the while loop
while True:
    #and if lenght of fraction is equal or greater than 1000002
    if len(fraction) >= 1000002:
        #then we print first, tenth, hundredth... decimal
        print("1: ", fraction[2])
        print("10: ", fraction[11])
        print("100: ", fraction[101])
        print("1000: ", fraction[1001])
        print("10000: ", fraction[10001])
        print("100000: ", fraction[100001])
        print("1000000: ", fraction[1000001])
        break
    #we turn adder into string and add it to fraction
    fraction += str(adder)
    #adder increses each time by 1
    adder += 1
