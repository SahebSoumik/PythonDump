# Factorial of a number
num=int(input("Enter the number to find the factorial : "))

fact=1

if num<0:
     print("Please provide a positive integer")
elif num==0:
     print("Factorial of 0 is 1")
else:
     print("The factorial is :")
     for i in range(1,num+1):
          fact=fact*i

     print(fact)
