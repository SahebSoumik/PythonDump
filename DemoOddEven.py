# to find the odd and even number in between a given range
num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))

for i in range(num1,num2):
     if i%2==0:
          print("{} the number is even".format(i))
     else:
          print("{} the number is odd".format(i))

     
