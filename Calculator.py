from cProfile import label
from logging import root
from tkinter import *
from tkinter import messagebox

root=Tk()

def add():
    a=int(e1.get())
    b=int(e2.get())

    messagebox.showinfo('Result','The addition is : {}'.format(a+b))


def sub():
    a=int(e1.get())
    b=int(e2.get())

    messagebox.showinfo('Result','The substraction is : {}'.format(a-b))


def mult():
    a=int(e1.get())
    b=int(e2.get())

    messagebox.showinfo('Result','The Multiplecation is : {}'.format(a*b))


def div():
    a=int(e1.get())
    b=int(e2.get())

    messagebox.showinfo('Result','The addition is : {}'.format(a/b))



Label(root,text="Enter the first number : ").grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Label(root,text="Enter the second number : ").grid(row=1,column=0)
e2=Entry(root)
e2.grid(row=1,column=1)

Button(root,text="+",command=add).grid(row=2,column=2)
Button(root,text="-",command=sub).grid(row=3,column=3)
Button(root,text="*",command=mult).grid(row=4,column=4)
Button(root,text="/",command=div).grid(row=6,column=6)