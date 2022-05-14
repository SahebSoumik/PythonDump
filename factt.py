n=int(input("Enter the number to make the factorial : "))

fact=1

if n<0:
     print("Please enter a positive number")
elif n==0:
     print("factorial of 0 is 1")
else:
     for i in range(1,n+1):
          fact=fact*i

     print(fact)
