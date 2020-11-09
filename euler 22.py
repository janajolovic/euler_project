score_sum = 0
#we open the file that we can read
file_names = open('p022_names.txt', 'r')
#we split it on "," 
names = file_names.read().split(",")
#we removed the first and last sign (double " ")
for i in range(len(names)):
    names[i] = names[i][1:-1]
#we sort all names into alphabetical order
names.sort()
for i in range(len(names)):
    sum_letters = []
    #names[i] is one name
    for j in names[i]:
        #we found value for each name
        sum_letters.append(ord(j)-64)
    #name score is sum of value of name multiply by its alphabetical position in the list
    #(i+1) because we start with 0, but we need to start with 1
    score_sum += (sum(sum_letters)) * (i+1)
#we print the total of all the name scores in the file
print(score_sum)



