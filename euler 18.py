
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#we split triangle on "\n" and now each row is one element (list)
line = []
line = triangle.split('\n')

#we create an empty list 
triangle_list = []
#we go through the for loop
for i in range(len(line)):
    #and we split line on " " and now each number is one element 
    line_list = line[i].split(" ")
    #then we append it to triangle_list
    triangle_list.append(line_list)

#we go through two for loops
for i in range(len(triangle_list)):
    for j in range(len(triangle_list[i])):
        #and turn each number into int because these numbers are string
        triangle_list[i][j] = int(triangle_list[i][j])
 
#we go through two for loops, but we go from buttom to top 
for i in range(len(triangle_list)-1,-1,-1):
    for j in range(i):
        #we calculate which one of adjacent number is greater
        #then we add that number to number above him(the number with index[i-1][j])
        triangle_list[i-1][j]+=max(triangle_list[i][j],triangle_list[i][j+1])
#we print the number with index (0,0) 
#because it is in the same time the maximum total of of the triangle
print(triangle_list[0][0])