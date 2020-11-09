#the first two terms will be a(1) and b(1)
a = 1
b = 1
sum_num = 0
#we through the while loop as long as b is less then 4000000 
while b<4000000:
    #c(helpful variable) takes values of b
    c = b
    #b takes value of sum of a and c
    #b will be the next term of sequence
    b = a + c
    #a takes value of c
    a = c
    #if b is even number
    if b % 2 == 0:
        #then sum_num increases by b
        sum_num += b
#we print the sum of the even-valued terms.
print(sum_num)