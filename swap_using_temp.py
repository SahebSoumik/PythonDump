# Swapping numbers using temporary variable
num1=int(input("Enter the 1st number  : "))
num2=int(input("Enter the 2nd number : "))

temp=0

print("The value in num1 is (before swap) : ",num1)
print("The value in num2 is (before swap): ",num2)

temp=num1
num1=num2
num2=temp

print("The value in num1 is (after swap): ",num1)
print("The value in num2 is (after swap): ",num2)
