year=int(input("Enter the year : "))

if(year%400==0) and(year%100==0):
     print("The year is leap year ",year)

elif (year%4==0) and (year%100 !=0):
     print("The year is leap year " ,year)

else:
     print("This is not a leap year",year)
