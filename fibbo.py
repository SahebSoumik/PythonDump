# fibonacci series :
nterms=int(input("Enter the number of terms : "))

n1,n2=0,1

count=0

if nterms<0:
     print("Please provide a positive integer")
elif nterms==1:
     print("For 1 term the series will be 0")
else:
     print("Fibonacci series are : ")
     while count<nterms:
          print(n1)
          nth=n1+n2
          n1=n2
          n2=nth
          count+=1
          
