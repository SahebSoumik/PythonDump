from tkinter import *
from tkinter import messagebox
import random

root=Tk()

def fun():
     a=int(e1.get())
     b=int(e2.get())
     c=int(e3.get())

     ran=random.randint(a,b)

     if c>ran:
          messagebox.showinfo('Guess','guess is greater than the actual number')

     elif c<ran:
          messagebox.showinfo('Guess','Guess is smaller than the actual number')

     else:
          messagebox.showinfo('Guess','Guess is Correct !!')
     

root.geometry("500x500")

Label(root,text="Enter the initial number : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)


Label(root,text="Enter the final number : ").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)


Label(root,text="Enter the Guess number : ").grid(row=2,column=0)
e3=Entry(root)
e3.grid(row=2,column=1)

Button(root,text="Submit",command=fun).grid(row=3,column=0)
