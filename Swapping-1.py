#swapping the numbers using temporary value

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print("The numbers before swap : ",num1,num2)

temp=0

temp=num1
num1=num2
num2=temp

print("The numbers after swap : ",num1,num2)

