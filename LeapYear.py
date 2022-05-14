year=2000
if(year%400==0) and (year%100==0):
     print("{} is a leap year".format(year))

elif(year%4==0) and (year%100!=0):
     print("{} is a leap year".format(year))

else:
     print("{} it is not a leap year".format(year))
