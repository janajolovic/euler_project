sum_num = 0
#we go through the for lopp to 1000000
for a in range(1,1000000):
    #we fisrt found the reverse_a  
    reverse_a = int(str(a)[::-1])
    #then we calculate the binary a (we start from 2 because of '0b' tags in binary number)
    bin_a = bin(a)[2:]
    #then we found the reverse of binary a
    reverse_bin_a = bin_a[::-1]
    #if this conditions are fulfilled
    if bin_a == reverse_bin_a and a == reverse_a:
        #then sum_num increases by 1
        sum_num += a
#we print the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
print(sum_num)