#Factorial of a number
num=int(input("Enter the first number : "))

fact=1

#conditions

if num<0:
     print("Please provide a positive integer")

elif num==0:
     print("The factorial of 0 is 1")

else:
     for i in range(1,num+1):
          fact=fact*i

     print("The factorial is : ",fact)

