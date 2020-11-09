factorial = 1
num = 0
#we go through the for loop to calculate the factorial (100!)
for i in range(1,101):
    factorial *= i
print(factorial)
#we turn it into string
factorial = str(factorial)
#now we create an empty list, where we will every digit of factorial
f_list = []
for i in factorial:
    f_list.append(i)
#we go though the for loop and add int values of every digit to counter num
for i in f_list:
    num += int(i)
#now we print the sum of digits
print(num)