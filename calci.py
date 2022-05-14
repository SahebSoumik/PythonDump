from tkinter import *
from tkinter import messagebox


root=Tk()

def add():
     num1=int(e1.get())
     num2=int(e2.get())

     ans=num1+num2

     messagebox.showinfo('Addition',"The addition is : {}".format(ans))

Label(root,text="Enter the 1st number : ").grid(row=0,column=1)
e1=Entry(root)
e1.grid(row=0,column=2)

Label(root,text="Enter the 2nd number : ").grid(row=1,column=2)
e2=Entry(root)
e2.grid(row=1,column=3)

Button(root,text="+",command=add).grid(row=5,column=5)



