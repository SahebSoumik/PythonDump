nterms=int(input("How many Terms : "))

n1,n2=0,1
count=0

if nterms<=0:
     print("Please enter a valid positive integer")

elif nterms==1:
     print("Fibonacci seires upto 1 is 0")

else:
     print("Fibonacci series is : ")
     while count<nterms:
          print(n1)
          nth=n1+n2
          n1=n2
          n2=nth
          count+=1
