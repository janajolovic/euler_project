#we turn number into string
n = str(2**1000)
#we create variable (counter)
sum_numbers = 0
#with for loop we go through the number n
for i in n:
    #end we add the int values of every digit in number n to sum_numbers
    sum_numbers += int(i)
print(sum_numbers)
