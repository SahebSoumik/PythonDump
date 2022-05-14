from tkinter import *
from tkinter import messagebox
import random

def guess():
     num1=int(e1.get())
     num2=int(e2.get())
     num3=int(e3.get())

     g=random.randint(num1,num2)

     if g>num3:
          messagebox.showinfo('Alert','The guess is low')
     elif g<num3:
          messagebox.showinfo('Alert','The guess is high')
     else:
          messagebox.showinfo('Alert','The guess is right')

root=Tk()

Label(root,text="Enter the first number : ").grid(row=0,column=0)

e1=Entry(root)

e1.grid(row=0,column=1)

Label(root,text="Enter the Second number : ").grid(row=1,column=0)

e2=Entry(root)

e2.grid(row=1,column=1)

Label(root,text="Enter the Guess Number : ").grid(row=2,column=0)

e3=Entry(root)

e3.grid(row=2,column=1)

Button(root,text="Submit",command=guess).grid(row=3,column=3)
