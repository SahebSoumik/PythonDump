from tkinter import *
import random
from tkinter import messagebox

root=Tk()

def submit():
     num1=int(e1.get())
     num2=int(e2.get())
     num3=int(e3.get())

     guss=random.randint(num1,num2)

     if num3>guss:
          messagebox.showinfo('Value','The guss is high')
     elif num3<guss:
          messagebox.showinfo('Value','The guss is low')
     else:
          messagebox.showinfo('Value','The guss is correct')

Label(root,text="Enter the 1st number : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Label(root,text="Enter the 2nd number : ").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

Label(root,text="Enter the guess number : ").grid(row=2,column=0)
e3=Entry(root)
e3.grid(row=2,column=1)

Button(root,text="Submit",command=submit).grid(row=3,column=3)


