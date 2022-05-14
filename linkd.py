class node:
     def __init__(self,dataval=None):
          self.dataval=dataval
          self.nextval=None

class SLinkedList:
     def __init__(self):
          self.headval=None

     def listprint(self):
          printval=self.headval

          while printval is not None:
               print(printval.dataval)
               printval=printval.nextval

list=SLinkedList()
list.headval=node("Mon")
e2=node("Tue")
e3=node("wed")

list.headval.nextval=e2

e2.nextval=e3

list.listprint()






