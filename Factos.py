#Factorial of a number

a=int(input("Enter a number to find a factorial : "))

fact=1

if a<0:
     print("IT is not possible to find the factorial of a negative number")
elif a==0:
     print("The factorial of 0 is always 1")
else:
     for i in range(1,a+1):
          fact=fact*i

     print("The factorial is : ",fact)
