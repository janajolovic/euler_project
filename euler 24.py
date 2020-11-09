#we create an empty list for permutations
per_list = []
import itertools
#this is list of numbers
lst = [0,1,2,3,4,5,6,7,8,9]
#we append permutations of numbers in per_list
per_list.append(list(itertools.permutations(lst)))
#we print per_list
print(per_list)