#Swapping the numbers without using temporary variable

num1=int(input("Enter the 1st number : "))
num2=int(input("Enter the 2nd number : "))

print("The value before swap : ",num1)
print("The value before swap : ",num2)

num1=num1+num2
num2=num1-num2
num1=num1-num2

print("The value after swap: ",num1)
print("The Value after swap : ",num2)
