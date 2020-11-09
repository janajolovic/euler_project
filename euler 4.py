max_number = 0
#we go through two for loops for each of two 3-digit numbers
for i in range(100,1000):
    for j in range(100,1000):
        #variable number takes value of  product of those numbers
        number = i*j
        #if that number is paindrome
        if str(number) == str(number)[::-1]:
            #and if max_number is less than number
            if max_number < number:
                #then max_counter takes value of number
                max_number = number
#we print the largest palindrome made from the product of two 3-digit numbers
print(max_number)
            