# def Demo():
#     print("This is from the Demo Method")

# Demo()

# calculator program using function
def addition(a,b):
    return a+b
def subs(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
add=addition(a,b)
sub=subs(a,b)
mult=mul(a,b)
divition=div(a,b)
print("The addition is : ",add)
print("The subsraction is : ",sub)
print("The mult is : ",mult)
print("The divition is : ",divition)

