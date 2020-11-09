#we create an empty list for results
result_list = []
#we go through two for loop (for each number one loop)
for a in range(2,101):
    for b in range(2,101):
        #and we append a**b toresult_list
        result_list.append(a**b)
#now we sort result_list (the numbers from smallest to largest)
result_list.sort()
#we create dictionary (keys are the numbers from result_list) and then turn it back into list
#because in dictionary can not be two same keys
result_list = list(dict.fromkeys(result_list))
#we print the lenght of result_list
print(len(result_list))