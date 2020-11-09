#counter for couting number of possibilities
counter = 1 #(1 because of 200p is one way)
#we go through the for loop for each coins
for a in range(3):  #100
		for b in range(int(1+(200-100*a)/50)):  #50
				for c in range(int(1+(200-100*a-50*b)/20)):  #20
						for d in range(int(1+(200-100*a-50*b-20*c)/10)):  #10
								for e in range(int(1+(200-100*a-50*b-20*c-10*d)/5)):    #5
										for f in range(int(1+(200-100*a-50*b-20*c-10*d-5*e)/2)):
											counter += 1

# Total number of ways we can form the 200p
print(counter)