from tkinter import *
from tkinter import messagebox


def check():
     num1=int(e1.get())

     if num1%2==0:
          messagebox.showinfo("OddEven",'The number is Even : {}'.format(num1))

     else:
          messagebox.showinfo("OddEven",'The Number is odd : {}'.format(num2))

root=Tk()

Label(root,text="Enter the number to check if it is a odd or a even number : ").grid(row=0,column=0)
e1=Entry(root)

e1.grid(row=0,column=1)

Button(root,text="Submit",command=check).grid(row=2,column=2)
