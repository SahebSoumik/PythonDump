#swapping the numbers using temporary value

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print("The numbers before swap : ",num1,num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("the numbers after swap : ",num1,num2)
