#python program to print the Floyed's Triangle
rows=int(input("Enter the number of Rows: "))
number=1

print("Floyed's Triangle")
for i in range(1,rows+1):
     for j in range(1,i+1):
          print(number,end=' ')
          number+=1
     print()
     
