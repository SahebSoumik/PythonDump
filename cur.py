from tkinter import *
from tkinter import messagebox

root=Tk()

def show():
     cur=int(e1.get())

     inr=cur*75.06

     messagebox.showinfo('Value','The the value in INR is : {}'.format(inr))


Label(root,text='Enter doller : ').grid(row=0,column=0)
e1=Entry(root)
e1.grid(row=0,column=1)

Button(root,text='Submit',command=show).grid(row=5,column=5)
