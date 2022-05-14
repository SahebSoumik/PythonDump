from tkinter import *
from tkinter import messagebox

root=Tk()

def save():
     num1=int(e1.get())
     num2=int(e2.get())

     if num2==1:
          messagebox.showinfo('Value','The money will be : {}'.format(num1/75))
     elif num2==2:
          messagebox.showinfo('Value','The money will be : {}'.format(num1/90))
     else:
          messagebox.showinfo('Value','The choice is invalid')

Label(root,text="Enter the Currency in INR : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Label(root,text="Choose the Conversion between 1.USD 2.Pound  : ").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

Button(root,text='Submit',command=save).grid(row=2,column=2)
