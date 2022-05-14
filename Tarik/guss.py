from tkinter import *
from tkinter import messagebox
import random
root=Tk()
def save():
     num1=int(e1.get())
     num2=int(e2.get())
     num3=int(e3.get())
     guss=random.randint(num1,num2)
     if guss>num3:
          messagebox.showinfo("Value","The guess is low")
     elif guss<num3:
          messagebox.showinfo("Value","The Guss is higher")
     else:
          messagebox.showinfo("Value","The Guess is right")
Label(root,text="Enter the 1st number : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)
Label(root,text="Enter the 2nd number : ").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)
Label(root,text="Enter guss number: ").grid(row=2,column=0)
e3=Entry(root)
e3.grid(row=2,column=1)

Button(root,text="Submit",command=save).grid(row=5,column=5)
