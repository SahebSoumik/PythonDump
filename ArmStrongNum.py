#Armstrong number

num=int(input("Enter a number : "))

sum=0

temp=num

while temp>0:
     digit=temp%10
     sum+=digit**3
     temp//=10

if num==sum:
     print(num,"It is an Armstrong number ")
else:
     print(num,"It is not an Armstrong number")
