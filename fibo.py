# Program to find the fibonacci series

nterms=int(input("How many terms you want : "))

n1,n2=0,1

count=0

#if the of terms is valid or not
if nterms<=0:
     print("Please enter a positive integer")
elif nterms==1:
     print("The fibonacci series will be",n1)
else:
     print("Fibonacci series is : ")
     while count<nterms:
          print(n1)
          nth=n1+n2
          n1=n2
          n2=nth
          count+=1
