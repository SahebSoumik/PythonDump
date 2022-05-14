#fibonacci series:

nterms=int(input("Enter the first number : "))

n1=0
n2=1

count=0

if nterms<0:
     print("please provide a positive integer")
elif nterms==0:
     print("Please provide a number")
else:
     while count<nterms:
          print(n1)
          nth=n1+n2
          n1=n2
          n2=nth
          count+=1



          
