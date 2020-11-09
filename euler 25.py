#a and b are the first terms of sequence
a = 1
b = 1
c = 0
#the number in sequence is the sum of two previous numbers
for i in range(9999999999):
    c = b
    b = b + a
    a = c
    #if number of digits is 1000 (or more), then we print that number and index of that number
    if len(str(b)) >= 1000:
        print(b)
        print(i+3)
        break