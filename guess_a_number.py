import random

a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))

c=int(input("Enter the guess number : "))

d=random.randint(a,b)

if c>d:
     print("My Guess is high")
elif c<d:
     print("My guess is low")

else:
     print("Perfect Guess")
     

