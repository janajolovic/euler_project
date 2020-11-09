#we open the file that we can read
w_file = open('p042_words.txt', 'r')
#we split it on ","
word_list = w_file.read().split(",")
#we removed the first and last sign (double " ")
for i in range(len(word_list)):
    word_list[i] = word_list[i][1:-1]

#we create an empty list for triangle numbers
triangle_num = []
#we go through the for loop and append numbers to list
for i in range(1,100):
    triangle_num.append(int((i**2+i)/2))

#this is counter for triangle numbers
triangle_words = 0
#we go through two for loops
for i in word_list:
    word_sum = 0
    for j in i:
        #we calculate the value for each letter in word
        word_sum+=(ord(j)-64)
    #if word_sum is in list of triaangle numbers
    if word_sum in triangle_num:
        #then counter (triangle_words) increases by 1
        triangle_words+=1
#we print the triangle_words
print(triangle_words)

