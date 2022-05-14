year=int(input("Enter the year:"))

if(year%400==0) and (year%100==0):
     print("the year is a leap year : ",year)

elif(year%4==0) and (year%100!=0):
     print("the year is a leap year : ",year)

else:
     print("the year is not a leap year",year)
