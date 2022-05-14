#Q1. Write a program to find the factorial of a given number:
num=int(input("Enter the number  : "))

fact=1

if num<0:
     print("We cannot find any factorial for negative number")
elif num==0:
     print(" factorial of 0 is 1")
else:
     print("The factorial is : ")
     for i in range(1,num+1):
          fact=fact*i

     print(fact)
          
