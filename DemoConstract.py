class Employee:
     def __init__(self,name,id):
          self.id=id
          self.name=name

     def display(self):
          print("ID : %d, Name: %s"%(self.id,self.name))

emp1=Employee("John",10)
emp2=Employee("David",10)

emp1.display()
emp2.display()
