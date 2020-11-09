#we import datetime from date
from datetime import date
#this is counter for sundays that fell on the first of the month
sundays=0
#we go through the for loop for years and months
for year in range(1901,2001):
	for month in range(1,13):
        #if first of the month is equal to 6 (sunday)
		if date(year,month,1).weekday() == 6:
            #then counter increses by 1
		    sundays+=1
#we print number of sundays that fell on the first of the month during the twentieth century
print(sundays)