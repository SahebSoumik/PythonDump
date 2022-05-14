print ("Liam Evans")


a=int(input("Enter the number to find the factorial : "))
fact=1

if a<0:
     print("Negative value... please provide positive one")
elif a==0:
     print("the factorial for 0 is 1")
else:
     print("the factorial is : ")
     for i in range(1,a+1):
          fact=fact*i

     print(fact)
          
          

